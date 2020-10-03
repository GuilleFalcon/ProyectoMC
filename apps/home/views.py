from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def home(request):
    current_user = request.user
    context = {
        "current_user" : current_user
    }
    return render(request, 'base.html', context)

def info(request):
    current_user = request.user

    context = {
        "current_user" : current_user
    }
    return render(request, 'info.html', context)

def servidor(request):
    current_user = request.user
    resp = requests.get('http://localhost:8000/graft/?query=query{estado}')
    if (resp.status_code != 200):
        return render(request, 'error.html')
    else:
        js = resp.json()
        status = js["data"]["estado"]
        context = {
            "current_user" : current_user,
            "status" : status
        }
        return render(request, 'servidor.html', context)  

#Ejemplos de consultas y post

#def prender(request):
#    resp = requests.post('http://127.0.0.1:8000/graft/?query=mutation {prender{estado}}')
#    return HttpResponse(resp)

#def apagar(request):
#    resp = requests.post('http://127.0.0.1:8000/graft/?query=mutation {apagar{estado}}')
#    return HttpResponse(resp)

#def estado(request):
#    resp = requests.get('http://127.0.0.1:8000/graft/?query=query{estado}')
#    return HttpResponse(resp)