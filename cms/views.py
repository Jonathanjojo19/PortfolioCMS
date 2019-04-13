from django.shortcuts import render
from .forms import (
    PersonalInfoForm,
    ProjectForm
)
from information.models import (
    PersonalInfo,
    Project
)

from django.urls import reverse
from django.http import JsonResponse
import json
from django.contrib import messages 

# Create your views here.
def dashboard(request):
    return render(request, 'cms/dashboard.html', {
        "info" : PersonalInfo.objects.all().first(),
        "form" : PersonalInfoForm(instance=PersonalInfo.objects.all().first())
    })

def updateInfo(request):
    if request.method == "PUT" and request.is_ajax():
        current_instance = PersonalInfo.objects.all().first()
        data = json.loads(request.body)
        form = PersonalInfoForm({
            "name" : data["name"],
            "description" : data["description"],
            "email" : data["email"],
            "linkedin" : data["linkedin"],
            "git" : data["git"],
            "phone_number" : data["phone_number"],
            "title" : data["title"]
        }, instance=current_instance)

        if form.is_valid():
            form.save()
            return JsonResponse(
                {
                    "success" : True,
                    "message" : "Your info have been successfuly updated",
                }
            )
        else:
            return JsonResponse(
                {
                    "success" : False,
                    "message" : form.errors,
                }
            )
    else:
        return JsonResponse(
            {
                "success" : False,
                "message" : "Unallowed Method"
            }
        )