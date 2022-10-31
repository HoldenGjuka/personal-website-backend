from django.contrib import admin

from .models import BlogPost, Image, Resume

admin.site.register(BlogPost)
admin.site.register(Image)
admin.site.register(Resume)