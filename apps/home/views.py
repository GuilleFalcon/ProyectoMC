from django.shortcuts import render

# Create your views here.
def home(request):
    current_user = request.user
    context = {
        "current_user" : current_user
    }
    return render(request, 'index.html', context)

def info(request):
    current_user = request.user
    context = {
        "current_user" : current_user
    }
    return render(request, 'info.html', context)