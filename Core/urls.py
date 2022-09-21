from django.urls import path, include

from . import views


app_name = "Core"

urlpatterns = [
    # authentication
    path("metrics/", views.getMetricValues, name="getMetricValues"),
    path("module/", views.getModuleValues, name="getModuleValues"),

]
