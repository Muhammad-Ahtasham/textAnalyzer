from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.
class vlogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, default= "")
    head0 = models.CharField(max_length=500, default= "")
    chead0 = models.CharField(max_length=500, default= "")
    head1 = models.CharField(max_length=500, default= "")
    chead1 = models.CharField(max_length=500, default= "")
    head2 = models.CharField(max_length=500, default= "")
    chead2 = models.CharField(max_length=500, default= "")
    pub_Date = models.DateField()
    thumbnail_pic = models.ImageField(upload_to = 'blog/images', default= "")


    def __str__(self):
        return self.title

class blog(models.Model):
    pass