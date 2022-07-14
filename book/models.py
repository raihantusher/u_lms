from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=155)
    page_number = models.CharField(max_length=155)
    pdf = models.FileField(null=True, blank=True)

    category = models.ForeignKey(Category, related_name="books", on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

