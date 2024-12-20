from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def home(request):
    return render(request, 'index.html')

def stats_data(request):
    # Example static data; in a real scenario, you’d query your models.
    data = {
        'labels': ['Team A', 'Team B', 'Team C'],
        'scores': [10, 20, 15]
    }
    return JsonResponse(data)