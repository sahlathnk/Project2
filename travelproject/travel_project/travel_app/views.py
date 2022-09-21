
#from django.http import HttpResponse
from .models import Place
from .models import Team
from django.shortcuts import render

def demo(request):
    obj=Place.objects.all()
    obj1=Team.objects.all()

    return render(request,'index.html',{'result':obj,'result1':obj1})

#def add(request): #  x=int(request.GET['num1'])
   # y=int(request.GET['num2'])
    #res=x+y
    #return render(request,'add.html',{'result':res})