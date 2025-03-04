from django.urls import path
from .views import home, update_email, update_gmb, update_poi, daily_check

urlpatterns = [
    path("", home, name="home"),
    path("update-email/", update_email, name="update_email"),
    path("update-gmb/", update_gmb, name="update_gmb"),
    path("update-poi/", update_poi, name="update_poi"),
   # path("update_mainbrand/", update_mainbrand, name="update_mainbrand"),
    path("daily-check/", daily_check, name="daily_check"),
]
