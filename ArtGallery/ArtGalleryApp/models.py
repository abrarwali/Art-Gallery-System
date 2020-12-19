from django.db import models
# from django.contrib.auth.models import User
from time import time
from slugify import slugify
from django.urls import reverse
import random
# Create your models here.


class Artist(models.Model):
    Artist_ID = models.AutoField(primary_key=True)
    First_Name = models.CharField(max_length=15)
    Last_Name = models.CharField(max_length=20)
    Phone = models.CharField(max_length=12)
    Slug = models.SlugField(max_length=100, unique=True, blank=True)

    def __str__(self):
        _ = str(self.Artist_ID) + " - " + str(self.First_Name) + " " + str(self.Last_Name)
        return _

    def save(self, *args, **kwargs):  # SAVE
        if not self.Slug:
            print("Creating Slug for '{}'".format(self.First_Name))
            strtime = "".join(str(time()).split("."))
            string = "%s-%s" % (strtime[7:], self.First_Name)
            self.Slug = slugify(string)
        super(Artist, self).save()

    def get_absolute_url(self):
        return reverse('url-ArtistList', args=[self.Slug])


class ArtistAddress(models.Model):

    Artist_ID = models.OneToOneField(Artist, on_delete=models.CASCADE, related_name='artist_addresses')
    Home_Address = models.CharField(max_length=255)
    Office = models.CharField(max_length=255)
    Slug = models.SlugField(max_length=100, unique=True, blank=True)

    def __str__(self):
        _ = "{0} {1}".format(str(self.Artist_ID.First_Name), str(self.Artist_ID.Last_Name))
        return _

    def save(self, *args, **kwargs):  # SAVE
        if not self.Slug:
            print("Creating Slug for '{}'".format(self.Artist_ID))
            self.Slug = slugify(str(self.Artist_ID.First_Name)+str(self.Artist_ID.Last_Name))
        super(ArtistAddress, self).save()

    def get_absolute_url(self):
        return reverse('url-Artist_Address', args=[self.Slug])


class Customer(models.Model):
    Customer_ID = models.AutoField(primary_key=True)
    First_Name = models.CharField(max_length=15)
    Last_Name = models.CharField(max_length=20)
    Address = models.CharField(max_length=255, help_text='Billing Address')
    Phone = models.CharField(max_length=13)
    Slug = models.SlugField(max_length=100, unique=True, blank=True)

    def __str__(self):
        _ = str(self.Customer_ID) + " - " + str(self.First_Name) + " " + str(self.Last_Name)
        return _

    def save(self, *args, **kwargs):  # SAVE
        if not self.Slug:
            print("Creating Slug for '{}'".format(self.Customer_ID))
            x = int(str(time())[7:9])
            x =random.randint(1,x)*999
            string = str(self.First_Name)+str(self.Last_Name)+str(x)
            self.Slug = slugify(string)
        super(Customer, self).save()

    def get_absolute_url(self):
        return reverse('url-CustomerList', args=[self.Slug])


class Painting(models.Model):
    Painting_ID = models.AutoField(primary_key=True)
    Painting = models.ImageField(null=True, upload_to='paintings/')
    Painting_Name = models.CharField(max_length=59,default='Not Provided')
    Year = models.CharField(max_length=4)
    Artist_ID = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='painting_artist')
    Sold = models.BooleanField(default=False)
    Slug = models.SlugField(max_length=100, unique=True, blank=True)

    # likes = models.ManyToManyField(User,related_name='Painting_Likes');
    #
    # def no_of_likes(self):
    def __str__(self):
        _ = "({0}) {1} by {2}.".format(str(self.Painting_ID), self.Painting_Name, self.Artist_ID.First_Name)
        return _

    def save(self, *args, **kwargs):  # SAVE
        if not self.Slug:
            print("Creating Slug for '{}'".format(self.Painting_ID))
            strtime = "".join(str(time()).split("."))
            string = "%s-%s" % (strtime[7:], self.Painting_Name)
            self.Slug = slugify(string)
        super(Painting, self).save()

    def get_absolute_url(self):
        return reverse('url-PaintingList', args=[self.Slug])


class Exhibition(models.Model):
    Exhibition_ID = models.AutoField(primary_key=True, )
    Start_Date = models.DateTimeField()
    End_Date = models.DateTimeField()
    Exhibition_Name = models.CharField(max_length=100)
    Venue = models.CharField(max_length=255)
    Slug = models.SlugField(max_length=100, unique=True, blank=True)

    def __str__(self):
        _ = "(" + str(self.Exhibition_ID) + ") " + str(self.Exhibition_Name)
        return _

    def save(self, *args, **kwargs):  # SAVE
        if not self.Slug:
            print("Creating Slug for '{}'".format(self.Exhibition_ID))
            x = int(str(time())[7:9])
            x =random.randint(1,x)*999
            string = "{0}_{1}".format(self.Exhibition_Name, str(x))
            self.Slug = slugify(string)
        super(Exhibition, self).save()
    def get_absolute_url(self):
        return reverse('url-Exhibitions', args=[self.Slug])


class Buy(models.Model):
    Choice = (
        ('INR', ('Indian Rupee')),
        ('EUR', ('Euros')),
        ('USD', ('US Dollars')),
    )


    Painting_ID = models.ForeignKey(Painting, on_delete=models.CASCADE, related_name='painting_bought')
    Painting_Name = models.CharField(blank=True,max_length=59)
    Artist_ID = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='sold_painting_artist')
    Customer_ID = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='sold_to_customer')
    Price = models.IntegerField()
    Currency = models.CharField(max_length=20,choices = Choice,default='INR')
    Slug = models.SlugField(max_length=100, unique=True, blank=True)
    Sold_In = models.ForeignKey(Exhibition,on_delete=models.CASCADE,
                                default=0,related_name='sold_in_exhibition')


    def __str__(self):
        return "{0} by {1}".format(str(self.Painting_Name), str(self.Painting_ID))

    def save(self, *args, **kwargs):  # SAVE
        if not self.Painting_Name:
            self.Painting_Name = self.Painting_ID.Painting_Name

        if not self.Slug:
            print("Creating Slug for '{}'".format(self.Painting_ID))
            x = int(str(time())[7:9])
            x =random.randint(1,x)*999
            string = "{0}{1}".format(self.Painting_Name, str(x))
            self.Slug = slugify(string)
        super(Buy, self).save()

    def get_absolute_url(self):
        return reverse('url-Buy', args=[self.Slug])
