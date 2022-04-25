from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="home"),
    path('index.html', views.index, name="index"),
    path('about.html', views.about, name="about"),
    path('blog.html', views.blog, name="blog"),
    path('contact.html', views.contact, name="contact"),
    path('pricing.html', views.pricing, name="pricing"),
    path('service.html', views.service, name="service"),
]


