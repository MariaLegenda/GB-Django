from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'mainapp/main.html')

def products(request):
    return render(request, 'mainapp/product.html')

def contacts(request):
    return render(request, 'mainapp/contacts.html')
