from django import forms
from .models import Donor, Donation

class DonorForm(forms.ModelForm):

    first_name = forms.CharField(
                                label='First Name',
                                widget=forms.TextInput(attrs={"cols": 20,
                                                                "class": "active"})
                                                                )
    last_name = forms.CharField(
                                label='Last Name',
                                widget=forms.TextInput(attrs={"cols": 40})
                                )

    phone = forms.CharField()
    # description = forms.CharField(
    #                         widget=forms.Textarea(attrs={"placeholder": "Your Description Not Here",
    #                                                         "class": "new-class-name two",
    #                                                         "id": "id-for-textarea",
    #                                                         "rows": 5,
    #                                                         "cols": 60
    #                                                         }))
    # price = forms.DecimalField(initial=299.99)

    class Meta:
        model = Donor
        fields = [
            'first_name',
            'last_name',
            'phone',
            'email',
            'addr_street',
            'addr_apt',
            'addr_city',
            'addr_zip',
        ]

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = [
            'sponsorship_amount',
            'expiry_date',
        ]
