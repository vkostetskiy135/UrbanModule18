"""
URL configuration for UrbanDjango project.

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
from django.views.generic import TemplateView
from task2.views import func_template, ClassTemplate
from task3.views import main_page, cart_page, games_page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('func_template/', func_template),
    path('class_template/', TemplateView.as_view(template_name='class_template.html')),
    path('platform/', main_page, name='main_page'),
    path('platform/cart/', cart_page, name='cart_page'),
    path('platform/games/', games_page, name='games_page'),
]
