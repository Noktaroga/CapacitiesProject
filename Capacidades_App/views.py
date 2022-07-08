from django.shortcuts import render, redirect
from .models import capacidad
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .forms import capacidadForm
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
        form = capacidadForm(request.POST)
        contexto = {'form':form}
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    return render(request,'crear_Capacidad.html',contexto)
        #post = capacidad.objects.all().filter(ID_SGI__icontains=search)
        #return render(request,'./searchbar.html',{'post':post})
def editarCapacidad(request, ID_SGI):
    book = capacidad.objects.get(ID_SGI = ID_SGI)
    if request.method == 'GET':
        form = capacidadForm(instance = book)
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
