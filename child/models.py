from django.db import models
from project.models import Project
from django.urls import reverse
from django.conf import settings
from .choices import GENDER_CHOICES
from datetime import date
from django.utils.timezone import now


# Create your models here.
User = settings.AUTH_USER_MODEL
class Child(models.Model):
    project_partner_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='partner_user_children')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_children')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

        class Meta:
            verbose_name_plural = "Children"
    def get_absolute_url(self):
        return reverse('child:child-detail', kwargs={'pk': self.pk})

class Progress(models.Model):
    child = models.ForeignKey(Child, on_delete=models.PROTECT)
    # progress_date = models.DateField(default=date.today())
    progress_date = models.DateField(default=now)
    milestone = models.CharField(max_length=100, blank=True)
    short_description = models.CharField(max_length=250)
    long_description = models.TextField(blank=True)

    def __str__(self):
        return str(self.progress_date) + ': ' + self.short_description
        # return str(self.child) + ' ' + str(self.progress_date) + ' ' + self.milestone + self.short_description

    def get_absolute_url(self):
        return reverse('child:progress-detail', kwargs={'child_pk':self.child.pk, 'pk': self.pk})
