from django import forms
from .models import Child, Progress
from .choices import GENDER_CHOICES
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from django.forms.widgets import ClearableFileInput

# class MyClearableFileInput(ClearableFileInput):
#     initial_text = 'Currently'
#     input_text = 'Change'
#     clear_checkbox_label = 'Clear'

class ChildForm(forms.ModelForm):

    # first_name = forms.CharField(
    #                             label='First Name',
    #                             widget=forms.TextInput(attrs={"cols": 40,
    #                                                             "class": "active"})
    #                                                             )
    # last_name = forms.CharField(
    #                             label='Last Name',
    #                             widget=forms.TextInput(attrs={"cols": 40})
    #                             )
    #
    # gender    = forms.ChoiceField(choices=GENDER_CHOICES)

    # age       = forms.IntegerField(
    #                             label='Age',
    #                             widget=forms.NumberInput()
    #                             )
    image     = forms.ImageField(label='Child Profile Image',
                                required=False,
                                error_messages = {'invalid':"Image files only"},
                                # widget = MyClearableFileInput,
                                )
    # description = forms.CharField(
    #                         widget=forms.Textarea(attrs={"placeholder": "Your Description Not Here",
    #                                                         "class": "new-class-name two",
    #                                                         "id": "id-for-textarea",
    #                                                         "rows": 5,
    #                                                         "cols": 60
    #                                                         }))
    # price = forms.DecimalField(initial=299.99)

    # def clean_project(self, *args, **kwargs):
    #     title = self.cleaned_data.get("title")
    #     if not "SV" in title:
    #         raise forms.ValidationError("This is not a valid project")
    #     else:
    #         return title
    #     endif

    class Meta:
        model = Child
        fields = [
            'first_name',
            'last_name',
            'gender',
            'age',
            'image',
        ]


class ProgressForm(forms.ModelForm):
    long_description = forms.CharField(
            widget=forms.Textarea(attrs={"placeholder": "Enter detailed desccription here",
                                        # "class": "new-class-name two",
                                        # "id": "id-for-textarea",
                                        "rows": 10,
                                        "cols": 60
                                        }))

    class Meta:
        model = Progress
        fields = [
            'progress_date',
            'milestone',
            'short_description',
            'long_description',
        ]
