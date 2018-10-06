from django.db import models
from project.models import Project
from django.urls import reverse
from django.conf import settings
from .choices import GENDER_CHOICES

# Create your models here.
User = settings.AUTH_USER_MODEL
class Child(models.Model):
    project_partner_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='project_children')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
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
