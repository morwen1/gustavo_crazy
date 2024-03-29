"""gustavo_crazy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path , include
from apps.api_users import urls as urls_api
from apps.monolitic_page import urls as urls_site
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', include(urls_site)), #landing page
    path('admin/', admin.site.urls),#admin page
    path('api/v1/',include(urls_api)),#public api
    path('chat/', include('apps.chat.urls')), #testing realtime chat
]