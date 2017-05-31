#coding=utf-8
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'df_user/index.html')