from django.shortcuts import get_object_or_404, redirect, render

from .forms import PersonForm, Triangle
from .models import Person


def triangle(request):
    hypotenuse = None
    if 'submit' in request.GET:
        form = Triangle(request.GET)
        if form.is_valid():
            hypotenuse = (form.cleaned_data.get('cathetus_1')**2 + form.cleaned_data.get('cathetus_2')**2)**0.5
            return render(request, 'triangle.html', {'hypotenuse': hypotenuse})
    else:
        form = Triangle()
    return render(request, 'triangle.html', {'form': form})


def person_create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog:person_create')
    else:
        form = PersonForm()
    return render(request, 'create_person.html', {"form": form})


def person_update(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            obj = form.save()
            return redirect('catalog:person_update', obj.id)
    else:
        form = PersonForm(instance=person)
    return render(request, 'update_person.html', {'form': form})
