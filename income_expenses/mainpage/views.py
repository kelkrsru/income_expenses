from django.shortcuts import render


def index(request):
    template = 'mainpage/index.html'
    return render(request, template)
