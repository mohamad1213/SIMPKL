from django.shortcuts import render
from django.contrib.auth import get_user_model

def index(req):
    
    group = req.user.groups.first()
    if group is not None and group.name == 'dosen':
        return render(req, 'dosen/index.html')
    elif group is not None and group.name == 'staf':
        return render(req, 'staf/index.html')
    else:
        return render(req, 'home/index.html')

