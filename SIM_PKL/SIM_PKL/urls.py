from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
    path('', include('home.urls')),
    # path('staf/', include('staf.urls')),
    path('catatan/', include('catatan.urls')),
    path('accounts/', include('accounts.urls')),
    path('mahasiswa/', include('mahasiswa.urls')),
    path('mitra/', include('mitra.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
