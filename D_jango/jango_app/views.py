from django.shortcuts import render

# Create your views here.

def all_jango(request):
    return render(request, 'jango_app/all_jango.html')

