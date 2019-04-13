from django import forms
from information.models import (
    PersonalInfo,
    Project
)

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo 
        fields = "__all__"
        exclude = ['logo']
        labels = {
            "name" : "Name",
            "description" : "Description",
            "email" : "E-mail",
            "linkedin" : "LinkedIn",
            "git" : "Git",
            "phone_number" : "Phone",
            "title" : "Site Name"
        }

        widgets = {
            "name" : forms.TextInput(
                attrs = {
                    "class" : "form-control",
                    "required" : True,
                    "placeholder" : "Your Name"
                }
            ),
            "description" : forms.Textarea(
                attrs = {
                    "class" : "form-control",
                    "required" : True,
                    "placeholder" : "About You"
                }
            ),
            "email" : forms.EmailInput(
                attrs = {
                    "class" : "form-control",
                    "required" : True,
                    "placeholder" : "Your E-mail Address"
                }
            ),
            "linkedin" : forms.URLInput(
                attrs = {
                    "class" : "form-control",
                    "required" : True,
                    "placeholder" : "Your LinkedIn Profile"
                }
            ),
            "git" : forms.URLInput(
                attrs = {
                    "class" : "form-control",
                    "required" : True,
                    "placeholder" : "Your Git URL"
                }
            ),
            "phone_number" : forms.TextInput(
                attrs = {
                    "class" : "form-control",
                    "required" : True,
                    "placeholder" : "Your Phone Number"
                }
            ),
            "title" : forms.TextInput(
                attrs = {
                    "class" : "form-control",
                    "required" : True,
                    "placeholder" : "Your Site Name"
                }
            )
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"