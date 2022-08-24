from importlib.resources import path
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('delete_item/<int:pk>',views.delete,name='delete'),
    path('update_item/<int:pk>',views.update,name='update')
]
