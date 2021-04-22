from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def window_view(request):
    return render(request, 'window_view')