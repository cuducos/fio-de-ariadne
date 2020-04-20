from django.urls import include, path

from web.api.views import KidResource


app_name = "api"
urlpatterns = [path("kid/", include(KidResource.urls()))]
