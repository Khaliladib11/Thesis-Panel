from django.shortcuts import render
from .models import Person, Student, Supervisor, Field, Course, Thesis


# Get all Theses
def theses(request):
    theses = Thesis.objects.all()
    context = {
        'theses': theses
    }
    return render(request, 'thesis/theses.html', context)


# Get one Thesis by its id
def thesis(request, pk):
    thesis = Thesis.objects.get(tid=pk)
    context = {
        'thesis': thesis
    }
    return render(request, 'thesis/thesis.html', context)
