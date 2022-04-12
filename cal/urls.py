from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('num/',views.num,name='num'),
    path('pnum/',views.pnum,name='pnum'),
    path('hcf/',views.hcf,name='hcf'),
]