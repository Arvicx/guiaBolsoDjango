from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     return HttpResponse('<h1>SindApp</h1><p>Bem-vindo ao portal do associado!</p>')

def index(request):
    return render(request, 'associado/index.html')