from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    text = {
        'name': "Pouriya Tajik",
        'age': 30,
        'phone': 4654646,
        'friend_name': ['kazi', 'ariyan', 'udemy', 'raju']
    }
    return render(request, "index.html", text)


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
