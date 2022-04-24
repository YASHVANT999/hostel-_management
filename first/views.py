from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # data={'salute':'welcome again',
    # 'list':["yashvant","gupta","sahu"],
    # 'name':['yashvant','aman','shivam'],
    # 'number':[10,20,30]
    # }
    return render(request,"index.html")

def admin_login(request):
    return render(request,"loginportal.html")

def yash(request):
    return HttpResponse("hii yashvant gupta")

def course(request,values):
    return HttpResponse(values)