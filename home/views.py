from django.http import HttpResponse

from home.models import BlogPost, Image
import json
import base64

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
  
  response = HttpResponse(json.dumps(blog_array))
  print(json.dumps(blog_array))
  response.setdefault('Access-Control-Allow-Origin', "http://localhost:3000")
  return response


def resume(request):
  images = Image.objects.all()
  image64 = base64.b64encode(images[0].img)
  response = HttpResponse(json.dumps("asdf"))
  response.setdefault('Access-Control-Allow-Origin', "http://localhost:3000")
  return response