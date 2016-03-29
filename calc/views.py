from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sumar(request, num1, num2):
    return HttpResponse(num1 + ' + ' + num2 + ' = ' + str(int(num1) + int(num2)))

def restar(request, num1, num2):
    return HttpResponse(num1 + ' - ' + num2 + ' = ' + str(int(num1) - int(num2)))

def multiplicar(request, num1, num2):
    return HttpResponse(num1 + ' * ' + num2 + ' = ' + str(int(num1) * int(num2)))

def dividir(request, num1, num2):
    try:
        return HttpResponse(num1 + ' / ' + num2 + ' = ' + str(int(num1) / int(num2)))
    except:
        return HttpResponse('Estas intentando dividir entre 0')

def NotFound(request):
    return HttpResponse('<h3>No existe la operacion que solicitas</h3>')
