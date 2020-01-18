"""startup_go_auth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from apps.users.views import get_public_key

urlpatterns = [
    path("admin/", admin.site.urls),
    path("o/", include("apps.oauth2.urls", namespace="oauth2_jwt")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("public_key.json", get_public_key, name="get_public_key"),
]
