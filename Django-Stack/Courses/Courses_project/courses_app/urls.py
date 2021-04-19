from django.urls import path

from . import views 
urlpatterns = [
    #localhost:8000
    path('', views.index),
    #localhost:8000
    path('course/', views.add_course),
    #localhost:8000/courses
    path('<int:course_id>/delete', views.delete),
]