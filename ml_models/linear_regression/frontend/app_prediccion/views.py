from django.shortcuts import render


def calculadora(request):
    return render(request, "app_prediccion/calculadora.html")
