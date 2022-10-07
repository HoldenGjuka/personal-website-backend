from django.http import HttpResponse

from home.models import BlogPost
import json

def index(request):
  index = 1
  blogpost_queryset = BlogPost.objects.all()
  output_dict = {
    "index": index,
    "title": blogpost_queryset[0].title[2:-2],
    "body": blogpost_queryset[0].body[2:-2]
  }
  json.dumps(output_dict)
  
  
  x = HttpResponse(json.dumps(output_dict))
  x.setdefault('Access-Control-Allow-Origin', "http://localhost:3000")
  return x
# json.parse on js side
# json.dumps on python side
# encode and decode as base 64 for more complex stuff