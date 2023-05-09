from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Url
from .serializers import UrlSerializer
# Create your views here.

csrf_exempt
def encode(request):
    # print(request.POST)
    if request.method == 'POST':
        original_url = request.POST.get('original_url')
        # print(original_url)
        if original_url:
            try:
                saved_url = Url(original_url=original_url)
                saved_url.save()
                # print(saved_url.shortened_url)
                serializer = UrlSerializer(saved_url)
                print(serializer.data['shortened_url'])
                shortened_url = serializer.data['shortened_url']
                return JsonResponse({'shortened_url': shortened_url})
            except Exception as e:
                print(e)
                return JsonResponse({'message': 'An error occured while saving url'})
    return JsonResponse({'encode': 'something'})

def decode(request):
    if request.method == 'POST':
        shortened_url = request.POST.get('shortened_url')
        if shortened_url:
            try:
                found_url = Url.objects.get(shortened_url = shortened_url)
                # print(found_url)
                serializer = UrlSerializer(found_url)
                # print(serializer.data)
                original_url = serializer.data['original_url']
                return JsonResponse({'original_url': original_url})
            except Exception as e:
                print(e)
                return JsonResponse({'message': 'An error occured while searching for an url'})
    return JsonResponse({'decode': 'something'})