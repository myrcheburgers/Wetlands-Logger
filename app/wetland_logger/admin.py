from django.contrib import admin
from wetland_logger.models import User
from wetland_logger.models import Project
from wetland_logger.models import Datapoint

# Register your models here.
admin.site.register(User)
admin.site.register(Project)
admin.site.register(Datapoint)