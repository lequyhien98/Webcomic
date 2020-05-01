from django.urls import path, re_path
from . import views 

app_name = 'blog'
urlpatterns = [
    # post views
    # path('', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name='post-list'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
    path('the-loai', views.GenreListView.as_view(), name='genre-list'),
    path('the-loai/<slug:slug>/', views.GenreDetailView.as_view(), name='genre-detail'),
    path('chap/<slug:post_slug>/<slug:chap_slug>/',
          views.chap_detail,
          name='chap-detail'),
    # re_path('tim-kiem/$',
    #     views.TitleAutocomplete.as_view(),
    #     name='title-autocomplete',
    # ),
] 