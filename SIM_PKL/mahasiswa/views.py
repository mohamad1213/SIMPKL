from django.shortcuts import render, redirect
from . import models, forms
from mitra.models import Mitra
from django.contrib import messages

def index(req):
    form_input = forms.PklForm()
    tasks = models.Pkl.objects.filter(owner=req.user)

    if req.POST:
        form_input = forms.PklForm(req.POST, req.FILES)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.save()
            messages.success(req, 'data successfully added')
        return redirect('/mahasiswa')
    group = req.user.groups.first()
    if group is not None and group.name == 'staf':
        tasks = models.Pkl.objects.all()
    return render(req, 'mahasiswa/index.html',{
        'data': tasks, 
        'form' : form_input,
    })

def detail(req, id):
    pkl = models.Pkl.objects.filter(pk=id).first()    
    return render(req, 'mahasiswa/detail.html', {
        'data': pkl,
    })

def delete(req, id):
    models.Pkl.objects.filter(pk=id).delete()
    return redirect('/mahasiswa')

def update(req, id):
    if req.POST:
        pkl = models.Pkl.objects.filter(pk=id).update(judul=req.POST['judul'], nama=req.POST['nama'], alamat=req.POST['alamat'], deskripsi=req.POST['deskripsi'], telp=req.POST['telp'])
        return redirect('/mahasiswa')

    pkl = models.Pkl.objects.filter(pk=id).first()    
    return render(req, 'mahasiswa/update.html', {
        'data': pkl,
    })
