from django.http import HttpResponse
from django.shortcuts import render, redirect


def home(request):
    # data={'salute':'welcome again',
    # 'list':["yashvant","gupta","sahu"],
    # 'name':['yashvant','aman','shivam'],
    # 'number':[10,20,30]
    # }
    return render(request, "index.html")


def admin_login(request):
    return render(request, "loginportal.html")


def yash(request):
    return HttpResponse("hii yashvant gupta")


def course(request, values):
    return HttpResponse(values)


# get and post method
def form(request):
    c = 0
    try:
        # a=int(request.GET["val1"])
        # b=int(request.GET["val2"])
        a = int(request.POST.get("val1"))
        b = int(request.POST.get("val2"))
        c = a+b
    except:
        pass
    return render(request, "html.html", {'output': c})


def submit(request):
    c = 0
    data = {}
    try:
        # a=int(request.GET["val1"])
        # b=int(request.GET["val2"])
        a = int(request.POST.get("val1"))
        b = int(request.POST.get("val2"))
        c = a+b
        data = {'n1': a, 'n2': b, 'output': c
                }
    except:
        pass
    return redirect(request, "html.html", data)
