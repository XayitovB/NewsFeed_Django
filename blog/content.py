import requests
from .models import Category

def valyuta(request):
    req = requests.get("https://cbu.uz/ru/arkhiv-kursov-valyut/json/")
    response = req.json()
    context = {
        "valyutalar": response,
        "categories": Category.objects.all()

    }
    return context