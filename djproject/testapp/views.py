from django.shortcuts import render
from testapp.models import *

# Create your views here.
def index(request):
    return render(request,'testapp/index.html')

def hydjobs1(request):
    hydjobs_list=hydjobs.objects.all().order_by('date')
    my_dict={'hydjobs_list':hydjobs_list}
    return render(request,'testapp/hydjobs.html',context=my_dict)

def blorejobs1(request):
    blorejobs_list=blorejobs.objects.all().order_by('date')
    my_dict={'blorejobs_list':blorejobs_list}
    return render(request,'testapp/blorejobs.html',context=my_dict)

def chennaijobs1(request):
    chennaijobs_list=chennaijobs.objects.all().order_by('date')
    my_dict={'chennaijobs_list':chennaijobs_list}
    return render(request,'testapp/chennaijobs.html',context=my_dict)

def punejobs1(request):
    punejobs_list=punejobs.objects.all().order_by('date')
    my_dict={'punejobs_list':punejobs_list}
    return render(request,'testapp/punejobs.html',context=my_dict)
