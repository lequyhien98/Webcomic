from django.urls import path
from . import views 

app_name = 'blog'
urlpatterns = [
    # post views
    # path('', views.post_list, name='post_list'),
     path('', views.PostListView.as_view(), name='post_list'),
     path('comic/<int:post_id>/',
          views.post_detail,
          name='post_detail'),
     path('view/<int:post_id>/<int:chap_id>/',
          views.chapter_detail,
          name='chapter_detail'),
     path('genres/', views.genre_list, name='genre_list'),
] 