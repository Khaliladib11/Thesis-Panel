from django.shortcuts import render


# Create your views here.

def theses(request):
    theses = []
    context = {
        'theses': theses
    }
    return render(request, 'thesis/theses.html', context)
