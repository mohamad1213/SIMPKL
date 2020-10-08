from django.db import models
from django.contrib.auth.models import User
# from mahasiswa.models import Pkl

class Dosen(models.Model):
    nama_dosen = models.CharField(max_length=100)
    nip = models.CharField(max_length=100)
    fakultas = models.CharField(max_length=100)
    jurusan = models.CharField(max_length=100)
    def __str__(self):
        return self.nama_dosen    