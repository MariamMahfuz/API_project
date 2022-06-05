from django.forms import ModelForm
from .models import Booklist, Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Booklist
        fields = ['writer_name','writer_photo','book_title']