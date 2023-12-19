from django.urls import path,include
from .import views

app_name='motel'
urlpatterns = [
    path('',views.home,name='home'),
    path('sigapor/',views.singapor,name='singapor')
]
