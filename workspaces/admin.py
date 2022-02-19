from django.contrib import admin
from . import models


admin.site.register(models.Workspace)
admin.site.register(models.File)