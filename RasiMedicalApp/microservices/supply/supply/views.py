import json

from ....kong.broker import Broker
from django.http import JsonResponse
from django.shortcuts import render
from .models import Supply


def home(request):
    response = Broker().get('supplies')
    context = {'supplies': response}
    return render(request, 'home.html', context)


def create_supply_form(request):
    return render(request, 'create_supply.html')


def list_supplies(request):
    queryset = Supply.objects.all()
    context = list(queryset.values('id', 'name', 'description', 'price', 'quantity'))
    return JsonResponse(context, safe=False)


def create_supply(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        supply = Supply.objects.create(
            name=data['name'],
            description=data['description'],
            price=data['price'],
            quantity=data['quantity']
        )
        supply.save()
        return JsonResponse({'message': 'Supply created successfully!'}, status=201)
