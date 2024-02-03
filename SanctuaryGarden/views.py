from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *



def home_page(request):

    return render(request, 'pages/home.html')

def about_page(request):
    return render(request, 'pages/about.html')

def administrator_page(request):
    plantcareguide = PlantCareGuide.objects.all()
    return render(request, 'pages/administrator.html', {'plantcareguide': plantcareguide})

def collection_page(request):
    plantcareguide = PlantCareGuide.objects.all()
    return render(request, 'pages/collection.html', {'plantcareguide': plantcareguide})


def PlantCareGuide_page(request,id):
    plantcareguide = PlantCareGuide.objects.get(id=id)
    return render(request, 'pages/PlantCareGuide.html', {'plantcareguide': plantcareguide})


def login_page(request):
    return HttpResponse("This is Loginpage")

def category_page(request):
    plantcareguide = PlantCareGuide.objects.all()
    return render(request, 'pages/category.html', {'plantcareguide': plantcareguide})


def done(request, id):
    if request.method == 'POST':
        plantcareguide = PlantCareGuide.objects.get(id=id)
        plantcareguide.status = "done"
        plantcareguide.save()
        return redirect('/collection/')

def addplant(request):
    return render(request, 'pages/addplant.html')

def addplants(request):
    if request.method == 'POST':
        a = request.POST.get('plant_name', '')
        b = request.POST.get('description', '')
        c = request.POST.get('seasonal', '')
        d = request.POST.get('guide', '')
        e = request.POST.get('admin_name', '')
        f = request.FILES.get('photo', None)
        g = request.POST.get('status', '')

        mem = PlantCareGuide(plant_name=a, description=b, seasonal=c, guide=d, admin_name=e, photo=f, status=g)
        mem.save()
    return redirect('/administrator/')


def deleteplant(request, id):
    blog = get_object_or_404(PlantCareGuide, id=id)
    blog.delete()
    return redirect('/administrator/')

def editplantpage(request,id):
    mem=PlantCareGuide.objects.get(id=id)
    return render(request, "pages/editplant.html",{'mem':mem})

def editplant(request, id):
    if request.method == 'POST':
        a = request.POST.get('plant_name')
        b = request.POST.get('description')
        c = request.POST.get('seasonal')
        d = request.POST.get('guide')
        e = request.POST.get('admin_name')
        f = request.FILES.get('photo')
        g = request.POST.get('status')

        mem = PlantCareGuide.objects.get(id=id)
        mem.plant_name = a
        mem.description = b
        mem.seasonal = c
        mem.guide = d
        mem.admin_name = e
        if f:
            mem.photo = f
        mem.status = g
        mem.save()
        return redirect('/administrator/')
