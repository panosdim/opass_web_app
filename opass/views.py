import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from opass.models import TOLL_RATES


def index(request):
    return render(request, 'opass/index.html', {'Frontal': TOLL_RATES['Frontal'], 'Ramp': TOLL_RATES['Ramp']})


def calculate(request):
    response_data = {}
    cost = 0
    vehicle_type = int(request.POST.get('vehicle'))
    for key, value in request.POST.items():
        if key != 'vehicle' or key != 'csrfmiddlewaretoken':
            if key in TOLL_RATES['Frontal']:
                cost += TOLL_RATES['Frontal'][key][vehicle_type]
            if key in TOLL_RATES['Ramp']:
                cost += TOLL_RATES['Ramp'][key][vehicle_type]
    response_data['cost'] = cost
    return JsonResponse(response_data)

    # return render(request, 'opass/index.html',
#               {'Frontal': TOLL_RATES['Frontal'], 'Ramp': TOLL_RATES['Ramp']})
