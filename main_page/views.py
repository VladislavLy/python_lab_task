from turtle import title
from django.shortcuts import render


def home_page(request):
    return render(request, 'web_pages/wrapper.html', {'Title':'Home'})


def form_page(request):
    return render(request, 'web_pages/form_page.html', {'Title':'Form'})


def list_of_page(request):
    return render(request, 'web_pages/list_of_page.html', {'Title':'List'})
