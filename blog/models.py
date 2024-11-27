from django.db import models
from django.utils import timezone



class Category(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name
    

class News(models.Model):
    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published" 

    title = models.CharField(max_length = 255)
    slug = models.SlugField(max_length = 255)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add = True)
    publish_time = models.DateTimeField(default = timezone.now)
    update_time = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length = 2, choices=Status.choices)


    def __str__ (self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length = 150)
    email = models.EmailField(max_length = 150)
    message = models.TextField()

    def __str__(self):
        return self.email

