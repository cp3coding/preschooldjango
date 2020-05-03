from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.index, name="index"),
    path('contact.html', views.contact, name="contact"),
    path('about.html', views.about, name="about"),
    path('pricing.html', views.pricing, name="pricing"),
    path('gallery.html', views.gallery, name="gallery"),
    path('packages.html', views.packages, name="packages"),



]
