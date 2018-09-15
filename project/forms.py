from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):

    name = forms.CharField(
                                label='Project Name',
                                widget=forms.TextInput(attrs={"cols": 20,
                                                                "class": "active"})
                                                                )
    contact_name = forms.CharField(
                                label='Contact Name',
                                widget=forms.TextInput(attrs={"cols": 40})
                                )

    contact_phone = forms.CharField()
    # description = forms.CharField(
    #                         widget=forms.Textarea(attrs={"placeholder": "Your Description Not Here",
    #                                                         "class": "new-class-name two",
    #                                                         "id": "id-for-textarea",
    #                                                         "rows": 5,
    #                                                         "cols": 60
    #                                                         }))
    # price = forms.DecimalField(initial=299.99)

    class Meta:
        model = Project
        fields = [
            'name',
            'contact_name',
            'contact_phone',
            'contact_email',
            'contact_addr_street',
            'contact_addr_apt',
            'contact_addr_city',
            'contact_addr_state',
            'contact_addr_zip',
            'location_addr_street',
            'location_addr_apt',
            'location_addr_city',
            'location_addr_state',
            'location_addr_zip',
        ]