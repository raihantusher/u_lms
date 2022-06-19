from django.urls import path
from . import views

app_name = "campaign"
urlpatterns = [
    path('run/<int:id>/', views.run, name="run_campaign"),
    path("tracker/<int:log_id>/", views.PixelView.as_view(), name="track")
]