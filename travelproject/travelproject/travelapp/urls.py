from .import views
from django.urls import path



urlpatterns = [
    path('',views.demo,name='demo'),
    #path('about/',views.about,name='about'),
    #path('name/',views.name,name='name'),
    #path('',views.opra,name='opra'),
    #path('add/',views.addition,name='addition'),

]
