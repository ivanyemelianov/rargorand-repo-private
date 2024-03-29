"""rargorand URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path

from accounts.views import (
    login_view,
    logout_view,
    register_view
)
from drops.views import schedule_view
from nftcollections.views import all_collections_view
from search.views import search_view
from .views import home_view

urlpatterns = [
    path('', home_view),
    path('schedule/', schedule_view, name='schedule'),
    path('allcollections/', all_collections_view, name='collections'),
    path('library/nftcollections/', include('nftcollections.urls')),
    path('library/collections/', include('ncollections.urls')),
    path('calendar/drops/', include('drops.urls')),
    path('search/', search_view, name='search'),
    path('admin/', admin.site.urls),
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
]
