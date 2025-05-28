from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,        
    )    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Shop(models.Model):
    name = models.CharField(max_length=255, verbose_name='店名')
    address = models.CharField(max_length=255, verbose_name='住所')
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        verbose_name='投稿者',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name='カテゴリ',
    )
    comment = models.TextField(max_length=1000, verbose_name='コメント')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('lunchmap:detail', kwargs={'pk':self.pk})

