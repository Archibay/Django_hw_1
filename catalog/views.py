from django.shortcuts import render

from .forms import Triangle


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
