import os
import django
from datetime import date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "raiz.settings")  # Ajusta se for 'solar_django.settings'
django.setup()
from app.models import Celular

Celular.objects.all().delete()

Celular.objects.create(
    nome='iphone x',
    preco=1200,
    modelo='x',
    descricao='celular iphone x',
    marca='iphone',
)


