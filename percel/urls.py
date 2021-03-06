from django.urls import path, include
from . import views

app_name = 'percel'

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('django.contrib.auth.urls')),
    path('order/', views.order, name='order'),
    path('invoice/', views.invoice, name='invoice')
]