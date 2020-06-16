from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User 
from django.urls import reverse

class PublishedManager(models.Manager): 
    def get_queryset(self): 
        return super(PublishedManager, self).get_queryset().filter(status='published')

STATUS_CHOICES = ( 
        ('draft', 'Draft'), 
        ('published', 'Published'), 
    )

class Post(models.Model): 
    title = models.CharField(max_length=250) 
    slug = models.SlugField(max_length=250, unique=True)
    user = models.ForeignKey(User, 
                               on_delete=models.CASCADE)
    body = models.TextField()
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    publish = models.DateTimeField(default=timezone.now) 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    status = models.CharField(max_length=10,  
                              choices=STATUS_CHOICES, 
                              default='draft') 
    
    objects = models.Manager() # The default manager. 
    published = PublishedManager() # Our custom manager.
    image_cover = models.ImageField(upload_to="cover_img", default="images/None/no-img.jpg", blank=True) 

    class Meta: 
        ordering = ('-publish',) 

    def __str__(self): 
        return self.title
    
    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('blog:post-detail',
                       args=[self.slug])

class Genre(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    posts = models.ManyToManyField(Post)
    class Meta: 
        ordering = ('name',) 
        verbose_name_plural = "genres"

    def __str__(self): 
        return self.name
    
    def get_absolute_url(self):
        return reverse('blog:genre-detail',
                       args=[self.slug])

class Chap(models.Model):
    post = models.ForeignKey(
        Post, related_name='chaps',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=250) 
    slug = models.SlugField(max_length=250, unique=True, default="")
    user = models.ForeignKey(User, 
                               on_delete=models.CASCADE)
    publish = models.DateTimeField(default=timezone.now) 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    status = models.CharField(max_length=10,  
                              choices=STATUS_CHOICES, 
                              default='draft') 
    
    objects = models.Manager() # The default manager. 
    published = PublishedManager() # Our custom manager.

    class Meta: 
        ordering = ('-title',)

    def __str__(self): 
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:chap-detail',
                       args=[self.post.slug, self.slug])

class ChapImage(models.Model):
    chap = models.ForeignKey(Chap, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="comics/headers/", default="")

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.ForeignKey('Comment', null=True, related_name="replies", on_delete=models.CASCADE)
    content = models.TextField(max_length=160)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.post.title, str(self.user.username))

