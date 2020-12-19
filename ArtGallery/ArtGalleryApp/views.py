from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import (NewArtistForm,NewCustomerForm,NewExhibitionForm,NewPaintingForm, NewArtistAddressForm)
from django.contrib import messages
from .models import Artist  , Painting , Exhibition,Customer
# Create your views here.
class ArtistView (View):
    template_name = 'ArtistList.html'

    def get(self,request):
        return render(request,self.template_name, {'Artists':Artist.objects.all()})

class ArtistAddressView(View):
    template_name = 'Artist_Address.html'
    def get(self,request,Artist_ID):
        Artist_ID = Artist.objects.get(Artist_ID=Artist_ID)
        return render(request,self.template_name)
class PaintingsView (View):
    template_name = 'Paintings.html'
    def get(self,request):
        return render(request,self.template_name, {'Paintings':Painting.objects.all()})
class ExhibitionView(View):
    template_name = 'Exhibitions.html'
    def get(self,request):
        return render(request,self.template_name, {'Exhibitions':Exhibition.objects.all()})
class CustomerView(View):
    template_name= 'Customers.html'
    def get(self,request):
        return render(request,self.template_name, {'Customers':Customer.objects.all()})

class NewArtistView(View):
    template_name = 'AddArtist.html'
    form = NewArtistForm
    def get(self,request):
        return render(request,self.template_name,{'form':self.form})
    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Artist Added Successfully.')
        else:
            messages.error(request,'Invalid Credentials! Try Again')
            return render(request,self.template_name,{'form':form})
        return redirect('home')

class NewArtistAddressView(View):
    template_name = 'AddArtistAddress.html'
    form = NewArtistAddressForm
    def get(self,request):
        return render(request,self.template_name,{'form':self.form})
    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Address Added Successfully.')
        else:
            messages.error(request,'Invalid Credentials! Try Again')
            return render(request,self.template_name,{'form':form})
        return redirect('home')

class NewPaintingView(View):
    template_name = 'AddPainting.html'
    form = NewPaintingForm
    def get(self,request):
        return render(request,self.template_name,{'form':self.form})
    def post(self, request, *args, **kwargs):
        form = self.form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,f'Painting Added Successfully.')
        else:
            messages.error(request,'Invalid Credentials! Try Again')
            return render(request,self.template_name,{'form':form})
        return redirect('home')


class NewCustomerView(View):
    template_name = 'AddCustomer.html'
    form = NewCustomerForm
    def get(self,request):
        return render(request,self.template_name,{'form':self.form})
    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Customer Added Successfully.')
        else:
            messages.error(request,'Invalid Credentials! Try Again')
            return render(request,self.template_name,{'form':form})
        return redirect('home')


class  NewExhibitionView(View):
    template_name = 'AddExhibition.html'
    form = NewExhibitionForm
    def get(self,request):
        return render(request,self.template_name,{'form':self.form})
    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Exhibition Created Successfully.')
        else:
            messages.error(request,'Invalid Credentials! Try Again')
            return render(request,self.template_name,{'form':form})
        return redirect('home')

