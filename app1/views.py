from django.shortcuts import render

# Create your views here.


def dhoni(request):
    return render(request,'dhoni.html')

def rohit(request):
    return render(request,'rohit.html')