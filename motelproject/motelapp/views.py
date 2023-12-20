from django.shortcuts import render,redirect
from .models import Hotel
# Create your views here.
def home(req):
    return render(req,'index.html')

def singapor(req):
    data=Hotel.objects.all
    return render(req,'singapor.html',{'data':data})

def details(req,id):
    data=Hotel.objects.get(id=id)
    return render(req,'detail.html',{'data':data})

def delete(req,id):
    if req.method=='POST':
        data=Hotel.objects.get(id=id)
        data.delete()

        return redirect('/')
    
    return render(req,'delete.html')