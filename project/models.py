from django.db import models
from django.urls import reverse
from django.db.models import Q

# Create your models here.

class ProjectQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup =     (Q(name__icontains=query) |
                             Q(contact_name__icontains=query)
                            )
            qs = qs.filter(or_lookup).distinct()
        return qs

class ProjectManager(models.Manager):
    def get_queryset(self):
        return ProjectQuerySet(self.model, using=self._db)
    def search(self, query=None):
        return self.get_queryset().search(query=query)


class Project(models.Model):
    name = models.CharField(max_length=250)
    contact_name = models.CharField(max_length=250)
    contact_phone = models.CharField(blank=True, max_length=20)
    contact_email = models.EmailField(blank=True, max_length=250)
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
    
    objects = ProjectManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('project:project-detail', kwargs={'pk': self.pk})

class Child(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

        class Meta:
            verbose_name_plural = "Children"
