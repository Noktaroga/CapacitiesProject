# Generated by Django 4.0.5 on 2022-07-05 03:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Capacidades_App', '0003_capacidad_asignacion_energía_capacidad_cantidad_n_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacidad',
            name='Ano_Solicitud',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Asignacion_Energía',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Cantidad_N',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Clase_Zona_Roja',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Clave',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Clientes_Afectados',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Comuna',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Cuadrantes',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='EPS',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Estado_Asignación_Energía',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Estado_CaPO',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Estado_Design_Simplificado',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Estado_Ejecucion',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Estado_Ejecucion_2',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Fecha_Cancelado',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Fecha_Comunicacion_EPS',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Fecha_Design',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Fecha_Ejecucion',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Fecha_Estado',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Fecha_Solicitud',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='HUB',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Horas_90',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Horas_95',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='ID_SGI',
            field=models.CharField(default='', max_length=500, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='KPI_DESIGN',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='KPI_EJECUCION',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='MES_Ejecucion',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Mes',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Mes_Ejecucion_2',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Mes_Sol',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Motivo',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='OBS_Solicitud',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Obras_Complementarias',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Observaciones_CaPO',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Responsable',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Semana_Ejecucion',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Sol2',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Tipo_Solucion',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Tipo_de_Red',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='W_Solicitud',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Year',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Year_2022',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Year_Ejecucion',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Zona',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='capacidad',
            name='Zona_Roja',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('user', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]