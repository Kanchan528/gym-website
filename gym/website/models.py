from django.db import models
from datetime import datetime, date

# Create your models here.

class BannerImage(models.Model):
    image = models.ImageField(null=True, blank= True)
    heading = models.CharField(max_length =100, null=True, blank= True)
    description = models.TextField(default='describe here')

    def __str__(self):
        return self.heading


class Introduction(models.Model):
    image = models.ImageField(null=True, blank=True)
    video = models.CharField(max_length=200 , null=True, blank=True)

   
class Program(models.Model):
    icon_name = models.CharField(max_length=100, null=True, blank=True)
    heading = models.CharField(max_length=100, null=True, blank= True)
    description = models.TextField(default=' describe here')

    def __str__(self):
        return self.heading


class CounterImage(models.Model):
    image = models.ImageField(null=True, blank=True)


class Counter(models.Model):
    happy_customer = models.IntegerField()    
    perfect_bodies = models.IntegerField()
    working_hours = models.IntegerField()
    success_stories = models.IntegerField()


class TestimonyImage(models.Model):
    image = models.ImageField(null=True, blank=True)


class Testimony(models.Model):
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(default='describe here')
    position = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Packages(models.Model):
    duration= models.CharField(max_length=100, null=True, blank= True)
    class_heading = models.CharField(max_length=100, null=True, blank=True)
    class_details = models.TextField(default='describe here')
    price = models.IntegerField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.class_heading


class BlogSingle(models.Model):
    heading = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    details = models.TextField(default=' describe here')
    date = models.DateField(default=datetime.now, blank = True)
    posted_by = models.CharField(max_length=100, null=True, blank=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.heading


class Comment(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(default=datetime.now, blank =True)
    email = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(default= 'describe here')
    blog = models.ForeignKey( BlogSingle, on_delete=models.CASCADE, related_name='post_comment', null =True, blank=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    F_name = models.CharField(max_length=100, null=True, blank=True)
    L_name = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(default=datetime.now, blank =True)
    time = models.TimeField(default= datetime.now, blank =True)
    phone_no = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(default='describe here')

    def __str__(self):
        return self.F_name


class Gallery(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null= True, blank=True)


class Coaches(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(default='describe here')
    twitter_link = models.CharField(max_length=200, null=True, blank=True)
    facebook_link = models.CharField(max_length=200, null=True, blank=True)
    instagram_link = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.name


class ClassType(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Classes(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    types = models.ForeignKey(ClassType, on_delete=models.CASCADE, related_name='class_type', null=True, blank=True)
    coach = models.ForeignKey(Coaches, on_delete=models.CASCADE, related_name='coach', null=True, blank=True) 

    def __str__(self):
        return self.name


class Schedule(models.Model):
    image =models.ImageField(null=True, blank= True)


class Contact(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(default='describe here')

    def __str__(self):
        return self.name


class Process(models.Model):
    icon_name = models.CharField(max_length=100, null=True, blank=True)
    heading = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(default='describe here')

    def __str__(self):
        return self.heading

