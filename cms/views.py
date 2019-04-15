from django.shortcuts import render, redirect
from .forms import (
    PersonalInfoForm,
    ProjectForm,
    ProjectModelFormSet
)
from information.models import (
    PersonalInfo,
    Project,
)

from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import JsonResponse
from django.contrib import messages 
import json

@login_required(login_url="/auth/login")
def dashboard(request):
    personal_info = PersonalInfo.objects.all().first() 
    projects = Project.objects.all()
    return render(request, 'cms/dashboard.html', {
        "projects" : projects,
        "info" : personal_info,
        "info_form" : PersonalInfoForm(instance=personal_info),
        "project_form" : ProjectModelFormSet()
    })

def update_info(request):
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
            return return_response(True)
        else:
            return return_response(False, form.errors)
    else:
        return_response(False, "Unallowed Method")

def update_project(request):
    if request.method == "POST":
        data = json.loads(request.body)
        form = ProjectForm({
            "name" : data["name"],
            "description" : data["description"],
            "url" : data["url"]
        })
        if form.is_valid():
            form.save()
            return JsonResponse({
                "success" : True,
                "message" : "Your info have been successfuly updated.",
                "url" : reverse('cms:dashboard')
            })
        else:
            return return_response(False, form.errors)
    elif request.method == "PUT" and request.is_ajax():
        data = json.loads(request.body)
        try:
            current_instance = Project.objects.filter(id=data['entryNo']).first()
            form = ProjectForm({
                "name" : data["name"],
                "description" : data["description"],
                "url" : data["url"]
            }, instance=current_instance)
        except: 
            form = ProjectForm({
                "name" : data["name"],
                "description" : data["description"],
                "url" : data["url"]
            })
        if form.is_valid():
            form.save()
            return return_response(True)
        else:
            return return_response(False, form.errors)
    elif request.method == "DELETE" and request.is_ajax():
        try:
            data = json.loads(request.body)
            current_instance = Project.objects.filter(id=data['entryNo']).first()
            current_instance.delete()
            return return_response(True)
        except Exception as e:
            return return_response(False, e)
    else:
        return return_response(False, "Unallowed Method")

def return_response(success, *argv):
    if success:
        return JsonResponse({
            "success" : True,
            "message" : "Your info have been successfuly updated."
        })
    else:
        return JsonResponse({
            "success" : False,
            "message" : argv[0],
        })