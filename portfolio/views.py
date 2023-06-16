from django.shortcuts import render
from .models import Project
# Create your views here.

def portfolio(request):
    projects = Project.objects.all() #objects gestiona en tiempo de ejecucion los objetos de la BD
    context = {'projects':projects}
    return render(request,"portfolio/portfolio.html", context)
    