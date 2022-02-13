from django.urls import path
from . import views
from .views import ContactFormView

app_name = 'timeline'
urlpatterns = [
    path('', views.Index, name='index'),
    path('site_information/', views.Site_Information, name='site_information'),
    path('post_list/<str:slug>/', views.Post_List_View, name='post_list'),
    path('mypost_list/<int:pk>/', views.MyPost_List_View.as_view(), name='mypost_list'),
    path('post_create/<str:slug>/', views.Post_Create_View, name='post_create'),
    path('post_edit/<slug:slug>/<int:pk>/<str:url_value>/', views.Post_EditView.as_view(), name='post_edit'),
    path('post_confirm_delete/<slug:slug>/<int:pk>/<str:url_value>/', views.Post_DeleteView.as_view(), name='post_confirm_delete'),
    path('like/', views.LikeView, name='like'),
    path('liked_post_list/<int:pk>/', views.Liked_PostListView, name='liked_post_list'),
    path('contact/', ContactFormView.as_view(), name='contact_form'),
]
