from django.shortcuts import render, redirect
from . import models, forms
from dosen import models as dosen_models
from mitra.models import Mitra
from catatan.models import Catatan
from bootstrap_datepicker_plus import DatePickerInput
from django.contrib import messages

def index(req):

    tasks_approved = models.Pkl.objects.filter(owner=req.user,approve=True).first()
    tasks = models.Pkl.objects.filter(owner=req.user)
    # ambil tanggal mulai 
    # tanggal mulai ditamnah 3 bulan 
    # ambil tanggal selesai
    # checked pake if apakah tanggal selesai lebih dari hasil dari tanggal yang ditentukan

    # untuk menentukan kapan mulainya maka harus ada pengecekan di bagian home
    form_input = forms.PklForm()

    if req.POST:
        form_input = forms.PklForm(req.POST, req.FILES)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.save()
            messages.success(req, 'Data telah ditambahkan.')
            return redirect('/mahasiswa')
        else:
            messages.danger(req, 'A problem has been occurred while submitting your data.')


    # group = req.user.groups.first()
    # if group is not None and group.name == 'staf':
    #     tasks = models.Pkl.objects.all()
    return render(req, 'mahasiswa/index.html',{
        'form' : form_input,
        'data': tasks,
        'data_approved': tasks_approved,
    })
    

def index_staf(req):
    tasks = models.Pkl.objects.filter(owner=req.user)
    form_input = forms.PklForm()
    
    if req.POST:
        form_input = forms.PklForm(req.POST, req.FILES)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.save()
            messages.success(req, 'Data telah ditambahkan.')
        return redirect('/mahasiswas')
        

    group = req.user.groups.first()
    if group is not None and group.name == 'staf':
        tasks = models.Pkl.objects.all()
    return render(req, 'mahasiswas/index.html',{
        'data': tasks,  
    })


def input(req):
    form_input = forms.PklForm()

    if req.POST:
        form_input = forms.PklForm(req.POST, req.FILES)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.save()
        return redirect('/mahasiswa')
        
    mitra = Mitra.objects.first()
    return render(req, 'mahasiswa/input.html', {
        'form' : form_input,
        'd': mitra,
    })

def input_staf(req):
    form_input = forms.PklForm()

    if req.POST:
        form_input = forms.PklForm(req.POST, req.FILES)
        if form_input.is_valid():
            form_input.instance.owner = req.user
            form_input.save()
        return redirect('/mahasiswas')
        
    mitra = Mitra.objects.first()
    return render(req, 'mahasiswas/input.html', {
        'form' : form_input,
        'd': mitra,
    })


def detail(req, id):
    pkl = models.Pkl.objects.filter(pk=id).first()    
    return render(req, 'mahasiswa/detail.html', {
        'data': pkl,
    })

def detail_staf(req, id):
    pkl = models.Pkl.objects.filter(pk=id).first()    
    return render(req, 'mahasiswas/detail.html', {
        'data': pkl,
    })


def delete(req, id):
    models.Pkl.objects.filter(pk=id).delete()
    messages.success(req, 'data telah di hapus.')
    return redirect('/mahasiswa')

def delete_staf(req, id):
    models.Pkl.objects.filter(pk=id).delete()
    messages.success(req, 'data telah di hapus.')
    return redirect('/mahasiswas')


def update(req, id):
    widgets = {
        'tanggal_mulai': DatePickerInput(),
        'tanggal_selesai': DatePickerInput(),
    }
    
    if req.POST:
        pkl = models.Pkl.objects.filter(pk=id).update(
            judul=req.POST['judul'], 
            nama_dosen=req.POST['nama_dosen'], 
            tanggal_mulai=req.POST['tanggal_mulai'], 
            tanggal_selesai=req.POST['tanggal_selesai'])
        messages.info(req, 'data telah di perbarui.')
        return redirect('/mahasiswa')

    pkl = models.Pkl.objects.filter(pk=id).first()    
    return render(req, 'mahasiswa/update.html', {
        'data': pkl,
    })

def update_staf(req, id):
    widgets = {
        'tanggal_mulai': DatePickerInput(),
        'tanggal_selesai': DatePickerInput(),
    }
    if req.POST:
        pkl = models.Pkl.objects.filter(pk=id).update(
            judul=req.POST['judul'], 
            nama_dosen=req.POST['nama_dosen'], 
            tanggal_mulai=req.POST['tanggal_mulai'], 
            tanggal_selesai=req.POST['tanggal_selesai'])
        return redirect('/mahasiswas')

    pkl = models.Pkl.objects.filter(pk=id).first()    
    return render(req, 'mahasiswas/update.html', {
        'data': pkl,
    })

def approve(req, id):
    a = models.Pkl.objects.filter(pk=id).update(approve=True)
    return redirect('/mahasiswas')

def approve_batal(req, id):
    a = models.Pkl.objects.filter(pk=id).update(approve=False)
    return redirect('/mahasiswas')

def index_dosen(req):
    group = req.user.groups.first() #mengambil group user
    tasks = models.Pkl.objects.all() # mengambil semua object yang ada di models pkl
    if group is not None and group.name == 'dosen': # mendefinisikan bahwa ini adalah dosen
        pkls = models.Pkl.objects.filter(nama_dosen=req.user) # memfilter bahwa satu mahasiswa hanya boleh menginputkan satu dosen
    return render(req, 'dosenah/index.html',{
        'data': pkls,
    })

def detail_dosen(req, id):
    pkl = models.Pkl.objects.filter(pk=id).first()
    catatans = Catatan.objects.filter(owner=pkl.owner) # mengambil semua object yang ada di models Catatan
    return render(req, 'dosenah/detail.html',{
        'data': catatans,
    })