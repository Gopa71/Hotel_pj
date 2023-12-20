from django.shortcuts import render,redirect
from .models import Hotel
from .form import Motelupdate
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

def update(req,id):
    hotel=Hotel.objects.get(id=id)
    form=Motelupdate(req.POST or None,req.FILES,instance=hotel)
    if form.is_valid():
       form.save()
       return redirect('/')
    return render(req,'update.html',{'hotel':hotel,'form':form})
def registerhotel(req):
   if req.method=='POST':
        name=req.POST.get('name')
        photo=req.FILES['photo']
        rate=req.POST.get('rate')
        desc=req.POST.get('desc')

        hotel=Hotel(name=name,photo=photo,rate=rate,desc=desc)
        hotel.save()
        return redirect('/')

   return render(req,'regmotel.html')