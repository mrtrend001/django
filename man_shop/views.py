from django.shortcuts import render, get_object_or_404
from . import models


def cloth_view(request):
    cloth = models.Surv.objects.all()
    return render(request, 'man/cloth.html', {'cloth': cloth})


def cloth_detail_view(request, id):
    cloth_id = get_object_or_404(models.Surv, id=id)
    return render(request, 'man/cloth_detail.html', {'cloth_id': cloth_id})
