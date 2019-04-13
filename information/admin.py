from django.contrib import admin
from .models import (
    PersonalInfo,
    Project,
    Logo
)

# Register your models here.
admin.site.register(PersonalInfo)
admin.site.register(Project)
admin.site.register(Logo)