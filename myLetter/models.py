from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True) #Unique Id
    username = models.CharField(max_length=50, null=True)
    user_age = models.IntegerField(null=True)
    user_mail = models.EmailField(max_length=254, null=True)
    partner_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        myUser = (self.username).replace(' ', '_')
        return myUser + "_" + str(self.id)

class Letter(models.Model):
    id = models.AutoField(primary_key=True)
    letter = models.TextField()
    user_img = models.ImageField(upload_to='image/', blank=True)
    audio = models.FileField(upload_to='audio/', blank=True)
    user = models.ForeignKey(User, null=True,  on_delete=models.SET_NULL, blank=True)
