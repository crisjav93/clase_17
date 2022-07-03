from django.http import HttpResponse
import datetime
from django.template import Context, Template


def saludar(request):
    return HttpResponse ('Hola Mundo')

def segunda_vista(request):
    return HttpResponse ('Esta es la segunda vista')

def dia_de_hoy(request):
    dia = datetime.datetime.today()
    codigohtml='<h1>Hoy es: '+str(dia)+'</h1>' #esto es una cadena
    return HttpResponse(codigohtml)

def saludo_nombre(self, nombre):
    return HttpResponse('<h3>Hola, mi nombre es:'+nombre+'</h3>')

def calcula_ano_nacimiento(self,edad):
    return HttpResponse('<h1>Tu año de nacimiento es:'+str(int(datetime.datetime.now().year)-int(edad))+'</h1>') #lo tengo que concatenar antes(de int, a str)

def probando_template(self):
    mi_archivo = open('C:/Users/crisj/Desktop/Programación/clase_17/Proyecto_1/Plantillas/template1.html')
    plantilla = Template(mi_archivo.read()) #leemos el archivo
    mi_archivo.close() #cerramos el archivo

    contexto = Context() #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo

    documento = plantilla.render(contexto) #Aca renderizamos la plantilla en documento

    return HttpResponse(documento)