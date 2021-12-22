from django.urls import path
from . import views

app_name = 'timeline'

urlpatterns = [
    path('', views.Index, name='index'),
    path('post_list/<str:slug>/', views.Post_List_View, name='post_list'),
    path('mypost_list/<int:pk>/', views.MyPost_List_View.as_view(), name='mypost_list'),
    path('post_create/<str:slug>/', views.Post_Create_View, name='post_create'),
    path('post_edit/<slug:slug>/<int:pk>/', views.Post_EditView.as_view(), name='post_edit'),
    path('mypost_edit/<slug:slug>/<int:pk>/', views.MyPost_EditView.as_view(), name='mypost_edit'),
    path('post_confirm_delete/<slug:slug>/<int:pk>/', views.Post_DeleteView.as_view(), name='post_confirm_delete'),
    path('mypost_confirm_delete/<slug:slug>/<int:pk>/', views.MyPost_DeleteView.as_view(), name='mypost_confirm_delete'),
    path('like/', views.LikeView, name='like'),
    path('liked_post_list/<int:pk>/', views.Liked_PostListView, name='liked_post_list'),
]