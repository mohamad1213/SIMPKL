from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Forum(models.Model):
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='forum')
    nama_mitra = models.CharField( max_length=255)
    alamat = models.CharField( max_length=255)
    deskripsi = models.TextField(default='')
    pic = models.CharField( max_length=255)
    telp = models.CharField(max_length=255)
    def __str__(self):
        return self.nama_mitra

class Posting(models.Model):
    forum = models.ForeignKey(Forum, on_delete = models.DO_NOTHING,related_name='posting')
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='owner')
    waktu = models.DateTimeField(default=datetime.now)
    desc = models.CharField(max_length=2000)

class Komen(models.Model):
    posting = models.ForeignKey(Posting, on_delete = models.CASCADE,related_name='komentar')
    pengguna = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='pengguna')
    waktu = models.DateTimeField(default=datetime.now)
    komentar = models.CharField(max_length=100)

class Balas(models.Model):
    komen = models.ForeignKey(Komen, on_delete = models.DO_NOTHING,related_name='balasan')
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING,related_name='user')
    waktu = models.DateTimeField(default=datetime.now)
    balasan = models.TextField()


