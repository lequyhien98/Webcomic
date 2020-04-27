from django.shortcuts import render, get_object_or_404 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Post, Chapter


def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/list.html',
                  {'page': page,
                   'posts': posts})


def post_detail(request, post_slug=None):
    post = get_object_or_404(Post, slug=post_slug,
                                   status='published')
    return render(request,
                  'blog/detail.html',
                  {'post': post})

def chapter_detail(request, id, slug):
    chapter = get_object_or_404(Chapter, id=id , slug=slug,
                                   status='published')
    return render(request,
                  'blog/chapter_detail.html',
                  {'chapter': chapter})


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/list.html'
