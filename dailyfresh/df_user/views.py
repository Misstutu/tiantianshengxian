#coding=utf-8
from django.shortcuts import render,redirect
from models import FreshInfo
from models import *
from hashlib import sha1
from django.http import JsonResponse,HttpResponseRedirect
from . import user_decorator
from django.core.paginator import Paginator,Page

def register(request):
    return render(request, 'df_user/register.html')

def post1(request):
    re = request.POST
    name=re.get('user_name')
    password=re.get('pwd')
    mailbox=re.get('email')

    data=FreshInfo.objects.create(fname=name,fpwd=password,femail=mailbox)
    data.save()
    return redirect('/')

def login(request):
    return render(request, 'df_user/login.html')

def logout(request):
    request.session.flush()
    return redirect('/')

def cart(request):
    return render(request, 'df_user/cart.html')

def detail(request):
    return render(request,'df_user/detail.html')

def list(request):
    return render(request,'df_user/list.html')

def denglu(request):
    re = request.POST
    name = re.get('username')
    password = re.get('pwd')

    dl=FreshInfo.objects.filter(fname=name)
    if dl[0].fpwd == password:
        request.session['user_name'] = name
        request.session['user_id'] = dl[0].id
        return redirect('/')
    else:
        return render(request,'df_user/register.html')

@user_decorator.login
def user_center_info(request):
        user_email = FreshInfo.objects.get(id=request.session['user_id']).femail
        # 最近浏览
        goods_list = []
        goods_ids = request.COOKIES.get('goods_ids', '')
        if goods_ids != '':
            goods_ids1 = goods_ids.split(',')  # ['']
            # GoodsInfo.objects.filter(id__in=goods_ids1)
            for goods_id in goods_ids1:
                goods_list.append(GoodsInfo.objects.get(id=int(goods_id)))

        context = {'title': '用户中心',
                   'user_email': user_email,
                   'user_name': request.session['user_name'],
                   'page_name': 1,
                   'goods_list': goods_list}
        return render(request, 'df_user/user_center_info.html', context)

def place_order(request):
    return render(request,'df_user/place_order.html')

@user_decorator.login
def user_center_order(request):
    return render(request, 'df_user/user_center_order.html')

@user_decorator.login
def user_center_site(request):
    data = FreshInfo.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        re = request.POST
        data.frecipients = re.get('newname')
        data.faddress = re.get('app', 0)
        data.fpostcode = re.get('postcode')
        data.fphone = re.get('phone')
        data.save()
        print data.faddress
    context = {'title': '用户中心', 'address': data.faddress, 'user':data.frecipients,
               'phone':data.fphone,
               'page_name': 1}
    return render(request, 'df_user/user_center_site.html', context)
































