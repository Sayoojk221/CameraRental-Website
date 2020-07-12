from django.db import models
from django.utils import timezone

class admin(models.Model):
    username = models.CharField(max_length=30,default='')
    password = models.CharField(default='',max_length=30)

class userregister(models.Model):
    profileimage = models.ImageField(upload_to='user',default='')
    username = models.CharField(max_length=200,default='')
    email = models.CharField(max_length=200,default='')
    password = models.CharField(max_length=200,default='')
    city = models.CharField(max_length=200,default='')
    state = models.CharField(max_length=200,default='')
    pincode = models.CharField(max_length=200,default='')
    number = models.CharField(max_length=200,default='')
    status = models.CharField(max_length=200,default='')

    def __str__(self):
        return self.username

class photographer(models.Model):
    name = models.CharField(max_length=200,default='')
    email = models.CharField(max_length=200,default='')
    password = models.CharField(max_length=200,default='')
    place = models.CharField(max_length=200,default='')
    contactnumber = models.CharField(max_length=200,default='')
    created_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=200,default='')


class camera(models.Model):
    cameraimage = models.ImageField(upload_to='camera',default='')
    name = models.CharField(max_length=200,default='')
    price = models.CharField(max_length=200,default='')
    quantity = models.CharField(max_length=200,default='')
    def __str__(self):
        return self.name

class booking(models.Model):
    cameraId = models.ForeignKey(camera,on_delete=models.CASCADE)
    userid = models.ForeignKey(userregister,on_delete=models.CASCADE)
    address = models.CharField(max_length=200,default='')
    quantity = models.CharField(max_length=200,default='')
    price = models.CharField(max_length=200,default='')
    date = models.DateTimeField(default=timezone.now)

class photographerboooking(models.Model):
    photographerid = models.ForeignKey(photographer,on_delete=models.CASCADE)
    userid = models.ForeignKey(userregister,on_delete=models.CASCADE)
    date = models.CharField(max_length=200,default='')
    status = models.CharField(max_length=200,default='')


