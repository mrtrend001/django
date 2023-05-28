from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models
from . import forms


def cloth_view(request):
    cloth = models.Surv.objects.all()
    return render(request, 'man/cloth.html', {'cloth': cloth})


def cloth_detail_view(request, id):
    cloth_view
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
            

def delete_cloth_view(request, id):
    cloth_id = get_object_or_404(models.Surv, id=id)
    cloth_id.delete()
    return HttpResponse('анкета удалена')


def update_cloth_view(request, id):
    cloth_id = get_object_or_404(models.Surv, id=id)
    if request.method == "POST":
        form = forms.ManShopForms(instance=cloth_id, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Данные обновлены')
    else:
        form = forms.ManShopForms(instance=cloth_id)
    context = {
        "form": form,
        "cloth_id": cloth_id
    }
    return render(request, "crud/update_cloth.html", context)
