from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm,BrandSearchForm,ReviewSearchForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .models import Post, Like,ProductModel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http.response import JsonResponse


def paginate_queryset(request, queryset, count):
    """Pageオブジェクトを返す。

    countは、1ページに表示する件数
    返却するPgaeオブジェクトは、以下のような感じで使えます。
        {% if page_obj.has_previous %}
          <a href="?page={{ page_obj.previous_page_number }}">Prev</a>
        {% endif %}

    また、page_obj.object_list で、count件数分の絞り込まれたquerysetが取得できます。

    """
    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        page_count = paginator.page(page)
    except PageNotAnInteger:
        page_count = paginator.page(1)
    except EmptyPage:
        page_count = paginator.page(paginator.num_pages)
    return page_count

def index(request):
    if(request.method == 'POST'): #リクエストされたブランドと一致する商品を一覧として表示する
        form = BrandSearchForm(request.POST) #扱うフォームを指定
        if 'button_all' in request.POST: #押されたボタンのnameからラケットを絞り込む
            product_data = ProductModel.objects.filter(display=True)
        elif 'button_yonex' in request.POST: #押されたボタンのnameからラケットを絞り込む
            product_data = ProductModel.objects.filter(brand='yonex',display=True)
        elif 'button_mizuno' in request.POST:
            product_data = ProductModel.objects.filter(brand='mizuno',display=True)
        elif 'button_dunlop' in request.POST:
            product_data = ProductModel.objects.filter(brand='dunlop',display=True)
        elif 'button_srixon' in request.POST:
            product_data = ProductModel.objects.filter(brand='srixon',display=True)
        elif 'button_gosen' in request.POST:
            product_data = ProductModel.objects.filter(brand='gosen',display=True)
        #brand_data = request.POST['brand'] #フォームからポストされてきたデータをbrand_dataに格納
        #product_data = ProductModel.objects.filter(brand = brand_data) #絞り込みの処理
    else:
        form = BrandSearchForm() #検索されていなければ商品を全て表示
        product_data = ProductModel.objects.filter(display=True)
    
    page_count = paginate_queryset(request, product_data, 30)
    
    params = {
        'form' : form,
        'product_data' :  page_count.object_list,
        'page_obj' :  page_count,
        
    }
    return render(request, 'index.html', params)    

def post_list(request,racket_url_name): 
    product_data = ProductModel.objects.get(racket_url_name = racket_url_name)#取得したpkと同じ商品の情報を取得
    object_list = Post.objects.filter(product_id__racket_url_name= racket_url_name) 
    object_count = Post.objects.filter(product_id__racket_url_name= racket_url_name).count()
    page_count = paginate_queryset(request, object_list, 20)
    liked_list = []
    current_user = request.user
    if (current_user.is_authenticated):
        for post in object_list:
            liked = post.like_set.filter(user=request.user)
            if liked.exists():
                liked_list.append(post.pk)
                
    params = {
        'product_data':product_data,
        'object_list':page_count.object_list,
        'object_count':object_count,
        'page_obj':page_count,
        'liked_list' :liked_list,
    }
    return render(request, 'post_list.html',params)
    
@login_required
def LikeView(request):
    if request.method =="POST":
        post = get_object_or_404(Post, pk=request.POST.get('post_pk'))
        current_user = request.user
        liked = False
        like = Like.objects.filter(post=post, user=current_user)
        if like.exists():
            like.delete()
        else:
            like.create(post=post, user=current_user)
            liked = True
                
        context={
            'post_pk': post.pk,
            'liked': liked,
            'count': post.like_set.count(),
        }
    if request.is_ajax():
        return JsonResponse(context)
    
@login_required
def Liked_PostListView(request,pk):
    current_user = request.user
    like_data = Like.objects.filter(user=current_user)
    all_post = Post.objects.all()
    liked_list = []
    for post in all_post:
        liked = post.like_set.filter(user=request.user)
        if liked.exists():
            liked_list.append(post.pk)
    page_count = paginate_queryset(request, like_data, 10)
    
    params = {
        'object_list' :like_data,
        'liked_list' :liked_list,
        'page_obj':page_count,
    }
    return render(request, 'liked_post_list.html',params)
    
    
# テンプレートpost_listに移動,base.htmlにjavascriptのcdm,ajax.js,などを追加,cssデザイン追加
#Ajax.jsを作成、処理を記述

class MyPostListView(LoginRequiredMixin,generic.ListView):
    template_name = 'mypost_list.html'
    model = Post 
    paginate_by = 15
    
    def get_queryset(self):
        current_user = self.request.user
        return Post.objects.filter(author=current_user.id)

@login_required
def create_view(request,racket_url_name): #レビュー作成関数
    if (request.method == "POST"):
        form = PostForm(request.POST,request.FILES) #扱うフォームを指定
        if form.is_valid():
            post = form.save(commit=False)#フォームに入力された内容を一時的に保持
            post.author = request.user #postテーブルのauthorにリクエストされてきたログインユーザーpkを格納
            
            product_info = ProductModel.objects.get(racket_url_name= racket_url_name) 
            #商品テーブルから取得してきたnameと同じラケットidをpostのラケットidに格納 
            post.product_id =  product_info
            #レビューするの商品pkをpostテーブルのproductカラムに格納
            post.save() 
            messages.success(request, 'レビューを作成しました。')
            return redirect('timeline:post_list',racket_url_name = racket_url_name)
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form})
    
#投稿編集

class Post_EditView(LoginRequiredMixin,SuccessMessageMixin,generic.UpdateView): 
    model = Post
    slug_field = "ProductModel__racket_url_name"
    slug_url_kwarg = "ProductModel__racket_url_name"
    form_class = PostForm
    template_name = 'post_edit.html'
    success_message = 'レビューを変更しました。'

#処理終了後の遷移先指定
    def get_success_url(self):
        return reverse_lazy('timeline:post_list',kwargs={'racket_url_name':self.object.product_id.racket_url_name})

class MyPost_EditView(LoginRequiredMixin,SuccessMessageMixin,generic.UpdateView): 
    model = Post
    slug_field = "ProductModel__racket_url_name"
    form_class = PostForm
    template_name = 'mypost_edit.html'
    success_message = 'レビューを変更しました。'

#処理終了後の遷移先指定

    def get_success_url(self):
        return reverse_lazy('timeline:mypost_list',kwargs={'pk':self.request.user.pk})
       

    #投稿削除(post_listから)
class Post_DeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    slug_field = "racket_url_name"
    #slug_url_kwarg = "racket_url_name"
    template_name = 'post_confirm_delete.html'
    #success_url = reverse_lazy('timeline:index')
    def get_success_url(self):
        return reverse_lazy('timeline:post_list',kwargs={'racket_url_name':self.object.product_id.racket_url_name})
    #投稿削除(mypost_listから)
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author == request.user: 
            #取得したユーザーがログインしているユーザーと同じであればif文実行
            messages.success(self.request, 'レビューを削除しました。')
        return super().delete(request, *args, **kwargs)
    
class MyPost_DeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    slug_field = "racket_url_name"
    #slug_url_kwarg = "racket_url_name"
    template_name = 'mypost_confirm_delete.html'
    #success_url = reverse_lazy('timeline:index')
    def get_success_url(self):
        return reverse_lazy('timeline:mypost_list',kwargs={'pk':self.request.user.pk})
        
        
        """
        url = reverse(request.META.get('HTTP_REFERER', '/'), kwargs={'groups': groups, 'product': product})
    return HttpResponseRedirect(url)
        if "posted" in path_x:
            return reverse_lazy('timeline:posted_list',kwargs={'pk':self.request.user.pk})
        else:
            return reverse_lazy('timeline:post_list',kwargs={'pk':self.object.product_id.racket_url_name})
        """
        
#if 送信元がpostedだったとき→投稿一覧に行く。それ以外は投稿リストにいく。

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author == request.user: 
            #取得したユーザーがログインしているユーザーと同じであればif文実行
            messages.success(self.request, 'レビューを削除しました。')
        return super().delete(request, *args, **kwargs)
        
        
"""
class LikeView(LoginRequiredMixin, generic.View):
    model = Like

    def post(self, request):
        post_pk = request.POST.get('pk')
        post = Post.objects.get(pk=post_pk)
        like = Like(user=self.request.user,post=post)
        like.save()
        like_count = Like.objects.filter(post=post).count()
        data = {'message': 'ほめました',
                'like_count': like_count}
        return JsonResponse(data)
        """