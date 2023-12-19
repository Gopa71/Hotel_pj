from django.shortcuts import render

# Create your views here.
def home(req):
    return render(req,'index.html')

def singapor(req):
    return render(req,'singapor.html')
    