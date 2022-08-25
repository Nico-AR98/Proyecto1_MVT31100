from django.shortcuts import render,HttpResponse
from django.template import loader #Importamos el cargador
from familia.models import Familiar

# Create your views here.

def familia(request):
    familiar_1 = Familiar(nombre='Maximiliano',apellido='Viltre',edad=37, fecha_nacimiento='1985-06-26')
    familiar_1.save()

    familiar_2 = Familiar(nombre='Martin',apellido='Viltre',edad=35, fecha_nacimiento='1987-03-01')
    familiar_2.save()

    familiar_3 = Familiar(nombre='David',apellido='Viltre',edad=32, fecha_nacimiento='1989-05-02')
    familiar_3.save()


    plantilla = loader.get_template('template_1.html')

    familiares = {'familiares':[familiar_1,familiar_2,familiar_3]}

    documento = plantilla.render(familiares)

    return HttpResponse(documento)







