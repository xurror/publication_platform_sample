from django.db import models
from datetime import datetime
# Create your models here.

class Contact(models.Model):
    news_details = models.CharField(max_length=200)
    news_details_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank = True)
    
    def __str_(self):
        return self.name
    