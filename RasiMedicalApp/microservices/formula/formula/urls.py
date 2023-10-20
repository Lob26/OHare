"""
URL configuration for formula project.

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
from django.contrib import admin
from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('formula/admin/', admin.site.urls),
    path('formula/', views.home, name='home'),
    path('formula/create_formula_form/', views.create_formula_form, name='create_formula_form'),
    re_path(r'^formulas/', views.list_formulas, name='list_formulas'),
    re_path(r'^create_formula/', csrf_exempt(views.create_formula), name='create_formula'),
]
