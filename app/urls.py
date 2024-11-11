from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('index_html/', views.index_html, name='index_html'),
    path('Investor/', views.Investorform, name='Investorform'),
    path('first/', views.first, name='first'),
]