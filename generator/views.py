from django.shortcuts import render
import random


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = list('abcdefghijklmopqrstuvwxyz')
    length = int(request.GET.get('length', 8))
    thepassword = ''
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    for i in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': thepassword})


def rickrolled(request):
    return render(request, 'generator/rickrolled.html')