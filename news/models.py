from django.db import models

# Create your models here.
class Category(models.Model):
    nomi = models.CharField(max_length=250)

    def __str__(self):
        return self.nomi
    

class News(models.Model):
    nomi = models.CharField(max_length=250)
    rasmi = models.URLField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    short_text = models.CharField(max_length=500)
    text = models.TextField()
    sana = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nomi
    

# UYGA VAZIFA:
# kamida 5 ta kategoriya va har biri ichida kamida 5 tadan yangilik(news) qo'shiladi