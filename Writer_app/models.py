from django.db import models

# Create your models here.
class Booklist(models.Model):
    book_title=models.CharField(max_length=70)
    def __str__(self):
        return str(self.book_title)
class Profile(models.Model):
    writer_name=models.CharField(max_length=30)
    writer_photo=models.ImageField(upload_to='writer-name',null=False,blank=False)
    book_list=models.ForeignKey(Booklist,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.writer_name)
