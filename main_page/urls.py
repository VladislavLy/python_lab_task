from django.urls import path

from . import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('form/', views.form_page, name='form_page'),
    path('list/', views.list_page, name='list_page'),
]
