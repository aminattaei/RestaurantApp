from django.shortcuts import render
from .forms import reservationForm

def reserve(request):
    form=reservationForm()
    if request.method=='POST':
        form=reservationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=reservationForm()
    context={
        'form':form,
    }
    return render(request,'reserve/reservation.html',context)
            
