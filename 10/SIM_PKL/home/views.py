from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from mahasiswa.models import Pkl
from catatan import models, forms
from forum.models import Forum

def index(req):
    group = req.user.groups.first()
    tasks = models.Catatan.objects.filter(owner=req.user)
    form_catatan = forms.CatatanForm()
    form_gambar = forms.GambarForm()
    # forum = models.Forum.objects.all()

    if req.method == 'POST':
        form_catatan = forms.CatatanForm(req.POST)
        if form_catatan.is_valid():
            form_catatan.instance.owner=req.user
            form_catatan.save()
        images = []
        files = req.FILES.getlist('upload_img')
        for file in files:
            images.append(models.Gambar.objects.create(upload_img=file,catatan=form_catatan.instance))
        return redirect('/')

    if group is not None and group.name == 'dosen':
        return render(req, 'dosen/index.html')
    elif group is not None and group.name == 'staf':
        tasks = models.Catatan.objects.all()
        return render(req, 'staf/index.html')
    else:
        return render(req, 'home/index.html', {
            'data': tasks,
            'form_catatan' : form_catatan,
            'form_gambar' : form_gambar,
            # 'forum': forum,
        })
        
    return render(req, 'staf/index.html')

def delete_catatan(req, id):
    models.Catatan.objects.filter(pk=id).delete()
    return redirect('/')

def cetak(req):
    cetak = models.Catatan.objects.all()
    return render(req, 'home/cetak.html', {
        'cetak' : cetak,
    })
