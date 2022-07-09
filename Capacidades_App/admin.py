from django.contrib import admin
from .models import capacidad, Profile
from import_export.admin import ImportExportModelAdmin
# Register your models here.
#admin.site.register(capacidad)
@admin.register(capacidad)
@admin.register(Profile)

class userdat(ImportExportModelAdmin):
    pass



"""
class PersonAdmin(ImportExportModelAdmin):
    list_display = (
        'Ano_Solicitud'
        ,'ID_SGI'
        ,'Zona'
        ,'HUB'
        ,'Comuna'
        ,'Clave'
        ,'Cuadrantes'
        ,'Cantidad_N'
        ,'Fecha_Solicitud'
        ,'Year'
        ,'Mes'
        ,'W_Solicitud'
        ,'OBS_Solicitud'
        ,'Tipo_Solucion'
        ,'Clientes_Afectados'
        ,'Estado_Ejecucion'
        ,'Sol2'
        ,'Fecha_Cancelado'
        ,'Tipo_de_Red'
        ,'Estado_Design_Simplificado'
        ,'Fecha_Design'
        ,'Asignacion_Energía'
        ,'Obras_Complementarias'
        ,'Estado_Asignación_Energía'
        ,'Estado_Ejecucion_2'
        ,'Fecha_Ejecucion'
        ,'Year_Ejecucion'
        ,'MES_Ejecucion'
        ,'Semana_Ejecucion'
        ,'EPS'
        ,'Fecha_Comunicacion_EPS'
        ,'Responsable'
        ,'Motivo'
        ,'KPI_DESIGN'
        ,'KPI_EJECUCION'
        ,'Estado_CaPO'
        ,'Fecha_Estado'
        ,'Observaciones_CaPO'
        ,'Horas_95'
        ,'Horas_90'
        ,'Zona_Roja'
        ,'Clase_Zona_Roja'
        ,'Mes_Sol'
        ,'Mes_Ejecucion_2'
        ,'Year_2022'
        ,)
"""
