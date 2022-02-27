from django.shortcuts import render

def index(request):
    return render(request, 'card/index.html')

def create_set(request):
    return render(request, 'card/create_set.html')

def view_set(request):
    return render(request, 'card/view_set.html')