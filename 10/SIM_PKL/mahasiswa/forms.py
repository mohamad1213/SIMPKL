from django.forms import ModelForm
from bootstrap_datepicker_plus import DatePickerInput
from countable_field.widgets import CountableWidget
from crispy_forms.helper import FormHelper
from mitra.models import Mitra

from . import models

class PklForm(ModelForm):
    class Meta:
        model = models.Pkl
        exclude = ['owner', 'approve','catatan','reject']
        widgets = {
            'tanggal_mulai': DatePickerInput().start_of('event days'),
            'tanggal_selesai': DatePickerInput().end_of('event days'),
        }
class RejectForm(ModelForm):
    class Meta:
        model = models.Pkl
        exclude = ['owner', 'judul', 'nama_mitra', 'nama_dosen', 'tanggal_mulai', 'tanggal_selesai', 'approve']
        widgets = {
            'catatan': CountableWidget(attrs={'data-count': 'characters','data-max-count': 500, 'data-count-direction': 'down'}),                                            
        }