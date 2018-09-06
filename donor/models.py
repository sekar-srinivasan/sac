from django.db import models
from django.urls import reverse
from django.conf import settings
from django.db.models import Q

# Create your models here.

class DonorQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup =     (Q(first_name__icontains=query) |
                             Q(last_name__icontains=query)
                            )
            qs = qs.filter(or_lookup).distinct()
        return qs

class DonorManager(models.Manager):
    def get_queryset(self):
        return DonorQuerySet(self.model, using=self._db)
    def search(self, query=None):
        return self.get_queryset().search(query=query)

# class DonorManager(models.Manager):
#     def search(self, query=None):
#         qs = self.get_queryset()
#         if query is not None:
#             or_lookup =     (Q(first_name__icontains=query) |
#                              Q(last_name__icontains=query)
#                             )
#         qs = qs.filter(or_lookup).distinct()
#         return qs



User = settings.AUTH_USER_MODEL
class Donor(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(blank=True, max_length=20)
    email = models.EmailField(blank=True)
    addr_street = models.CharField(blank=True, max_length=250)
    addr_apt = models.CharField(blank=True, max_length=10)
    addr_city = models.CharField(blank=True, max_length=50)
    addr_state = models.CharField(blank=True, max_length=100)
    addr_zip = models.CharField(blank=True, max_length=6)
    active = models.BooleanField(default=True)

    objects = DonorManager()

    def get_absolute_url(self):
        return reverse('donor:donor-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.first_name + ' ' + self.last_name


#
# class Donation(models.Model):
#     donor = models.ForeignKey(Donor, on_delete=models.PROTECT)
#     child = models.ForeignKey(Child, on_delete=models.PROTECT)
#     amount = models.FloatField()
#
#     def __str__(self):
#         return 'Donor: ' + self.donor + 'Child: ' + self.child + 'Donation: ' + self.amount
