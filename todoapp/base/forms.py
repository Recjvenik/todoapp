
from django.forms import ModelForm, SelectDateWidget, CheckboxInput
from django.contrib.auth.forms import UserCreationForm
from .models import Task, User
from django import forms


DEMO_CHOICES = (
    ("title", "name"),
    ("due_date", "complete by date"),
    ("created", "added on date")
)


class SortingForm(forms.Form):


    def __init__(self, *args, **kwargs):
        super(SortingForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'}) 
    

    sort_by = forms.ChoiceField(choices=DEMO_CHOICES)



class CustomUserCreationForm(UserCreationForm):


    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'}) 


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        


class TodoForm(ModelForm):


    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'}) 


    class Meta:
        model = Task
        fields = ['title', 'due_date', 'complete']
        labels = {
            'title' : 'Task Name',
            'due_date' : 'Deadline'
        }
        widgets = {
            'due_date' : SelectDateWidget,
            'complete' : CheckboxInput
        }

    
        

    
        