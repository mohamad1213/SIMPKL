from django.forms import ModelForm
from mitra.models import Mitra
# from bootstrap_modal_forms.forms import BSModalModelForm 

from . import models

class PklForm(ModelForm):
    class Meta:
        model = models.Pkl
        exclude = ['owner']
        # fields = ['judul']