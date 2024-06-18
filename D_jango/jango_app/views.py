from django.shortcuts import render
from .models import ChaiVariety, Store
from django.shortcuts import get_object_or_404
from .forms import ChaiVarietyForm
# Create your views here.

def all_jango(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'jango_app/all_jango.html', {'chais':chais})

def chai_description(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request,'jango_app/chai_details.html', {'chai': chai})

def chai_store(request):
    stores = None
    if request.method == 'POST':
        form = ChaiVarietyForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_variety']
            stores = Store.objects.filter(chai_varieties=chai_variety)
    else:
        form = ChaiVarietyForm()
    return render(request, 'jango_app/chai_store.html', {'stores': stores, 'form': form})