import gamelib
import logica
from pila import *

def main():
    gamelib.title("AlgoPaint")
    gamelib.resize(345, 545)
    tecla, color, nuevo_color, modo = 1, None, None, 'lapiz'       # Empieza con el color negro elegido y en modo 'lapiz'
    pixeles = 20
    pila_deshacer, pila_rehacer = Pila(), Pila()
    primera_version = {}

    paint = logica.paint_nuevo()
    logica.paint_mostrar(paint, tecla, pixeles, nuevo_color, modo)


    while gamelib.is_alive():

        ev = gamelib.wait()
        if not ev:
            break

        if ev.type == gamelib.EventType.ButtonPress and ev.mouse_button == 1:
            if 5 < ev.x < 340 and 5 < ev.y < 340:
                if nuevo_color:                     # Color ingresado por el usuario
                    color = nuevo_color
                else:
                    color = logica.elegir_color(tecla)  # Color elegido dentro de los predeterminados

                if modo == 'lapiz':
                    if color == '#ffffff':
                        logica.borrar(paint, ev.x, ev.y, pixeles)
                    elif color:
                        logica.pintar(paint, ev.x, ev.y, pixeles, color)
                else:
                    try:
                        logica.balde(paint, ev.x, ev.y, pixeles, color)
                    except RecursionError:
                        gamelib.say('Ocurrió un error, se pintará el área que sea posible. Disculpe las molestias ocasionadas :(')


        elif ev.type == gamelib.EventType.Motion:
            if 5 < ev.x < 340 and 5 < ev.y < 340:
                if color is None:       # Si no hay color, no pinta
                    continue
                if color == '#ffffff':
                    logica.borrar(paint, ev.x, ev.y, pixeles)
                else:
                    logica.pintar(paint, ev.x, ev.y, pixeles, color)


        elif ev.type == gamelib.EventType.ButtonRelease and ev.mouse_button == 1:
            color = None                 # Al dejar de apretar el mouse, deja de pintar
            if 5 < ev.x < 340 and 5 < ev.y < 340:
                pila_rehacer = Pila()
                pila_deshacer.apilar(logica.copiar_diccionario(paint))


        elif ev.type == gamelib.EventType.KeyPress:
            # Eleccion de color
            if ev.key.isdigit():
                if ev.key in ('1', '2', '3', '4', '5', '6', '7'):
                    tecla = int(ev.key)
                    nuevo_color = None

            # Creacion de color
            elif ev.key.lower() == 'c':
                nuevo = logica.crear_color()

                if nuevo is not None:
                    nuevo_color = nuevo
                    tecla = ev.key

            # Borrado
            elif ev.key.lower() == 'n':
                dibujo_nuevo = logica.crear_hoja()
                if dibujo_nuevo is not None:
                    paint = dibujo_nuevo
                pila_deshacer = Pila()
                pila_rehacer = Pila()
                primera_version = {}

            # Guardado de ppm
            elif ev.key.lower() == 'g':
                logica.guardar_ppm(paint, pixeles)

            # Apertura de ppm
            elif ev.key.lower() == 'a':
                try:
                    nuevo, dimension = logica.abrir_ppm()
                    if nuevo is not None:
                        pixeles = int(dimension)
                        paint = nuevo
                        pila_deshacer, pila_rehacer = Pila(), Pila()
                        primera_version = logica.copiar_diccionario(paint)
                except UnicodeDecodeError:
                    gamelib.say('El archivo que desea abrir no es compatible')

            # Guardado de png
            elif ev.key.lower() == 'p':
                logica.guardar_png(paint, pixeles)

            # Pintar con balde
            elif ev.key.lower() == 'b':
                modo = 'balde'

            # Pintar con lapiz
            elif ev.key.lower() == 'l':
                modo = 'lapiz'

            # Deshacer
            elif ev.key == 'Left':
                if pila_deshacer.esta_vacia():
                    continue

                pila_rehacer.apilar(pila_deshacer.desapilar())
                if not pila_deshacer.esta_vacia():
                    paint = logica.copiar_diccionario(pila_deshacer.ver_tope())
                else:
                    paint = logica.copiar_diccionario(primera_version)

            # Rehacer
            elif ev.key == 'Right':
                if pila_rehacer.esta_vacia():
                    continue

                pila_deshacer.apilar(pila_rehacer.desapilar())
                paint = logica.copiar_diccionario(pila_deshacer.ver_tope())


        logica.paint_mostrar(paint, tecla, pixeles, nuevo_color, modo)

gamelib.init(main)
