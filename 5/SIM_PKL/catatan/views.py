
from django.shortcuts import render, redirect
from . import models, forms
# tasks : mengambil catatan berdasarkan user yang login
# jika user adalah staff maka ambil semua catatan 
def index(req):
    form_catatan = forms.CatatanForm()
    form_gambar = forms.GambarForm()
    if req.method == 'POST':
        form_catatan = forms.CatatanForm(req.POST)
        if form_catatan.is_valid():
            form_catatan.instance.owner=req.user
            form_catatan.save()
        images = []
        files = req.FILES.getlist('upload_img')
        for file in files:
            images.append(models.Gambar.objects.create(upload_img=file,catatan=form_catatan.instance))
        return redirect('/catatan/')

    tasks = models.Catatan.objects.filter(owner=req.user)
    group = req.user.groups.first()
    if group is not None and group.name == 'staf':
        tasks = models.Catatan.objects.all()
    return render(req, 'catatan/index.html',{
        'data': tasks,
        'form_catatan' : form_catatan,
        'form_gambar' : form_gambar,

    })
    
def new(req, *args, **kwargs):
    form_catatan = forms.CatatanForm()
    form_gambar = forms.GambarForm()
    if req.method == 'POST':
        form_catatan = forms.CatatanForm(req.POST)
        if form_catatan.is_valid():
            form_catatan.instance.owner=req.user
            form_catatan.save()
        images = []
        files = req.FILES.getlist('upload_img')
        for file in files:
            images.append(models.Gambar.objects.create(upload_img=file,catatan=form_catatan.instance))
        return redirect('/catatan/')
    return render(req, 'catatan/new.html',{
        'form_catatan' : form_catatan,
        'form_gambar' : form_gambar,
    })

def detail(req, id):
    task = models.Catatan.objects.filter(pk=id).first()
    return render(req, 'catatan/detail.html', {
        'data': task,
    })

def delete(req, id):
    models.Catatan.objects.filter(pk=id).delete()
    return redirect('/catatan/')

# def update(req, id):
#     if req.POST:
#         task = models.Catatan.objects.filter(pk=id).update(
#             tgl_kegiatan=req.POST['tgl_kegiatan'], 
#             judul=req.POST['judul'], 
#             ket=req.POST['ket'], 
#             upload_img=req.POST['upload_img'])
#         return redirect('/catatan/')

#     task = models.Catatan.objects.filter(pk=id).first()
#     return render(req, 'catatan/update.html', {
#         'data': task,
#     })

def index_dosen(req):

    group = req.user.groups.first() #mengambil group user
    catatans = models.Catatan.objects.all() # mengambil semua object yang ada di models Catatan
    if group is not None and group.name == 'dosen': # mendefinisikan bahwa ini adalah dosen
        catatans = models.Catatan.objects.filter(owner=req.user)
    return render(req, 'dosenah/index.html',{
        'data': catatans,
    })

def detail_dosen(req):

    group = req.user.groups.first() #mengambil group user
    catatans = models.Catatan.objects.all() # mengambil semua object yang ada di models Catatan
    if group is not None and group.name == 'dosen': # mendefinisikan bahwa ini adalah dosen
        catatans = models.Catatan.objects.filter(owner=req.user)
    return render(req, 'dosenah/index.html',{
        'data': catatans,
    })
