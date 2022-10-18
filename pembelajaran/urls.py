"""pembelajaran URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from evaluasi.views import evaluasi
from home.views import home
from materi.views import materi
from pecahandesimal.views import pecahandesimal
from pecahanoperasi.views import pecahanoperasi
from pecahanpengurangan.views import pecahanpengurangan
from pecahanpenjumlahan.views import pecahanpenjumlahan
from pecahansenilai.views import pecahansenilai
from profil.views import profil
from video.views import video

urlpatterns = [
    path('admin/', admin.site.urls),
    path('evaluasi/', evaluasi),
    path('home/', home),
    path('materi/', materi),
    path('pecahandesimal/', pecahandesimal),
    path('pecahanoperasi/', pecahanoperasi),
    path('pecahanpengurangan/', pecahanpengurangan),
    path('pecahanpenjumlahan/', pecahanpenjumlahan),
    path('pecahansenilai/', pecahansenilai),
    path('profil/', profil),
    path('video/', video),
]
