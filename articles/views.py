from django.shortcuts import render, redirect
from .models import Articles
from django.contrib.auth.decorators import login_required
from . import forms
from .forms import *
from django.views.generic import CreateView


def article_list(request):
    # articles = Articles.objects.all().order_by('-id')[:3] # this returns last 3 rows
    articles = Articles.objects.all().order_by('date')
    print(articles)
    return render(request, 'article_list.html', {'articles': articles})


def article_detail(request, slug):
    article_4_models = Articles.objects.get(slug = slug)

    return render(request, 'article_detail.html', {'articles': article_4_models})


@login_required(login_url='accounts:login')
def create_article(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:article_list')
    else:
        form = forms.CreateArticle()
    return render(request, 'create.html', {'form': form})


class NewAtricle(CreateView):
    form_class = NewArticleForm
    template_name = 'create.html'
    success_url = '/articles/'