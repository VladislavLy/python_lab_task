from django.shortcuts import render
from .forms import TheUsersForm
from .models import TheUsers
import re


def home_page(request):
    return render(request, 'web_pages/wrapper.html', {'Title':'Home'})


def form_page(request):
    error = ''

    if request.method == 'GET':
        our_form = TheUsersForm()
        context = {
            'form': our_form,
            'error': error,
            'Title': 'Form',
        }

    elif request.method == 'POST':
        our_form = TheUsersForm(request.POST)
        
        user_name = str(re.sub("[^A-Za-z ]", "", our_form.data['name']).strip()).capitalize()
        user_surname = str(re.sub("[^A-Za-z ]", "", our_form.data['surname']).strip()).capitalize()
        result = TheUsers.objects.filter(name=user_name, surname=user_surname)
        user_dict = {'name': user_name, 'surname': user_surname}

        if our_form.is_valid() and not result:
            our_form.save()
            return render(request, 'web_pages/hello_page.html', {'Title': 'Hello', 'data': user_dict})
        elif result:
            return render(request, 'web_pages/hello_again_page.html', {'Title': 'Hello again', 'data': user_dict})
        else:
            error = "Form isn't valid!"
            context = {
            'form': our_form,
            'error': error,
            'Title': 'Form',
        }

    return render(request, 'web_pages/form_page.html', {'Title': 'Form', 'data': context})


def list_page(request):
    the_users_list = TheUsers.objects.all().order_by('-id')
    return render(request, 'web_pages/list_of_page.html', {'Title': 'List', 'list_of_objects': the_users_list,})
