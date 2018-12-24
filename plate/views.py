from django.shortcuts import render
from django.views.generic import DetailView
from . import models
from report.models import Report
# Create your views here.

class PlateDetail(DetailView):
    model = models.Vehicle_plate

def loadPlatePage(request, pk=None, load_plate=None):
    try:
        if pk:
            plate = models.Vehicle_plate.objects.get(pk=pk)
        if load_plate:
            plate = models.Vehicle_plate.objects.get(plate_nubmer=load_plate.upper())
        reports = Report.objects.all().filter(vehicle_plate=plate)
        contex = {
            'plate': plate,
            'reports': reports,
        }
        return render(request, 'plate/vehicle_plate_detail.html', contex)
    except models.Vehicle_plate.DoesNotExist:
        contex = {
            'plate': load_plate,
        }
        return render(request, 'plate/no_plate_found.html', contex)

def findPlate(request):
    return loadPlatePage(request, load_plate=request.GET.get('search'))
