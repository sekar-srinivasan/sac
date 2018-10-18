from django.contrib import admin
from .models import Donor, Donation

# Register your models here.
admin.site.register(Donor)
admin.site.register(Donation)
