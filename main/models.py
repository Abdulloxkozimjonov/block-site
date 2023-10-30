from django.db import models
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Baner(models.Model):
    img=models.ImageField(upload_to="baner_photos/",null=True, blank=True)
    title=models.CharField(max_length=25)
    description=models.CharField(max_length=100)

    def __str__(self):
        return self.title


class About(models.Model):
    name=models.CharField(max_length=19,null=True, blank=True)
    title=models.CharField(max_length=25)
    text=models.TextField()
    description=models.CharField(max_length=15, null=True, blank=True)
    date= models.IntegerField()
    facebook= models.CharField(max_length=25)
    google= models.CharField(max_length=25)
    twitter= models.CharField(max_length=25)
    dribbble= models.CharField(max_length=25)
    github= models.CharField(max_length=25)

    def __str__(self):
        return self.title


class Courses(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Price(models.Model):
    title=models.CharField(max_length=20)
    price=models.IntegerField(default=0)
    name=models.CharField(max_length=10)
    javobgar=models.CharField(max_length=40)
    fani=models.CharField(max_length=30)
    flex=models.CharField(max_length=55)
    mobil_ilova=models.CharField(max_length=35)
    natija=models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Video(models.Model):
    category=models.ForeignKey(to=Category,on_delete=models.CASCADE)
    text=models.CharField(max_length=150)
    img=models.ImageField(upload_to="video/")

    def __str__(self):
        return self.text


class Contact(models.Model):
    title=models.CharField(max_length=30)
    description=models.CharField(max_length=200)
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=40)
    phone_number=models.IntegerField()
    subject=models.CharField(max_length=155)
    message=models.TextField()

    def __str__(self):
        self.title


class Info(models.Model):
    name=models.CharField(max_length=15)
    adress=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone_number=models.IntegerField()
    icon=models.CharField(max_length=30)

    def __str__(self):
        return self.name


class User(AbstractUser):
    phone_number=models.CharField(max_length=13,null=True,blank=True)
    bio=models.CharField(max_length=155,null=True, blank=True)


    class Meta(AbstractUser.Meta):
        swappable= 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'