from django.contrib import admin
from .models import (
    PersonalInfo,
    Project
)

# Register your models here.
admin.site.register(PersonalInfo)
admin.site.register(Project)