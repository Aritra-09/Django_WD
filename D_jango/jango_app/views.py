from django.shortcuts import render
from .models import ChaiVariety
from django.shortcuts import get_object_or_404
# Create your views here.

def all_jango(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'jango_app/all_jango.html', {'chais':chais})

def chai_description(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request,'jango_app/chai_details.html', {'chai': chai})