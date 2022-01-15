from django.shortcuts import render
from .forms import TheUsersForm
from .models import TheUsers


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
        form_name = our_form.data['name'].replace(' ', '')
        form_surname = our_form.data['surname'].replace(' ', '')
        result = TheUsers.objects.filter(name=str(form_name).capitalize(), surname=str(form_surname).capitalize())
        user_dict = {'name': form_name, 'surname': form_surname}

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
