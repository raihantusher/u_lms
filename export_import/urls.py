from django.urls import path
from . import views

app_name = "backup"
urlpatterns = [
    path("import/list/<int:list_id>", views.import_csv, name='import_csv'),
    path("export/list/<int:list_id>", views.export_csv, name='export_csv'),
]