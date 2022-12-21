# applications forms.py
from django import forms
from .models import login
from .models import Boards

class BoardsForm(forms.ModelForm):
    class Meta:
        model=Boards
        fields = ['title', 'content']

class loginForm(forms.ModelForm):
    class Meta:
        model=login
        fields = ['id', 'password']