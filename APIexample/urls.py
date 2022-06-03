from django.urls import path
from . import views

urlpatterns = [
   path('API',views.index,name='index')
]