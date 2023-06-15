from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Articulo

# Create your views here.
layout = """
<h1> Proyecto Web (LP3) | Juan Montesinos </h1>
<hr/>
<ul>
<li>
<a href="/inicio"> Inicio</a>
</li>
<li>
<a href="/saludo"> Mensaje de Saludo</a>
</li>
<li>
<a href="/rango"> Mostrar Números [a,b]</a>
</li>
<li>
<a href="/rango2/10/15"> Mostrar Números [10,15]</a>
</li>
</ul>

<hr/>
"""
def index(request):
    return render(request,'index.html')

def saludo(request):
    return render(request,'saludo.html')

def rango(request):
    a = 10
    b = 20
    rango_numeros = range(a,b+1)
    return render(request,'rango.html',{
'titulo':'Rango',
'a':a,
'b':b,
'rango_numeros':rango_numeros
})

def rango2(request,a=40,b=10):
    if a>b:
        return redirect('rango2',a=b, b=a)
    resultado = f"""
<h2> Números de [{a},{b}] </h2>
"""
    while a<=b:
        resultado += f"<li> {a} </li>"
        a+=1
    resultado += "</ul"
    return HttpResponse(layout + resultado)


def index(request):
    return render(request,'index.html', {
    'titulo':'Inicio',
    'mensaje':'Proyecto web con DJango (Desde el View)'
})

def saludo(request):
    return render(request,'saludo.html',{
    'titulo':'Saludo',
    'autor_saludo':'Anthony Gabriel Bailon Villugas'
})

def index(request):
    return render(request,'index.html', {
    'titulo':'Inicio',
})


def index(request):
    estudiantes = [ 'Isabella Caballero',
'Alejandro Hermitaño',
'Joan Palomino',
'Pierre Bernaola',
'Danne Barzola']

    return render(request,'index.html', {
'titulo':'Inicio',
'mensaje':'Proyecto Web Con DJango',
'estudiantes': estudiantes
})

def crear_articulo(request,titulo, contenido, publicado):
    articulo = Articulo(
        titulo = titulo,
        contenido = contenido,
        publicado = publicado
    )
    articulo.save()
    return HttpResponse(f"Articulo Creado: {articulo.titulo} - {articulo.contenido}")