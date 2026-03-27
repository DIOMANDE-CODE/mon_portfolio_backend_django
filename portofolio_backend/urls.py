from django.contrib import admin
from django.urls import path, include
from contact.views import acceuil

urlpatterns = [
    path("gestion-portofolio/", admin.site.urls),
    path("admin/", include("admin_honeypot.urls", namespace="admin_honeypot")),
    path("users/", include(("users.urls", "users"), namespace="users")),
    path("projet/", include(("projets.urls", "projets"), namespace="projets")),
    path("contact/", include(("contact.urls", "contact"), namespace="contact")),
    path("", acceuil, name="acceuil"),
]
