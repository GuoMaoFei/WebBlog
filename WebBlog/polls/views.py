# encoding: utf-8
from django.shortcuts import render
from .models import Postinfo
# Create your views here.
#主页面
def index(request):
    list=postinfo.objects.order_by('-pubdate')[:5]
    context={'list':list}
    return render(request,'polls/blog_index.html',context)