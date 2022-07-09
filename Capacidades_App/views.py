from django.shortcuts import render, redirect
from .models import capacidad
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .forms import capacidadForm
from django.contrib import messages
from tablib import Dataset
import csv, io

# Create your views here.

def index(request):
    book = capacidad.objects.all()
    context = {'book':book}
    return render(request,'index.html',context)

def base(request):
    return render(request,'base.html')

def dashboard(request):
    book = capacidad.objects.all().order_by('ID_SGI')
    p = Paginator(book,per_page=15)  # creating a paginator object
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    context = {'page_obj': page_obj,'book':book}
    # sending the page object to index.html
    return render(request,'./dashboard.html', context)

def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        multiple_post = Q(Q(ID_SGI__icontains=search) | Q(Zona__icontains=search) | Q(Estado_Ejecucion__icontains=search) | Q(Tipo_Solucion__icontains=search) | Q(Fecha_Ejecucion__icontains=search) | Q(EPS__icontains=search) | Q(Estado_CaPO__icontains=search) | Q(Clave__icontains=search))#Aca podemos ejecutar los diferentes filtros que queramos aplicar a nuestra searchbar
        post = capacidad.objects.all().filter(multiple_post)
        context_2 = {'post':post}
        # sending the page object to index.html
        return render(request,'./searchbar.html', context_2)

def crearCapacidad(request):
    if request.method == 'GET':
        form = capacidadForm()
        contexto = {'form':form}
    else:
        form = capacidadForm(request.POST) #Llamando a capacidadForm(request.POST) el cual contiene toda nuestra base al hacerle un request.POST me permite ingresar informacion en ella.
        contexto = {'form':form}
        if form.is_valid(): #
            form.save()
            return redirect('dashboard')
    return render(request,'crear_Capacidad.html',contexto)
        #post = capacidad.objects.all().filter(ID_SGI__icontains=search)
        #return render(request,'./searchbar.html',{'post':post})
def editarCapacidad(request, ID_SGI):
    book = capacidad.objects.get(ID_SGI = ID_SGI)
    if request.method == 'GET':
        form = capacidadForm(instance = book)#Dentro de book se creara una instancia de una clase particular en este caso ID_SGI es el que se esta tomando en cuenta.
        contexto = {'form':form}
    else:
        form = capacidadForm(request.POST, instance=book)
        contexto = {'form':form}
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    return render(request,'crear_Capacidad.html',contexto)

def eliminarCapacidad(request,ID_SGI):
    book = capacidad.objects.get(ID_SGI=ID_SGI)
    book.delete()
    return redirect('dashboard')

def profile_upload(request):
    # declaring template
    template = "upload.html"
    data = capacidad.objects.all()
    prompt = {
        'order': 'Order of the CSV should be: ID_SGI , Zona ...',
        'capacidades': data
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)


    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')

    data_set = csv_file.read().decode('UTF-8')

    # setup a stream which is when we loop through each line we are able to handle a data in a stream.
    io_string = io.StringIO(data_set)
    next(io_string)

    for column in csv.reader(io_string, delimiter=','):
        created = capacidad.objects.update_or_create(Ano_Solicitud=column[0]
            ,ID_SGI=column[1]
            ,Zona=column[2]
            ,HUB=column[3]
            ,Comuna=column[4]
            ,Clave=column[5]
            ,Cuadrantes=column[6]
            ,Cantidad_N=column[7]
            ,Fecha_Solicitud=column[8]
            ,Year=column[9]
            ,Mes=column[10]
            ,W_Solicitud=column[11]
            ,OBS_Solicitud=column[12]
            ,Tipo_Solucion=column[13]
            ,Clientes_Afectados=column[14]
            ,Estado_Ejecucion=column[15]
            ,Sol2=column[16]
            ,Fecha_Cancelado=column[17]
            ,Tipo_de_Red=column[18]
            ,Estado_Design_Simplificado=column[19]
            ,Fecha_Design=column[20]
            ,Asignacion_Energía=column[21]
            ,Obras_Complementarias=column[22]
            ,Estado_Asignación_Energía=column[23]
            ,Estado_Ejecucion_2=column[24]
            ,Fecha_Ejecucion=column[25]
            ,Year_Ejecucion=column[26]
            ,MES_Ejecucion=column[27]
            ,Semana_Ejecucion=column[28]
            ,EPS=column[29]
            ,Fecha_Comunicacion_EPS=column[30]
            ,Responsable=column[31]
            ,Motivo=column[32]
            ,KPI_DESIGN=column[33]
            ,KPI_EJECUCION=column[34]
            ,Estado_CaPO=column[35]
            ,Fecha_Estado=column[36]
            ,Observaciones_CaPO=column[37]
            ,Horas_95=column[38]
            ,Horas_90=column[39]
            ,Zona_Roja=column[41]
            ,Clase_Zona_Roja=column[41]
            ,Mes_Sol=column[42]
            ,Mes_Ejecucion_2=column[43]
            ,Year_2022=column[44]
            ,
        )
    context = {}
    return render(request, template, context)
