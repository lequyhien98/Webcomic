from django.shortcuts import render, get_object_or_404 , redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView
from .models import Post, Chap, Genre, Comment
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from django.db.models import Q

def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 12) 
    new_chaps = Chap.published.all().reverse()
    rank_like = sorted(post_list, key= lambda t: t.total_likes(), reverse=True)   

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    if page is None:
        start_index = 0
        end_index = 7
    else:
        (start_index, end_index) = proper_pagination(posts, index=4)

    page_range = list(paginator.page_range)[start_index:end_index]
    context = {
        'posts': posts,
        'page_range': page_range,
        'new_chaps': new_chaps,
        'rank_like': rank_like,
    }

    return render(request, 'blog/post_list.html', context)

def post_detail(request, slug): 
    genre_list = Genre.objects.all()
    post = get_object_or_404(Post, slug=slug,
                                   status='published')
    comments = Comment.objects.filter(post=post, reply=None).order_by('-id')
    genre_list = genre_list.filter(posts=post)
    is_liked = False

    if post.likes.filter(id=request.user.id).exists():
        is_liked = True
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(post=post, user=request.user, content=content, reply=comment_qs)
            comment.save()
            # return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form= CommentForm()


    context = {
        'post': post,
        'is_liked': is_liked,
        'total_likes': post.total_likes(),
        'genre_list': genre_list,
        'comments': comments,
        'comment_form': comment_form,
    }
    if request.is_ajax():
        html = render_to_string('blog/comments.html', context, request=request)
        return JsonResponse({'form': html})
    return render(request, 'blog/post_detail.html', context)

def chap_detail(request, post_slug, chap_slug):
    post = get_object_or_404(Post, slug=post_slug,
                                   status='published')
    chap = get_object_or_404(Chap, post=post , slug=chap_slug,
                                   status='published')
    pre_chap = post.chaps.filter(title__lt=chap.title).order_by('-title').first()
    next_chap = post.chaps.filter(title__gt=chap.title).order_by('title').first()

    return render(request,
                  'blog/chap_detail.html',
                  {'chap': chap,
                  'next_chap': next_chap,
                  'pre_chap': pre_chap,})

def genre_list(request):
    genres = Genre.objects.all()
    return render(request,
                  'blog/genre_list.html',
                  {'genres': genres})

def genre_detail(request, slug):
    genre = get_object_or_404(Genre, slug=slug)
    post_list =  genre.posts.all()

    paginator = Paginator(post_list, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    if page is None:
        start_index = 0
        end_index = 7
    else:
        (start_index, end_index) = proper_pagination(posts, index=4)

    page_range = list(paginator.page_range)[start_index:end_index]
    context = {
        'genre': genre,
        'posts': posts,
        'page_range': page_range,
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

def like_post(request):
    # post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post = get_object_or_404(Post, id=request.POST.get('id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    context = {
        'post': post,
        'is_liked': is_liked,
        'total_likes': post.total_likes(),
    }
    if request.is_ajax():
        html = render_to_string('blog/like_section.html', context, request=request)
        return JsonResponse({'form': html})

def autocomplete(request):
    if request.is_ajax():
        queryset = Post.published.filter(title__contains=request.GET.get('search', None))
        list = []        
        for i in queryset:
            list.append(i.title)
        data = {
            'list': list,
        }
        return JsonResponse(data)

def search_list(request):
    query = request.GET.get("q")
    post_list = Post.published.all()
    post_list = post_list.filter(Q(title__contains=query))
    paginator = Paginator(post_list, 4) 
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    if page is None:
        start_index = 0
        end_index = 7
    else:
        (start_index, end_index) = proper_pagination(posts, index=4)

    page_range = list(paginator.page_range)[start_index:end_index]
    context = {
        'posts': posts,
        'page_range': page_range,
    }

    return render(request, 'blog/search_list.html', context)


def proper_pagination(posts, index):
    start_index = 0
    end_index = 7
    if posts.number > index:
        start_index = posts.number - index
        end_index = start_index + end_index
    return (start_index, end_index)

    