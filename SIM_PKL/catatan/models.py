from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Catatan(models.Model):
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='catatan')
    tgl_kegiatan = models.DateField(default=datetime.now)
    judul = models.CharField(max_length=100)
    ket = models.TextField(max_length=200)
    upload_img = models.ImageField(default='', upload_to='images/')
    

