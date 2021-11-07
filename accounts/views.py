from django.urls import reverse_lazy
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .forms import ProfileForm,MySignUpForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

class SignUpView(generic.CreateView):
    form_class = MySignUpForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'

class MypageView(LoginRequiredMixin,generic.ListView):
    model = CustomUser 
    template_name = 'index.html'
    
class MypageView(LoginRequiredMixin, generic.DetailView):
    model = CustomUser
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = 'account/mypage.html'

class Mypage_Edit(LoginRequiredMixin,SuccessMessageMixin,generic.UpdateView): 
    model = CustomUser
    form_class = ProfileForm
    template_name = 'account/mypage_edit.html'
    success_message = 'プロフィールを変更しました。'

#処理終了後の遷移先指定
    def get_success_url(self):#処理成功時に移動する動的に変化するurlを指定する（オーバーライド）
        return reverse_lazy('accounts:mypage',kwargs={'pk':self.kwargs['pk']})
    #urlの逆引きを行う。urlのハードコーディングを無くす効果がある？ 
    # self.kwargsのpkを辞書にしている。それをkwargsに格納？
 #他人が自分のプロフィールをみるためのview
class ReviewerView(LoginRequiredMixin,generic.DetailView):
    model = CustomUser
    slug_field = "username"
    slug_url_kwargs = "username"
    template_name = 'account/reviewer.html'

class Account_DeleteView(LoginRequiredMixin,generic.DeleteView):
    model = CustomUser
    template_name = 'account/customuser_confirm_delete.html'
    success_url = reverse_lazy('timeline:index')
    
    def delete(self,request,*args,**kwargs):
        messages.success(self.request, "退会しました。")
        return super().delete(request,*args,**kwargs)



