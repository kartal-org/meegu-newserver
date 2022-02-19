from django.contrib import admin
from . import models


admin.site.register(models.Institution)
admin.site.register(models.Verification)
admin.site.register(models.Department)
admin.site.register(models.Member)
