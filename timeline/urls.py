from django.urls import path
from . import views


app_name = 'timeline'

urlpatterns = [
    path('', views.index, name='index'),
    #path('<int:num>/', views.index, name='index'),
    #path('like/', views.LikeView.as_view(), name='like'),
    path('post_list/<str:racket_url_name>/', views.post_list, name='post_list'),
    path('mypost_list/<int:pk>/', views.MyPostListView.as_view(), name='mypost_list'),
    path('post_create/<str:racket_url_name>/', views.create_view, name='post_create'),
    path('post_edit/<slug:racket_url_name>/<int:pk>/', views.Post_EditView.as_view(), name='post_edit'),
    path('mypost_edit/<slug:racket_url_name>/<int:pk>/', views.MyPost_EditView.as_view(), name='mypost_edit'),
    path('post_confirm_delete/<slug:racket_url_name>/<int:pk>/', views.Post_DeleteView.as_view(), name='post_confirm_delete'),
    path('mypost_confirm_delete/<slug:racket_url_name>/<int:pk>/', views.MyPost_DeleteView.as_view(), name='mypost_confirm_delete'),
    path('like/', views.LikeView, name='like'),
    path('liked_post_list/<int:pk>/', views.Liked_PostListView, name='liked_post_list'),
]