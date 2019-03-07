from django.shortcuts import render

# Create your views here.
def header(request):
    return render(request, 'fw/base.html', {})


def index(request):
    return render(request, 'fw/index.html', {})

def ticket(request):
    return render(request, 'fw/ticket.html', {})