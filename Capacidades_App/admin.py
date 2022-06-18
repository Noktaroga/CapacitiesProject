from django.contrib import admin
from .models import capacidad
from import_export.admin import ImportExportModelAdmin
# Register your models here.
#admin.site.register(capacidad)
@admin.register(capacidad)

class userdat(ImportExportModelAdmin):
    pass
