"""django_basic_template URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
{%- if cookiecutter.use_drf == 'y' %}
from rest_framework.authtoken.views import obtain_auth_token
{%- endif %}



urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),    
    
    path(settings.ADMIN_URL, admin.site.urls),
{%- if cookiecutter.use_drf == "y" %}
    path('api-auth/', include('rest_framework.urls')),
{%- endif %}    
]
{% if cookiecutter.use_drf == 'y' %}
# API URLS
urlpatterns += [
    # API base url
    path("api/", include("config.api_router")),
    # DRF auth token
    path("auth-token/", obtain_auth_token),
]
{%- endif %}


### include your apps urls below

urlpatterns += [
    path("__debug__/", include("debug_toolbar.urls")),
#     path("<your_app_name>/", include("{{cookiecutter.project_name}}.<your_app_name>.urls", namespace="<your_app_name>")),    
]

