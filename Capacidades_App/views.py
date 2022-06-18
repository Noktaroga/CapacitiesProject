from django.shortcuts import render
from .models import capacidad
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.

def index(request):
    book = capacidad.objects.all()
    context = {'book':book}
    return render(request,'index.html',context)

def base(request):
    return render(request,'base.html')

def dashboard(request):
    book = capacidad.objects.all()
    p = Paginator(book, 25)  # creating a paginator object
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    context = {'book':book,'page_obj': page_obj}
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



        #post = capacidad.objects.all().filter(ID_SGI__icontains=search)
        #return render(request,'./searchbar.html',{'post':post})
