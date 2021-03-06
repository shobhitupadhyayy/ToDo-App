from django import forms
from django.forms import ModelForm

from Home.models import Tasks

class AddTaskForm(forms.ModelForm):

    task = forms.CharField(max_length = 250,
                            widget = forms.TextInput(
                                attrs = {
                                    'class' : 'form-control',
                                    'placeholder' : 'Enter Your Tasks', 
                                }
                            )
                        )

    class Meta:
        model = Tasks
        fields = '__all__'