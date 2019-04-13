from django.shortcuts import render
from .forms import (
    PersonalInfoForm,
    ProjectForm,
    LogoForm
)
from information.models import (
    PersonalInfo,
    Project,
    Logo
)

from django.urls import reverse
from django.http import JsonResponse
import json
from django.contrib import messages 

# Create your views here.
def dashboard(request):
    personal_info = PersonalInfo.objects.all().first() 
    logo = Logo.objects.all().first()
    return render(request, 'cms/dashboard.html', {
        "logo" : logo,
        "info" : personal_info,
        "info_form" : PersonalInfoForm(instance=personal_info),
        "logo_form" : LogoForm(instance=personal_info)
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

def updateProject(request):
    return None

# def updateLogo(request):
#     if request.method == "POST":
#         print(json.loads(request.body))
#         print(request.POST, request.FILES)
#         current_instance = Logo.objects.all().first()
#         form = LogoForm(data=request.POST, files=request.FILES, instance=current_instance)
#         if form.is_valid():
#             form.save()
#             return JsonResponse(
#                 {
#                     "success" : True,
#                     "message" : "Your info have been successfuly updated",
#                 }
#             )
#         else:
#             return JsonResponse(
#                 {
#                     "success" : False,
#                     "message" : form.errors,
#                 }
#             )
#     else:
#         return JsonResponse(
#             {
#                 "success" : False,
#                 "message" : "Unallowed Method"
#             }
#         )
