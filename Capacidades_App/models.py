from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class capacidad(models.Model):
    Ano_Solicitud = models.CharField(null=True,max_length=500,default="")
    ID_SGI = models.CharField(null=True,max_length=500,unique=True,default="")
    Zona = models.CharField(null=True,max_length=500,default="")
    HUB = models.CharField(null=True,max_length=500,default="")
    Comuna = models.CharField(null=True,max_length=500)
    Clave = models.CharField(max_length=500,default="")
    Cuadrantes = models.CharField(max_length=500,default="")
    Cantidad_N = models.CharField(max_length=500,default="")
    Fecha_Solicitud = models.CharField(max_length=500,default="")
    Year = models.CharField(max_length=500,default="")
    Mes = models.CharField(max_length=500,default="")
    W_Solicitud = models.CharField(max_length=500,default="")
    OBS_Solicitud= models.CharField(null=False,max_length=500,default="")
    Tipo_Solucion = models.CharField(max_length=500,default="")
    Clientes_Afectados = models.CharField(max_length=500,default="")
    Estado_Ejecucion = models.CharField(max_length=500,default="")
    Sol2 = models.CharField(max_length=500,default="")
    Fecha_Cancelado = models.CharField(max_length=500,default="")
    Tipo_de_Red = models.CharField(max_length=500,default="")
    Estado_Design_Simplificado = models.CharField(max_length=500,default="")
    Fecha_Design = models.CharField(max_length=500,default="")
    Asignacion_Energía = models.CharField(max_length=500,default="")
    Obras_Complementarias = models.CharField(max_length=500,default="")
    Estado_Asignación_Energía = models.CharField(max_length=500,default="")
    Estado_Ejecucion_2 = models.CharField(max_length=500,default="")
    Fecha_Ejecucion = models.CharField(max_length=500,default="")
    Year_Ejecucion = models.CharField(max_length=500,default="")
    MES_Ejecucion = models.CharField(max_length=500,default="")
    Semana_Ejecucion = models.CharField(max_length=500,default="")
    EPS = models.CharField(max_length=500,default="")
    Fecha_Comunicacion_EPS = models.CharField(max_length=500,default="")
    Responsable = models.CharField(max_length=500,default="")
    Motivo = models.CharField(max_length=500,default="")
    KPI_DESIGN =models.CharField(max_length=500,default="")
    KPI_EJECUCION = models.CharField(max_length=500,default="")
    Estado_CaPO = models.CharField(max_length=500,default="")
    Fecha_Estado = models.CharField(max_length=500,default="")
    Observaciones_CaPO = models.CharField(max_length=500,default="")
    Horas_95 = models.CharField(max_length=500,default="")
    Horas_90 = models.CharField(max_length=500,default="")
    Zona_Roja = models.CharField(max_length=500,default="")
    Clase_Zona_Roja = models.CharField(max_length=500,default="")
    Mes_Sol = models.CharField(max_length=500,default="")
    Mes_Ejecucion_2 = models.CharField(max_length=500,default="")
    Year_2022 =models.CharField(max_length=500,default="")

    class Meta:
        db_table = 'capacidad'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default="")
    image = models.ImageField(default = 'default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
