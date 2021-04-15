from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('submit_form', views.submit_form),
    path('result', views.result)
]
