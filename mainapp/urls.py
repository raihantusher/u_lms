from django.urls import path
from . import views

urlpatterns = [

    path('send-blast/', views.send_blast),
]
