from django.db import models
from django.urls import reverse
from django.conf import settings
from django.db.models import Q
from PIL import Image
import os

# Create your models here.

class ProjectQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup =     (Q(name__icontains=query) |
                             Q(contact_first_name__icontains=query)|
                             Q(contact_last_name__icontains=query)
                            )
            qs = qs.filter(or_lookup).distinct()
        return qs

class ProjectManager(models.Manager):
    def get_queryset(self):
        return ProjectQuerySet(self.model, using=self._db)
    def search(self, query=None):
        return self.get_queryset().search(query=query)

User = settings.AUTH_USER_MODEL
class Project(models.Model):
    project_partner_user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=250)
    contact_first_name = models.CharField(max_length=250)
    contact_last_name = models.CharField(max_length=250)
    contact_phone = models.CharField(blank=True, max_length=20)
    contact_email = models.EmailField(blank=True, max_length=100)
    contact_addr_street = models.CharField(blank=True, max_length=250)
    contact_addr_apt = models.CharField(blank=True, max_length=10)
    contact_addr_city = models.CharField(blank=True, max_length=50)
    contact_addr_state = models.CharField(blank=True, max_length=100)
    contact_addr_zip = models.CharField(blank=True, max_length=6)
    location_addr_street = models.CharField(blank=True, max_length=250)
    location_addr_apt = models.CharField(blank=True, max_length=10)
    location_addr_city = models.CharField(blank=True, max_length=50)
    location_addr_state = models.CharField(blank=True, max_length=100)
    location_addr_zip = models.CharField(blank=True, max_length=6)
    sponsorship_amount_per_child = models.FloatField(default=50)
    image = models.ImageField(blank = True, default = 'project_pics/india.gif', upload_to='project_pics')

    objects = ProjectManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('project:project-detail', kwargs={'pk': self.pk})

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        try:
            thumbnail_size = (300, 300)
            img.thumbnail(thumbnail_size)
            f, e = os.path.splitext(self.image.path)
            thumbnail_img = f + ".thumbnail"
            img.save(thumbnail_img, 'JPEG')
        except IOError:
            print("cannot create thumbnail for", img)
