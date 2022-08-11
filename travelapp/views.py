

from django.http import HttpResponse
from django.shortcuts import render
from .models import place, news


# Create your views here.



def fun(request):
    obj=place.objects.all()
    obj2 = news.objects.all()
    return render(request,'index.html',{"results":obj,"values":obj2})
    # return render(request,'home.html',{'name':'addition'})
def fun2(request):
    obj2=news.objects.all()
    return render(request,'index.html',{"values":obj2})


def addition(request):
    num1=int(request.POST['num1'])
    num2=int(request.POST['num2'])
    sum=num1+num2
    return render(request,"result.html",{"add":sum})