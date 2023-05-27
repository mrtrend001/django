from django import forms
from . import models


class ManShopForms(forms.ModelForm):
    class Meta:
        models = models.Surv
        fields = "__all__"
        #fields = "title description image"



