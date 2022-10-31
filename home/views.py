from django.http import HttpResponse

from home.models import BlogPost
import json
import PIL
import base64

from io import BytesIO

origin_url = "127.0.0.1"

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
  response.setdefault('Access-Control-Allow-Origin', origin_url)
  return response


def github_logo(request):
  img = PIL.Image.open('media/images/GitHub_Logo.png', mode='r')
  buffered = BytesIO()
  img.save(buffered, format="PNG")
  img_str = base64.b64encode(buffered.getvalue())
  response = HttpResponse(img_str)
  response.setdefault('Access-Control-Allow-Origin', origin_url)
  return response


def resume(request):
  pdf = open('media/documents/HOLDEN_GJUKA_CS_Resume_August.pdf', mode='r')
  buffered = BytesIO()
  pdf.save(buffered, format="PDF")
  pdf_str = base64.b64encode(buffered.getvalue())
  response = HttpResponse(pdf_str)
  response.setdefault('Access-Control-Allow-Origin', origin_url)
  return response
