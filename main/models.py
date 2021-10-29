from django.db import models
from django.urls import reverse

from ckeditor.fields import RichTextField



class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    def __str__(self):
        return str(self.name)


class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return str(self.name)



class Article(models.Model):
    name = models.CharField(max_length=255)
    preview = models.ImageField(upload_to='previews/')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    short_description = models.TextField()
    body = RichTextField()
    date = models.DateField(auto_now_add=True)
    looks = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)

    def get_absolute_url(self):

        return f'/articles/{self.subcategory.category.slug}/{self.subcategory.slug}/{self.pk}/'


    def increase_like(self):
        self.likes += 1
        self.save()

    def increase_look(self):
        self.looks += 1
        self.save()


    def __str__(self):
        return str(self.name)