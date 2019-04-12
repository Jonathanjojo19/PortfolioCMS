from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    email = models.EmailField(max_length=100)
    linkedin = models.URLField(max_length=100)
    git = models.URLField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    logo = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "PersonalInfo"
    
    def __str__(self):
        return "[INFO] {}".format(self.name)

    def save(self, *args, **kwargs):
        if PersonalInfo.objects.exists() and not self.pk:
            raise ValidationError('There can be only one PersonalInfo instance')
        return super(PersonalInfo, self).save(*args, **kwargs)

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    url = models.URLField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Projects"
    
    def __str__(self):
        return "[PROJECT] {}".format(self.name) 