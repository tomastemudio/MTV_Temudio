from django.http import HttpResponse
from django.template import Context, loader, Template
import datetime

from home.models import Familiar

def crear_familiar(request):

    familiar1 = Familiar(nombre = 'Silvana', apellido = 'Monteforte', edad = 54, fecha_nacimiento =datetime.datetime(1968,3,21,0,0,0), fav_color = 'Verde', fav_animal = 'Perro')
    familiar2 = Familiar(nombre = 'Gustavo', apellido = 'Temudio', edad = 57, fecha_nacimiento =datetime.datetime(1964,12,29,13,22,0), fav_color = 'Negro', fav_animal = 'Gato')
    familiar3 = Familiar(nombre = 'Maia', apellido = 'Temudio', edad = 14, fecha_nacimiento =datetime.datetime(2008,4,15,11,44,0), fav_color = 'Violeta', fav_animal = 'Perro')
    familiar4 = Familiar(nombre = 'Pascuala', apellido = 'Rapanaro', edad = 77, fecha_nacimiento =datetime.datetime(1945,11,29,22,17,0), fav_color = 'Azul', fav_animal = 'Leon')
    familiar5 = Familiar(nombre = 'Tomás', apellido = 'Temudio', edad = 21, fecha_nacimiento =datetime.datetime(2001,10,3,17,52,0), fav_color = 'Azul', fav_animal = 'Elefante')
    familiar1.save()
    familiar2.save()
    familiar3.save()
    familiar4.save()
    familiar5.save()
    
    template = loader.get_template('crear_familiar.html')
    template_renderizado = template.render({})

    return HttpResponse(template_renderizado)

def ver_familiares(request):
    
    familiares = Familiar.objects.all()

    template = loader.get_template('ver_familiares.html')
    template_renderizado = template.render({'familiares': familiares})

    return HttpResponse(template_renderizado)