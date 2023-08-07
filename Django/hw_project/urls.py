
from django.contrib import admin
from django.urls import path, include

from quotes.views import main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quotes.urls')),
    path('users/', include('users.urls')),
    path('', main, name='index'),
]
