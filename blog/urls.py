from django.urls import path, re_path
from . import views 

app_name = 'blog'
urlpatterns = [
    # post views
    # path('', views.post_list, name='post_list'),
    # path('<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
    path('the-loai/', views.genre_list, name='genre-list'),
    path('<slug:slug>/', views.post_detail, name='post-detail'),
    # path('the-loai/', views.GenreListView.as_view(), name='genre-list'),
    path('the-loai/<slug:slug>/', views.genre_detail, name='genre-detail'),
    path('chap/<slug:post_slug>/<slug:chap_slug>/',
          views.chap_detail,
          name='chap-detail'),
]