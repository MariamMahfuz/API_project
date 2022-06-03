from django.urls import path
from . import views

urlpatterns = [
    path('',views.Writer_list,name='writer_list'),
    path('Profile/<int:primarykey>',views.Writer_Profile,name='profile'),
    path('add_writer',views.Add_writer,name='add_writer'),
    path('Edit_Profile/<int:primarykey>',views.Edit_Profile,name='edit_profile'),
    path('delete/<int:primarykey>',views.Delete_profile,name='delete_profile')
]