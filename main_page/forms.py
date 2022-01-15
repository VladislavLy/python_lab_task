from django.forms import ModelForm, TextInput
from .models import TheUsers


class TheUsersForm(ModelForm):

    class Meta:
        model = TheUsers
        fields = ['name', 'surname']
        widgets = {
            'name': TextInput(attrs={
                'type': 'text',
                'placeholder': 'Name',
                'size': '25',
                'style': 'margin-bottom: 5px; padding: 7px 7px; border-radius: 5px'}
                ),
            'surname': TextInput(attrs={
                'type': 'text',
                'placeholder': 'Surname',
                'size': '25',
                'style': 'margin-bottom: 5px; padding: 7px 7px; border-radius: 5px'}
                ),
        }
