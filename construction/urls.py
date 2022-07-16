
from django.contrib import admin
from django.urls import path
from .views import index,contactUsConstruction,contactUsEvents,services,blog,aboutUs,contactConstruction,contactEvents
urlpatterns = [
    path('',index),
    path('mountainconstruction',contactUsConstruction),
    path('mountainevents',contactUsEvents),
    path('mountainservices',services),
    path('mountainblogs',blog),
    path('mountainaboutus',aboutUs),
    path('contactConstruction',contactConstruction),
path('contactEvent',contactEvents)
]
