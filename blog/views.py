from django.shortcuts import render, get_object_or_404 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView
from dal import autocomplete
from .models import Post, Chap, Genre
from django.http import HttpResponse


def post_list(request):
    posts = Post.published.all()
    context = {
        'posts ': posts ,
    }

    return render(request, 'blog/list.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug,
                                   status='published')
    return render(request,
                  'blog/detail.html',
                  {'post': post})

def chap_detail(request, post_slug, chap_slug):
    post = get_object_or_404(Post, slug=post_slug,
                                   status='published')
    chap = get_object_or_404(Chap, post=post , slug=chap_slug,
                                   status='published')
    return render(request,
                  'blog/chap_detail.html',
                  {'chap': chap})

def genre_list(request):
    genres = Genre.objects.all()
    return render(request,
                  'blog/genres_list.html',
                  {'genres': genres})

def genre_detail(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    context = {
        'genre': genre,
    }
    return render(request, 'blog/genre_detail.html', context)

class PostListView(ListView):
    model = Post
    paginate_by = 100  # if pagination is desired
    template_name = "blog/post_list.html"
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PostDetailView(DetailView):

    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class GenreListView(ListView):
    model = Genre
    paginate_by = 100  # if pagination is desired
    template_name = "blog/genre_list.html"
    context_object_name = 'genres'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class GenreDetailView(DetailView):
    model = Genre
    paginate_by = 100  # if pagination is desired
    template_name = "blog/genre_detail.html"
    context_object_name = 'genre'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
        
# class TitleAutocomplete(autocomplete.Select2ListView):
#     def get_list(self):
#         qs = Post.published.all()
#         if self.q:
#             qs = qs.filter(title__istartswith=self.q).values('title')
        
#         titles = qs.values('title')
        
#         title_choices = []
#         for title in titles:
#             title_choices.append(title['title'])
#         return title_choices