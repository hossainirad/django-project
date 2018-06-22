from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return redirect('articles:article_list')