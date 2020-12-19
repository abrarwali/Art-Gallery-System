from django import forms
from django.contrib.auth.models import User
from .models import Artist, Painting , Customer , Exhibition ,ArtistAddress


class NewPaintingForm(forms.ModelForm):
    class Meta:
        model = Painting
        exclude = ('Slug','Painting_ID', )


class NewArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        exclude = ('Slug','Artist_ID', )


class NewCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ('Slug','Customer_ID', )

class NewExhibitionForm(forms.ModelForm):
    class Meta:
        model = Exhibition
        exclude = ('Slug','Exhibition_ID', )

class NewArtistAddressForm(forms.ModelForm):
    class Meta:
        model = ArtistAddress
        exclude=('Slug',)
