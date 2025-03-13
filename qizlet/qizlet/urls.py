"""
URL configuration for qizlet project.

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
import base.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name = 'index'),
    path('delete_module',views.delete_module,name = 'delete_module'),
    path('create_module',views.create_module, name='create_module'),
    path('edit_module',views.edit_module, name='edit_module'),
    path('start_test',views.start_test, name='start_test'),
    path('view_cards',views.view_cards, name='view_cards'),
]
