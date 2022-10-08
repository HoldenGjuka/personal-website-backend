import datetime

from django.db import models
from django.utils import timezone

class BlogPost(models.Model):
    def __str__(self):
        return self.title
    
    def pub_date_default():
        return timezone.now()

    def title_default():
        return "sample_title"
    
    def body_default():
        return ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod" +
                "tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim" + 
                "veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo" +
                "consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum" +
                "dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non" +
                "proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1) and self.pub_date <= timezone.now()

    pub_date = models.DateTimeField('date published', default=pub_date_default)
    title = models.CharField(max_length=200, default=title_default)
    body = models.CharField(max_length=1500, default=body_default)

class Image(models.Model):
    def __str__(self):
        return "image"
    
    img = models.ImageField('./../media/GitHub_Logo.png')