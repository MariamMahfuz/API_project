from django.db import models

# Create your models here.

class Profile(models.Model):
    writer_name=models.CharField(max_length=30)
    writer_photo=models.ImageField(upload_to='writer-name',null=False,blank=False)
    

    def __str__(self):
        return str(self.writer_name)

class Booklist(models.Model):
    book_title=models.CharField(max_length=70)
    writer=models.ForeignKey(Profile,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.book_title)
