from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import place
from .models import human


def home(request):
    obj = place.objects.all()
    obj1 = human.objects.all()
    return render(request, 'index.html', {'result': obj, 'result1': obj1})


def about(request):
    return render(request, 'about.html')
#
# def contact(request):
#     return render(request, 'contact.html')
#
#
# def booking(request):
#     return HttpResponse("Booking")
#
#
# def addition(request):
#     x = int(request.GET['number1'])
#     y = int(request.GET['number2'])
#     a = x + y
#     s = x - y
#     m = x * y
#     d = x / y
#     dict = {'number1': x, 'number2': y, 'addition': a, 'sub': s, 'mul': m, 'div': d}
#     return render(request, 'contact.html', dict)
