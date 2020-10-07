from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from mitra.models import Mitra
from dosen.models import Dosen

class Pkl(models.Model):
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='mahasiswa')
    judul = models.CharField(max_length=255)
    nama_mitra = models.ForeignKey(Mitra, on_delete = models.DO_NOTHING)
    nama_dosen = models.ForeignKey(User, on_delete = models.DO_NOTHING, related_name='membimbing')
    tanggal_mulai = models.DateField(default=datetime.now)
    tanggal_selesai = models.DateField()
    approve = models.BooleanField(default=False)

    def tanggal_mulai_format(self):
        return self.tanggal_selesai.strftime('%Y-%m-%d')
    def tanggal_selesai_format(self):
        return self.tanggal_selesai.strftime('%Y-%m-%d')



