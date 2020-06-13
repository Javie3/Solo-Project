from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('delete/<int:id>', views.delete),
    path('cross_off/<int:id>', views.cross_off),
    path('uncross/<int:id>', views.uncross),
    path('edit/<int:id>', views.edit),
]
