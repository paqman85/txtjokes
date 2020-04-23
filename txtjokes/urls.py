from django.conf import settings
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('txt-jokes-administratus/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('pages.urls')),
]
