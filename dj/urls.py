"""dj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from front import  views

urlpatterns = [
    path('',views.index,name='index'),
    path('dj_detail/<dj_id>',views.dj_detail,name='dj_detail'),
    path('dj_detail_two/<city_list>',views.dj_detail_two,name='dj_detail_two'),
    path('dj_view/<city>',views.dj_view,name='dj_view'),
    path('dj_view_one/<city>',views.dj_view_one,name='dj_view_one'),
    path('dj_view_two/<city>',views.dj_view_two,name='dj_view_two'),
    path('dj_view_three/<city>',views.dj_view_three,name='dj_view_three'),
    path('dj_view_four/<city>',views.dj_view_four,name='dj_view_four'),
    path('dj_view_five/<city>',views.dj_view_five,name='dj_view_five'),
    path('dj_kind/<city>',views.dj_kinds,name='dj_kinds'),
    path('dj_good/<city>',views.dj_food,name='dj_good'),
    path('dj_history/<city>',views.dj_history,name='dj_history'),
    path('dj_background',views.background,name='dj_background'),
    path('dj_famous/<city>',views.dj_famous,name='dj_famous'),
    path('dj_person/<city>',views.dj_person,name='dj_person'),
    path('dj_goods/<city>',views.dj_goods,name='dj_goods'),
    path('dj_add/',views.dj_add,name='dj_add'),
    path('dj_detailes/<dj_id>',views.dj_detailes,name='dj_detailes'),
    path('dj_change/',views.change_dj,name='change_dj'),
    path('update_dj/',views.update_dj,name='update_dj'),
    path('search_dj/',views.search_dj,name='search_dj'),
    path('dj_delete/',views.dj_delete,name='dj_delete'),
]
