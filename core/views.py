from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')


def about(requset):
    return render(requset, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def magazine_list(request):
    return render(request, 'autopart-magazine-list.html')
