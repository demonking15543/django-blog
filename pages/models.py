from django.db import models
from django.utils.translation import gettext as _
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class DateTime(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    

    class Meta:
        abstract = True

        

STATUS = (
    ("Draft","Draft"),
    ("Publish","Publish")
)

class Post(DateTime):
    author=models.ForeignKey(User, related_name="author", on_delete=models.CASCADE)    
    title=models.CharField(max_length=150)
    slug = models.SlugField(max_length=300, verbose_name=_('Post Slug'))
    description=models.TextField(_("Describe your post here..."), max_length=3000)
    status=models.CharField(max_length=7,choices=STATUS, default='Draft')
    likes = models.ManyToManyField(User, related_name='post_like')

    

    

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering=['-created_at']

    def __str__(self):
        return self.title
    
    # Slugify title into slug and save to slug field
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
        

    
    def get_absolute_url(self):
        return reverse("pages:post_detail", kwargs={"pk": self.pk, "slug":self.slug})
        
    def number_of_likes(self):
        return self.likes.count()








class Comment(DateTime):
    post = models.ForeignKey(Post, related_name="post_comment", on_delete=models.CASCADE)  
    email=models.EmailField(max_length=255)
    name=models.CharField(max_length=150)
    content=models.TextField(_("Please Post Your Comment here..."), max_length=150)

    active = models.BooleanField(default=False)


    

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering=['-created_at']

    def __str__(self):
        return self.name
    

    
        


