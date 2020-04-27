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
    slug = models.SlugField(max_length=250,  
                            unique_for_date='publish') 
    user = models.ForeignKey(User, 
                               on_delete=models.CASCADE,
                               related_name='blog_posts') 
    body = models.TextField() 
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

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.slug])

class Chapter(models.Model):
    post = models.ForeignKey(
        'Post', related_name='chapters',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=250) 
    slug = models.SlugField(max_length=250,  
                            unique_for_date='publish')
    user = models.ForeignKey(User, 
                               on_delete=models.CASCADE,
                               related_name='blog_chapters')
    publish = models.DateTimeField(default=timezone.now) 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    status = models.CharField(max_length=10,  
                              choices=STATUS_CHOICES, 
                              default='draft') 
    
    objects = models.Manager() # The default manager. 
    published = PublishedManager() # Our custom manager.

    class Meta: 
        ordering = ('-publish',)
        index_together = (('id', 'slug'),)
 

    def __str__(self): 
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:chapter_detail',
                       args=[self.id, self.slug])

class ChapterImage(models.Model):
    chapter = models.ForeignKey('Chapter', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="comics/headers/")
