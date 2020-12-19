from django.urls import path , re_path
from .views import (ArtistView , PaintingsView, ExhibitionView,CustomerView, ArtistAddressView)
from .views import NewArtistView, NewPaintingView , NewCustomerView , NewExhibitionView, NewArtistAddressView
urlpatterns = [
    path(r'Artists/',ArtistView.as_view(),name ='url-ArtistList'),
    path(r'Artist_Address/',ArtistAddressView.as_view(),name ='url-Artist_Address'),
    path(r'Painting/',PaintingsView.as_view(),name ='url-PaintingList'),
    path(r'Customer/',CustomerView.as_view(),name ='url-CustomerList'),
    path(r'Buy/',ArtistView.as_view(),name ='url-Buy'),
    path(r'Exhibition/',ExhibitionView.as_view(),name ='url-Exhibitions'),
    path(r'createArtist/',NewArtistView.as_view(),name ='url-addArtist'),
    path(r'createArtistAddress/',NewArtistAddressView.as_view(),name ='url-addArtistAddress'),
    path(r'newPainting/',NewPaintingView.as_view(),name ='url-addPainting'),
    path(r'newCustomer/',NewCustomerView.as_view(),name ='url-addCustomer'),
    path(r'newExhibition/',NewExhibitionView.as_view(),name ='url-addExhibition'),
]
