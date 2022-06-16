from django.urls import path

from .views import index, address


app_name = "{{cookiecutter.app_name}}"
urlpatterns = [
    path("", index, name="index"),
    path("<int:address_id>/", address, name="address"),
]
