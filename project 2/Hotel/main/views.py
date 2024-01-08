from django.shortcuts import render

def main(request):

    return render(request, 'index.html')

def blog(request):

    return render(request, 'blog.html')

def contact(request):

    return render(request, 'contact.html')

def hotel(request):

    return render(request, 'hotel.html')

def services(request):

    return render(request, 'services.html')


