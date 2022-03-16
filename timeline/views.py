from django.shortcuts import render,redirect,get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm,BrandSearchForm,ContactForm
from .models import Post, Like,Item
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http.response import JsonResponse
from django import forms


def paginate_queryset(request, queryset, count):
    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        paginate_count = paginator.page(page)
    except PageNotAnInteger:
        paginate_count = paginator.page(1)
    except EmptyPage:
        paginate_count = paginator.page(paginator.num_pages)
    return paginate_count


def Index(request):
    global items
    query = request.GET.get('selected-name')
    if query:
        if query == 'YONEX' or query == 'MIZUNO' or query == 'DUNLOP':
            items = Item.objects.filter(brand_name = query) 
        else:
            items =Item.objects.filter(series_name = query)
    else:
        items = Item.objects.all()
       

    params = {
        'item_objects' : items,
    }
    return render(request, 'index.html', params)

def Site_Information(request):
    return render(request, 'site_information.html')

def Post_List_View(request,slug):
    item_data = Item.objects.get(slug = slug)
    post_object_list = Post.objects.filter(item__slug = slug)
    url_value = 'postlist'
    post_count = post_object_list.count()
    paginate_count = paginate_queryset(request, post_object_list, 10)
    liked_list = []
    current_user = request.user
    if (current_user.is_authenticated):
        for post in post_object_list:
            liked = post.like_set.filter(user=request.user)
            if liked.exists():
                liked_list.append(post.pk)

    params = {
        'item_data':item_data,
        'object_list':paginate_count.object_list,
        'url_value':url_value,
        'post_count':post_count,
        'page_obj':paginate_count,
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
    like_data = Like.objects.filter(user=request.user)
    all_post = Post.objects.all()
    url_value = 'liked'
    liked_list = []
    for post in all_post:
        liked = post.like_set.filter(user=request.user)
        if liked.exists():
            liked_list.append(post.pk)

    paginate_count = paginate_queryset(request, like_data, 30)

    params = {
        'object_list' :like_data,
        'url_value':url_value,
        'liked_list' :liked_list,
        'page_obj':paginate_count,
    }
    return render(request, 'liked_post_list.html',params)


class MyPost_List_View(LoginRequiredMixin,generic.ListView):
    template_name = 'mypost_list.html'
    model = Post 
    paginate_by = 15
    
    def get_context_data(self, **kwargs):
        all_post = Post.objects.filter(author = self.request.user.id)
        context = super().get_context_data(**kwargs)
        liked_list = []
        current_user = self.request.user
        if (current_user.is_authenticated):
            for post in all_post:
                liked = post.like_set.filter(user=current_user)
                if liked.exists():
                    liked_list.append(post.pk)
        context["liked_list"] = liked_list
        context['url_value'] = 'mypost'
        return context

    def get_queryset(self):
        return Post.objects.filter(author = self.request.user.id)


@login_required
def Post_Create_View(request,slug): #レビュー作成関数
    if (request.method == "POST"):
        form = PostForm(request.POST,request.FILES) 
        if form.is_valid():
            post = form.save(commit = False)#フォームに入力された内容を一時的に保持
            try:
                post.author = request.user #postテーブルのauthorにリクエストされてきたログインユーザーpkを格納
                post.item = Item.objects.get(slug = slug) 
            except IntegrityError:
                    return post
            post.save() 
            messages.success(request, 'レビューを作成しました。')
            return redirect('timeline:post_list',slug = slug)
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form})


class Post_EditView(LoginRequiredMixin,SuccessMessageMixin,generic.UpdateView):
    model = Post
    slug_field = "Item__slug"
    form_class = PostForm
    template_name = 'post_edit.html'
    success_message = 'レビューを変更しました。'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.edited = "True"
        post.save()
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request,"変更に失敗しました。")
        return super().form_invalid(form)

    def get_success_url(self):
        referer = self.request.META['HTTP_REFERER']
        if 'mypost' in referer:
            return reverse_lazy('timeline:mypost_list',kwargs={'pk':self.request.user.pk})
        elif 'liked' in referer:
            return reverse_lazy('timeline:liked_post_list',kwargs={'pk':self.request.user.pk})
        else:
            return reverse_lazy('timeline:post_list',kwargs={'slug':self.object.item.slug})


class Post_DeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    slug_field = "slug"
    template_name = 'post_confirm_delete.html'
     
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author == request.user: 
            messages.success(self.request, 'レビューを削除しました。')
        return super().delete(request, *args, **kwargs)
    
    def get_success_url(self):
        referer = self.request.META['HTTP_REFERER']
        if 'mypost' in referer:
            return reverse_lazy('timeline:mypost_list',kwargs={'pk':self.request.user.pk})
        elif 'liked' in referer:
            return reverse_lazy('timeline:liked_post_list',kwargs={'pk':self.request.user.pk})
        else:
            return reverse_lazy('timeline:post_list',kwargs={'slug':self.object.item.slug})
       
       
class ContactFormView(LoginRequiredMixin,SuccessMessageMixin,generic.FormView):
    template_name = 'contact_form.html'
    form_class = ContactForm
    success_message = 'お問い合わせ内容を送信しました。'
    
    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('timeline:index')
