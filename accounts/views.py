from django.views import generic
from .forms import ProfileForm,MySignUpForm
from .models import CustomUser
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


class SignUpView(generic.CreateView):
    form_class = MySignUpForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'
    
class MypageView(LoginRequiredMixin, generic.DetailView):
    model = CustomUser
    template_name = 'account/mypage.html'

class Mypage_Edit(LoginRequiredMixin,SuccessMessageMixin,generic.UpdateView): 
    model = CustomUser
    form_class = ProfileForm
    template_name = 'account/mypage_edit.html'
    success_message = 'プロフィールを変更しました。'

    def get_success_url(self):
        return reverse_lazy('accounts:mypage',kwargs={'pk':self.kwargs['pk']})
    
    
class ReviewerView(LoginRequiredMixin,generic.DetailView):
    model = CustomUser
    template_name = 'account/reviewer.html'

class Account_DeleteView(LoginRequiredMixin,generic.DeleteView):
    model = CustomUser
    template_name = 'account/customuser_confirm_delete.html'
    success_url = reverse_lazy('timeline:index')
    
    def delete(self,request,*args,**kwargs):
        messages.success(self.request, "退会処理が完了しました。")
        return super().delete(request,*args,**kwargs) 