from django.urls import path,include
from .import views

app_name='motel'
urlpatterns = [
    path('',views.home,name='home'),
    path('sigapor/',views.singapor,name='singapor'),
    path('details/<int:id>',views.details,name='details'),
    path('delete/<int:id>',views.delete,name='delete'),
    
]
