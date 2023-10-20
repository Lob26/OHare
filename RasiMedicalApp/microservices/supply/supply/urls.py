"""
URL configuration for supply project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('supply/admin/', admin.site.urls),
    path('supply/', views.home, name='home'),
    path('supply/create_supply_form/', views.create_supply_form, name='create_supply_form'),
    re_path(r'^supplies/', views.list_supplies, name='list_supplies'),
    re_path(r'^create_supply/', csrf_exempt(views.create_supply), name='create_supply'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
