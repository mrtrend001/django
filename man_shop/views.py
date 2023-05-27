from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models
from . import forms


def cloth_view(request):
    cloth = models.Surv.objects.all()
    return render(request, 'man/cloth.html', {'cloth': cloth})


def cloth_detail_view(request, id):
    cloth_id = get_object_or_404(models.Surv, id=id)
    return render(request, 'man/cloth_detail.html', {'cloth_id': cloth_id})


def create_cloth_view(request):
    method = request.method
    if method == "POST":
        form = forms.ManShopForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Анкета добавлена')
    else:
        form = forms.ManShopForms()
    return render(request, 'crud/create_cloth.html', {"form": form})
            

