from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TestData(models.Model):
    title = models.CharField(max_length=255)

    
class Post(models.Model):
    # image
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=255)
    content =  models.TextField()
    # category
    # tag
    counted_views = models.IntegerField(default=1)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True) #2023-03-24 22:31:54.422427
    # class Meta:
    #     ordering = ['-created_date']
    # def __str__(self):
    #     return "{} - {}".format(self.title, self.id)

