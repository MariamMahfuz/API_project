from django.urls import path
from . import views

urlpatterns = [
   path('form_home/', views.home, name='home'),
   path('edit/<int:primaryk>/',views.edit,name='edit'),
   path('delete/<int:pk>/',views.delete,name='delete')
]