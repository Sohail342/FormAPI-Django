from django.shortcuts import render
from .form import RegForm


def formAPI(request):
    if request.method == "POST":
        form = RegForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirmPassword = form.cleaned_data['confirmPassword']
    else:
        form = RegForm()
    return render(request, 'core/index.html', {'form':form})