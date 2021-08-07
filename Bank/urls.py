from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('viewcust',views.viewcust,name='viewcust'),
    path('transact',views.transact,name='transact'),
    path('viewtransact',views.viewtransact,name='viewtransact'),
]
