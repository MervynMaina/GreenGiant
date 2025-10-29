from django.shortcuts import render
from logisticsapp.models import *
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def quote(request):
    if request.method == "POST":
        myquote = Quote(
            city_departure = request.POST['departure'],
            delivery_city = request.POST['delivery'],
            total_weight = request.POST['weight'],
            dimension = request.POST['dimensions'],
            shipment_type = request.POST['shipment_type'],
            urgency_level = request.POST['urgency'],
            fullname = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            additional_info = request.POST['message'],
        )
        myquote.save()
        messages.success(request, 'Your quotation is being processed!')
        return redirect('/quote')

    else:
        messages.error(request, 'Unable to get a quote!.')
        return render(request, 'get-a-quote.html')
def pricing(request):
    return render(request, 'pricing.html')

def servicedetails(request):
    return render(request, 'service-details.html')

def services(request):
    return render(request, 'services.html')

def starter(request):
    return render(request, 'starter-page.html')