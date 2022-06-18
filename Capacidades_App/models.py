from django.db import models

# Create your models here.
class capacidad(models.Model):
    Ano_Solicitud = models.CharField(null=True,max_length=500)
    ID_SGI = models.CharField(null=True,max_length=500)
    Zona = models.CharField(null=True,max_length=500)
    HUB = models.CharField(null=True,max_length=500)
    Comuna = models.CharField(null=True,max_length=500)
    Clave = models.CharField(null=True,max_length=500)
    Cuadrantes = models.CharField(null=True,max_length=500)
    Cantidad_N = models.CharField(null=True,max_length=500)
    Fecha_Solicitud = models.CharField(null=True,max_length=500)
    Year = models.CharField(null=True,max_length=500)
    Mes = models.CharField(null=True,max_length=500)
    W_Solicitud = models.CharField(null=True,max_length=500)
    OBS_Solicitud= models.CharField(null=True,max_length=500)
    Tipo_Solucion = models.CharField(null=True,max_length=500)
    Clientes_Afectados = models.CharField(null=True,max_length=500)
    Estado_Ejecucion = models.CharField(null=True,max_length=500)
    Sol2 = models.CharField(null=True,max_length=500)
    Fecha_Cancelado = models.CharField(null=True,max_length=500)
    Tipo_de_Red = models.CharField(null=True,max_length=500)
    Estado_Design_Simplificado = models.CharField(null=True,max_length=500)
    Fecha_Design = models.CharField(null=True,max_length=500)
    Asignacion_Energía = models.CharField(null=True,max_length=500)
    Obras_Complementarias = models.CharField(null=True,max_length=500)
    Estado_Asignación_Energía = models.CharField(null=True,max_length=500)
    Estado_Ejecucion_2 = models.CharField(null=True,max_length=500)
    Fecha_Ejecucion = models.CharField(null=True,max_length=500)
    Year_Ejecucion = models.CharField(null=True,max_length=500)
    MES_Ejecucion = models.CharField(null=True,max_length=500)
    Semana_Ejecucion = models.CharField(null=True,max_length=500)
    EPS = models.CharField(null=True,max_length=500)
    Fecha_Comunicacion_EPS = models.CharField(null=True,max_length=500)
    Responsable = models.CharField(null=True,max_length=500)
    Motivo = models.CharField(null=True,max_length=500)
    KPI_DESIGN =models.CharField(null=True,max_length=500)
    KPI_EJECUCION = models.CharField(null=True,max_length=500)
    Estado_CaPO = models.CharField(null=True,max_length=500)
    Fecha_Estado = models.CharField(null=True,max_length=500)
    Observaciones_CaPO = models.CharField(null=True,max_length=500)
    Horas_95 = models.CharField(null=True,max_length=500)
    Horas_90 = models.CharField(null=True,max_length=500)
    Zona_Roja = models.CharField(null=True,max_length=500)
    Clase_Zona_Roja = models.CharField(null=True,max_length=500)
    Mes_Sol = models.CharField(null=True,max_length=500)
    Mes_Ejecucion_2 = models.CharField(null=True,max_length=500)
    Year_2022 =models.CharField(null=True,max_length=500)

    class Meta:
        db_table = 'capacidad'