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

    category = models.ForeignKey(Category, related_name="books", on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

