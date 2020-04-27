from django.urls import path
from . import views 

app_name = 'blog'
urlpatterns = [
    # post views
    # path('', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('<slug:post_slug>/',
         views.post_detail,
         name='post_detail'),
    path('<int:id>/<slug:slug>/',
         views.chapter_detail,
         name='chapter_detail')
] 