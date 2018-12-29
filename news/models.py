from django.db import models
from datetime import datetime
from editors.models import Editors

# Create your models here.
class NewsDetails(models.Model):
    title = models.CharField(max_length=200)
    editor = models.ForeignKey(Editors, on_delete=models.DO_NOTHING)
    description = models.TextField()
    file_1 = models.FileField(upload_to='files/%Y/%m/%d', blank=True)
    file_2 = models.FileField(upload_to='files/%Y/%m/%d', blank=True)
    file_3 = models.FileField(upload_to='files/%Y/%m/%d', blank=True)
    file_4 = models.FileField(upload_to='files/%Y/%m/%d', blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    published_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
