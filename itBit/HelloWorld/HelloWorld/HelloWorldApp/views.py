from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def foo(request):
    html = "<html><body>Hello World!<body></html>"
    return HttpResponse(html)
