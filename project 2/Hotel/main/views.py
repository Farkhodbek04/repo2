from django.shortcuts import render
from .models import Hotels

def main(request):

    return render(request, 'index.html')

def blog(request):

    return render(request, 'blog.html')

def contact(request):

    return render(request, 'contact.html')

def hotel(request):
    hotels = Hotels.objects.all()
    

    return render(request, 'hotel.html', {'hotels':hotels})

def services(request):

    return render(request, 'services.html')


