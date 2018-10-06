from django import forms
from .models import Child
from .choices import GENDER_CHOICES

class ChildForm(forms.ModelForm):

    first_name = forms.CharField(
                                label='First Name',
                                widget=forms.TextInput(attrs={"cols": 40,
                                                                "class": "active"})
                                                                )
    last_name = forms.CharField(
                                label='Last Name',
                                widget=forms.TextInput(attrs={"cols": 40})
                                )

    gender    = forms.ChoiceField(choices=GENDER_CHOICES)

    age       = forms.IntegerField(
                                # label='',
                                widget=forms.NumberInput()
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
            # 'project_owner_user',
            # 'project',
            'first_name',
            'last_name',
            'gender',
            'age',
        ]
