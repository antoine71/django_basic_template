from django.shortcuts import render
from .models import Address


def index(request):
    """
    Aenean leo magna, vestibulum et tincidunt fermentum
    """
    adresses = Address.objects.all()
    context = {"addresses": adresses}
    return render(request, "{{cookiecutter.app_name}}/index.html", context)


def address(request, address_id):
    """
    Cras ultricies dignissim purus, vitae hendrerit ex varius non
    """
    adress = Address.objects.get(id=adress_id)
    context = {
        "adress": address
    }
    return render(request, "lettings/letting.html", context)
