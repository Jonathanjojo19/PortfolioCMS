from django.shortcuts import render
from information.models import (
    PersonalInfo,
    Project
)

def index(request):
    return render(request, 'portfolio/index.html', {
        "info"      : PersonalInfo.objects.all().first(),
        "projects"  : Project.objects.all()
    })
