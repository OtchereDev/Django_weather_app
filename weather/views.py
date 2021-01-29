from django.shortcuts import render
from .forms import searchForm


def home(request):
    form=searchForm(request.POST or None)

    context={
        'form':form
    }
    
    if form.is_valid():
        print('yes',request.POST.get('location'))
    else:
        print('no')

    return render(request,'weather_app/index.html',context)