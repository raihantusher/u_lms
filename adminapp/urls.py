from django.urls import path
from . import views

app_name = "adminapp"
urlpatterns = [
    path('', views.Home, name="home"),

    path('template/add/', views.add_template, name="add_template"),
    path('template/edit/<int:id>/', views.edit_template, name="edit_template"),

    path('lists/', views.List.as_view(), name="all_list"),
    path('lists/edit/<int:id>/', views.edit_list, name="edit_list"),

    path('campaign-lists/', views.CList.as_view(), name="all_campaign"),
    path('campaign-lists/edit/<int:id>/', views.edit_campaign, name="edit_campaign"),
]