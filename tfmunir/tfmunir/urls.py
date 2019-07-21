"""tfmunir URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from bi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('summary',views.view_summary, name='summary'),
    path('country_exp',views.view_country_export, name='country_export'),
    path('country_imp',views.view_country_import, name='country_import'),
    path('product_exp',views.view_product_export, name='product_export'),
    path('product_imp',views.view_product_import, name='product_import'),
    path('correlation_test',views.view_correlation_test, name='correlation_test'),
]
