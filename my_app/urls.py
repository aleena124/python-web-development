# 1) copy codes from first_project > urls.py

#from django.contrib import admin
from django.urls import path
from . import views  #import views for urls to recognise

urlpatterns = [
    
    #path('',views.index), #our function
    #path('response/',views.home)
    path('',views.createbook),
    path('listview/',views.listbook),
    path('detailsview/<int:book_id>/',views.detailsview),
    path('updateview/<int:book_id>/',views.updateview)
]
