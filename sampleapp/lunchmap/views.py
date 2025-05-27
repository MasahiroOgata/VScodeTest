# from django.shortcuts import render
from django.views import generic
from .models import Category, Shop

class IndexView(generic.ListView):
    model = Shop
