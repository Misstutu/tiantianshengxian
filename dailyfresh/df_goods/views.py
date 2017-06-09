#coding=utf-8
from django.shortcuts import render
from django.http import JsonResponse
from models import *
from django.core.paginator import Paginator
from df_cart.models import CartInfo
# Create your views here.
def index(request):
    click_list=GoodsInfo.objects.filter(gtype_id=1).order_by('-gclick')[0:3]
    list = GoodsInfo.objects.filter(gtype_id=1).order_by('-id')[0:4]

    context={'title':'首页',
             'click_list':click_list,
             'new_list':list,
             }
    return render(request, 'df_goods/index.html',context)

def list(request,tid,pindex,orderby):
    gtype=TypeInfo.objects.get(id=int(tid))

    # 查询两条最新的数据
    new_list = gtype.goodsinfo_set.order_by('-id')[0:2]
    # 查询指定分类tid的商品
    goods_list = GoodsInfo.objects.filter(gtype_id=int(tid))
    # 根据指定规则排序
    if orderby == '1':
        goods_list = goods_list.order_by('-id')
    elif orderby == '2':
        goods_list = goods_list.order_by('-gprice')
    elif orderby == '3':
        goods_list = goods_list.order_by('-gclick')
    # 进行分页
    paginator = Paginator(goods_list, 10)
    pindex2 = int(pindex)
    if pindex2 <= 0:
        pindex2 = 1
    elif pindex2 > paginator.num_pages:
        pindex2 = paginator.num_pages
    page = paginator.page(pindex2)
    context={'title':'列表页','page':page,
             'tid':tid,'gtype':gtype,'orderby':orderby,
             'new_list':new_list}
    return render(request, 'df_goods/list.html',context)

def detail(request,gid):
    goods=GoodsInfo.objects.get(pk=gid)
    goods.click=goods.gclick+1
    goods.save()
    new_list=goods.gtype.goodsinfo_set.order_by('id')[0:2]
    cart_count = CartInfo.objects.all().count()
    context={'title':'商品详细','goods':goods,'new_list':new_list,'cart_count':cart_count}
    return render(request, 'df_goods/detail.html',context)