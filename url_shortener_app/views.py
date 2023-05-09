from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

csrf_exempt
def encode(request):
    print(request.POST.get('url'))
    return JsonResponse({'encode': 'something'})

def decode(request):
    
    return JsonResponse({'decode': 'something'})