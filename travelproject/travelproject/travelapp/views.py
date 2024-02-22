from django.http import HttpResponse
from django.shortcuts import render
from . models import Place



# Create your views here.

def demo(request):
    obj=Place.objects.all()
    return render(request,"index.html",{'result':obj})

#def about(request):
    #return HttpResponse("Hello world")

#def name(request):
    #name="Athul"
    #return render(request,"index1.html",{'obj':name})

#def opra(request):
   #return render(request,"index3.html")

#def addition(request):
    #x=int(request.GET['num1'])
    #y=int(request.GET['num2'])
    #Result1=x+y
    #Result2=x-y
    #Result3=x*y
    #Result4=x//y

    #return render(request,"index4.html",{'res1':Result1,'res2':Result2,'res3':Result3,'res4':Result4})



