from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from opass.calculate import calculate_cost
from opass.models import FRONTAL, RAMP


def index(request):
    return render(request, 'opass/index.html', {'Frontal': FRONTAL, 'Ramp': RAMP})


def calculate(request):
    response_data = {}
    cost = 0
    vehicle_type = int(request.POST.get('vehicle', 1))
    working_days = bool(request.POST.get('Working Days'))
    nr_of_passes = int(request.POST.get('Passes per day', 2))
    for key, value in request.POST.items():
        if key in FRONTAL:
            cost += FRONTAL[key][vehicle_type]
        if key in RAMP:
            cost += RAMP[key][vehicle_type]

    if cost == 0:
        return JsonResponse(status=422, data={'message': 'You have to select at least one Frontal or Ramp station'})
    for month in range(1, 13):
        response_data[month] = calculate_cost(cost, working_days, month, nr_of_passes)

    return JsonResponse(response_data)
