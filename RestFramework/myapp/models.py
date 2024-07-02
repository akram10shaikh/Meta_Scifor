from django.db import models

# Create your models here.

class Category_Model(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.title

class Post_Model(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True)
    image = models.ImageField(upload_to='')
    category = models.ForeignKey(Category_Model,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.title