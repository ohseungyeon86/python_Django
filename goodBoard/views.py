from django.shortcuts import render
from django.http import HttpResponse
from .models import login,Boards
from .forms import loginForm,BoardsForm
# Create your views here.
def index(request):
    form = loginForm()
    return render(request, '../templates/goodBoards/login.html',{'form':form})
# Create your views here.
