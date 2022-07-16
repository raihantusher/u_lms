from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('',  views.home, name="l_home"),

    path('cat/', views.list_category, name="list_cat"),
    path('cat/add/',  views.add_category, name="add_cat"),
    path('cat/edit/<int:id>/',  views.edit_category, name="edit_cat"),
    path('cat/<int:id>/delete/',  views.del_category, name="delete_cat"),

    path('book/', views.list_book, name="list_book"),
    path('book/add/', views.add_book, name="add_book"),
    path('book/edit/<int:id>/', views.edit_book, name="edit_book"),
    path('book/<int:id>/delete/', views.del_book, name="delete_book"),

    path('dept/', views.list_dept, name="list_dept" ),
    path('dept/add/', views.add_dept, name="add_dept"),
    path('dept/edit/<int:id>/', views.edit_dept, name="edit_dept"),
    path('dept/<int:id>/delete/', views.del_dept, name="delete_dept"),

    path('pending-requests/', views.issue_request, name="pending_requests"),
    path('issued-book/', views.issued_book, name="all_requests"),


]
