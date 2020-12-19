from django.contrib import admin
from .models import Artist , ArtistAddress, Buy , Customer , Exhibition , Painting
# Register your models here.
admin.site.register(Artist)
admin.site.register(ArtistAddress)
admin.site.register(Buy)
admin.site.register(Customer)
admin.site.register(Exhibition)
admin.site.register(Painting)
