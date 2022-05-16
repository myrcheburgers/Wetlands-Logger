from django.db import models
from django.contrib.auth.hashers import make_password
import jsonfield

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255, null=False, unique=True)
    password = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=True, unique=True)

    def save(self, **kwargs):
        self.password = make_password(self.password)
        super().save(**kwargs)

class Project(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True)
    project_no = models.CharField(max_length=255, null=True, unique=True)
    state = models.CharField(max_length=64, null=True)
    usace_region = models.CharField(max_length=64, null=False)
    lrr = models.CharField(max_length=64, null=True)
    mlra = models.CharField(max_length=64, null=True)
    users = models.ManyToManyField(User, blank=True)

class Datapoint(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    sample_id = models.CharField(max_length=64, null=False)
    nwi = models.CharField(max_length=32, null=False)
    is_wetland = models.BooleanField()
    landform = models.CharField(max_length=32, null=True)
    relief = models.CharField(max_length=32, null=True)
    datum = models.CharField(max_length=32, null=True, default="NAD83")
    disturbed_veg = models.BooleanField(default=False)
    disturbed_soil = models.BooleanField(default=False)
    disturbed_hydro = models.BooleanField(default=False)
    problem_veg = models.BooleanField(default=False)
    problem_soil = models.BooleanField(default=False)
    problem_hydro = models.BooleanField(default=False)
    normal_circumstances = models.BooleanField(default=True)
    soils = jsonfield.JSONField()
    hydrology = jsonfield.JSONField()
    vegetation = jsonfield.JSONField()

