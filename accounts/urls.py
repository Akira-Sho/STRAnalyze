from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('mypage/<str:pk>/',views.MypageView.as_view(), name='mypage'),
    path('mypage_edit/<str:pk>/',views.Mypage_Edit.as_view(), name='mypage_edit'),
    path('reviewer/<str:pk>/',views.ReviewerView.as_view(), name='reviewer'),
    path('customuser_confirm_delete/<str:pk>/',views.Account_DeleteView.as_view(), name='customuser_confirm_delete'),
    path('accounts/signup/', views.SignUpView.as_view(),name='signup'),
]
