from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import View


class HelloWorld(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello World')
