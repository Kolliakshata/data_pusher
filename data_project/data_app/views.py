from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Account, Destination
from .serializers import AccountSerializer, DestinationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import requests

@api_view(['GET', 'POST'])
def account_list_create(request):
    if request.method == 'GET':
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def account_retrieve_update_delete(request, account_id):
    account = get_object_or_404(Account, id=account_id)

    if request.method == 'GET':
        serializer = AccountSerializer(account)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        account.delete()
        return Response(status=204)

@api_view(['GET', 'POST'])
def destination_list_create(request):
    if request.method == 'GET':
        destinations = Destination.objects.all()
        serializer = DestinationSerializer(destinations, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DestinationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def destination_retrieve_update_delete(request, destination_id):
    destination = get_object_or_404(Destination, id=destination_id)

    if request.method == 'GET':
        serializer = DestinationSerializer(destination)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DestinationSerializer(destination, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        destination.delete()
        return Response(status=204)
    

def get_destinations_for_account(request, account_id):
    account = get_object_or_404(Account, id=account_id)
    destinations = Destination.objects.filter(account=account)

    destination_data = [
        {
            'id': destination.id,
            'url': destination.url,
            'http_method': destination.http_method,
            'headers': destination.headers,
        }
        for destination in destinations
    ]

    
    return JsonResponse(destination_data, safe=False)
def incoming_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid Data'}, status=400)
        app_secret_token = request.headers.get('CL-XTOKEN')

        if not app_secret_token:
            return JsonResponse({'message': 'Unauthenticated'}, status=401)

        account = get_object_or_404(Account, app_secret_token=app_secret_token)
        for destination in account.destinations.all():
            response = requests.post(destination.url, json=data, headers=destination.headers)
    return JsonResponse({'message': 'Data processed successfully'})






