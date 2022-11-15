from django.contrib import admin

from .models import BlogPost, Image, PDF

admin.site.register(BlogPost)
admin.site.register(Image)
admin.site.register(PDF)