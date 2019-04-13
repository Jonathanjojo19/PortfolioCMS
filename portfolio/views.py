from django.shortcuts import render
from information.models import (
    PersonalInfo,
    Project,
    Logo
)

def index(request):
    return render(request, 'portfolio/index.html', {
        "logo"      : Logo.objects.all().first(),
        "info"      : PersonalInfo.objects.all().first(),
        "projects"  : Project.objects.all()
    })
