from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path("admin/", admin.site.urls),
    path("", include("updater.urls")),  # Manteniamo il routing della nostra app
]
