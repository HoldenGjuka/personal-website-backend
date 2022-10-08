from django.http import HttpResponse

from home.models import BlogPost
import json


# sends all blog posts as json array
def index(request):
  blogpost_queryset = BlogPost.objects.all()
  blog_array = []
  
  for i in blogpost_queryset:
    count = 0
    blog = { 
      'title': i.title,
      'body': i.body
    }
    blog_array.append(blog)
    count = count + 1
  
  x = HttpResponse(json.dumps(blog_array))
  print(json.dumps(blog_array))
  x.setdefault('Access-Control-Allow-Origin', "http://localhost:3000")
  return x