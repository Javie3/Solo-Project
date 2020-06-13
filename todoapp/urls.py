from django.urls import path, include
from todolist import views

urlpatterns = [
    path('', include('todolist.urls')),
]
