from django.shortcuts import render, redirect
from .forms import BookingForm

def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('vehicle_list')
    else:
        form = BookingForm()
    return render(request, 'booking/create_booking.html', {'form': form})

from .models import Vehicle

def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'booking/vehicle_list.html', {'vehicles': vehicles})
