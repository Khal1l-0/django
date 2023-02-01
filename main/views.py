from django.shortcuts import render, redirect
from .forms import FormApp
# Create your views here.
def index(request):
    error = ''
    if request.method == 'POST':
        form = FormApp(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank')
        else:
            error = 'Ошибка в форме'


    form = FormApp()
    data = {
        'form': form,
        'error': error
    }
    
    return render(request, 'main/index.html', data)

def thank(request):
    return render(request, 'main/thank.html')
# Create your views here.
