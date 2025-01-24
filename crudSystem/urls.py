"""
URL configuration for crudSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import views as denis_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', denis_views.home, name='home-url'),
    path('register_members/', denis_views.register_members, name='register_members-url'),
    path('all_members/', denis_views.all_members, name='all_members-url'),

    path('delete/<id>', denis_views.delete_member, name='delete-url'),
]
