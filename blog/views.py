from django.shortcuts import render, get_object_or_404 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.db.models import Max
from .models import Post, Chapter, Genre


def post_list(request):
    posts = Post.published.all()
    context = {
        'posts ': posts ,
    }

    return render(request, 'blog/list.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id,
                                   status='published')
    return render(request,
                  'blog/detail.html',
                  {'post': post})

def chapter_detail(request, post_id, chap_id):
    post = get_object_or_404(Post, id=post_id,
                                   status='published')
    chapter = get_object_or_404(Chapter, post=post , id=chap_id,
                                   status='published')
    return render(request,
                  'blog/chapter_detail.html',
                  {'chapter': chapter})

def genre_list(request):
    # object_list = Post.published.all()
    genres = Genre.objects.all()
    # genre = get_object_or_404(Genre, id=genre_id)
    # object_list = object_list.filter(genre=genre)

    # paginator = Paginator(object_list, 3) # 3 posts in each page
    # page = request.GET.get('page')
    # try:
    #     posts = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer deliver the first page
    #     posts = paginator.page(1)
    # except EmptyPage:
        # If page is out of range deliver last page of results
        # posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/genre_list.html',
                  {
                    #   'page': page,
                #    'posts': posts,
                #    'genre': genre,
                   'genres': genres})

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/list.html'
