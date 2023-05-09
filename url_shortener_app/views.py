from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def encode(request):
    
    return JsonResponse({'encode': 'something'})

def decode(request):
    
    return JsonResponse({'decode': 'something'})