from django.contrib import admin
from .models import capacidad, Profile
from import_export.admin import ImportExportModelAdmin
# Register your models here.
#admin.site.register(capacidad)
@admin.register(capacidad)
@admin.register(Profile)

class userdat(ImportExportModelAdmin):
    pass
