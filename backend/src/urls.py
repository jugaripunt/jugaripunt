"""
URL configuration for src project.

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
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from django.http import HttpResponse, JsonResponse # type: ignore

# Vista simple para la página de bienvenida
def welcome_view(request):
    return HttpResponse("¡Bienvenido a Django!")

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el admin
    path('', welcome_view, name='welcome'),  # Ruta para la página de bienvenida
    path('api/', include('jugaripunt.urls')),  # Incluye las URLs de tu app jugador
]
