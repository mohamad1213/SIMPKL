from django.forms import ModelForm

from . import models

class MitraForm(ModelForm):
    class Meta :
        model = models.Mitra
        exclude=['owner']