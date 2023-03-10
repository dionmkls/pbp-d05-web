"""PBP_D5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path, include
from beranda.views import index 
from faq.views import MainView, PostJsonListView, add_faq, get_flutter

import beranda.urls as index_urls
import vaksin.urls as vaksin_urls
import apd.urls as apd_urls
from faq.views import MainView, PostJsonListView
# import forum.urls as forum_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("index/", include(index_urls)),
    re_path(r"^$", index, name="index"),
    path('lokasi-vaksin/', include(vaksin_urls)),
    path('beranda/', include('beranda.urls')),
    path('apd/', include(apd_urls)),
    path('faq/', MainView.as_view(), name='main-view'),
    path('faqs-json/<int:num_posts>/', PostJsonListView.as_view(), name='faqs-json-view'),
    path('faq/add-faq', add_faq, name='add_faq'),
    path('forum/', include('forum.urls')),
    path('rumah-sakit/', include('rumah_sakit.urls')),
    path('tempat-oksigen/', include('oksigen.urls')),
    path('tempat-oksigen/json', include('oksigen.urls')),
    path('get-flutter', get_flutter, name='get_flutter')
]
