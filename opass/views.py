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
    vehicle_type = int(request.POST.get('vehicle'))
    working_days = bool(request.POST.get('Working Days'))
    for key, value in request.POST.items():
        if key in FRONTAL:
            cost += FRONTAL[key][vehicle_type]
        if key in RAMP:
            cost += RAMP[key][vehicle_type]

    for month in range(1, 13):
        response_data[month] = calculate_cost(cost, working_days, month)

    return JsonResponse(response_data)
