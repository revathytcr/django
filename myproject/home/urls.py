
from django.urls import path,include
from . import views
urlpatterns = [
   
    path('',views.index),
    path('about',views.about),
    path('contact',views.contact),
    path('rest',views.index1),
    path('restmodel',views.index2),
    path('restmodels/<id>',views.update)
   
]