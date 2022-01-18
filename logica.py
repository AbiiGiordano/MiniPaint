import gamelib
import png

COLORES = ((1, '#000000'), (2, '#ffff00'), (3, '#00ff00'), (4, '#0000ff'), (5, '#ff0000'), (6, '#ff00ff'), (7, '#ffffff'))

def paint_nuevo():
    '''Inicializa el estado del programa con una imagen vacía'''
    return {}


def paint_mostrar(paint, tecla, pixeles, nuevo_color, modo):
    '''Dibuja la interfaz de la aplicación en la ventana'''
    gamelib.draw_begin()

    # Cuadrícula
    gamelib.draw_rectangle(5, 5, 345, 345)
    for linea_fila in range(5, 350, 350 // pixeles):           # Dibujo lineas horizontales
        gamelib.draw_line(5, linea_fila, 345, linea_fila, fill = 'black')
    for linea_columna in range(5, 350, 350 // pixeles):        # Dibujo lineas verticales
        gamelib.draw_line(linea_columna, 5, linea_columna, 345, fill = 'black')

    # Colores
    gamelib.draw_rectangle(10, 370, 40, 400, fill = 'black', outline = 'gray')
    gamelib.draw_rectangle(50, 370, 80, 400, fill = 'yellow', outline = 'gray')
    gamelib.draw_rectangle(90, 370, 120, 400, fill = 'lime', outline = 'gray')
    gamelib.draw_rectangle(130, 370, 160, 400, fill = 'blue', outline = 'gray')
    gamelib.draw_rectangle(170, 370, 200, 400, fill = 'red', outline = 'gray')
    gamelib.draw_rectangle(210, 370, 240, 400, fill = 'magenta', outline = 'gray')
    gamelib.draw_rectangle(250, 370, 280, 400, fill = 'white', outline = 'gray')

    # Color elegido por el usuario
    if nuevo_color is None:
        gamelib.draw_rectangle(310, 370, 340, 400, fill = 'gray', outline = 'gray')
    else:
        gamelib.draw_rectangle(310, 370, 340, 400, fill = nuevo_color, outline = 'gray')

    # Instrucciones para elegir colores
    gamelib.draw_text('1', 25, 360, bold = True)
    gamelib.draw_text('2', 65, 360, bold = True)
    gamelib.draw_text('3', 105, 360, bold = True)
    gamelib.draw_text('4', 145, 360, bold = True)
    gamelib.draw_text('5', 185, 360, bold = True)
    gamelib.draw_text('6', 225, 360, bold = True)
    gamelib.draw_text('7', 265, 360, bold = True)
    gamelib.draw_text('C', 325, 360, bold = True)

    # Opciones para guardar/abrir
    gamelib.draw_rectangle(10, 420, 90, 460, fill = 'gray', outline = 'white')
    gamelib.draw_text('Guardar ppm', 50, 430, fill = 'black')
    gamelib.draw_text('G', 50, 450, fill = 'black', bold = True)

    gamelib.draw_rectangle(110, 420, 190, 460, fill = 'gray', outline = 'white')
    gamelib.draw_text('Abrir ppm', 150, 430, fill = 'black')
    gamelib.draw_text('A', 150, 450, fill = 'black', bold = True)

    gamelib.draw_rectangle(210, 420, 290, 460, fill = 'gray', outline = 'white')
    gamelib.draw_text('Guardar png', 250, 430, fill = 'black')
    gamelib.draw_text('P', 250, 450, fill = 'black', bold = True)

    # Deshacer/Rehacer
    gamelib.draw_rectangle(110, 480, 190, 530, fill = '#D5DCDE', outline = 'white')
    gamelib.draw_text('Deshacer', 150, 490, fill = 'black')
    gamelib.draw_text('Flecha izq', 150, 510, bold = True, fill = 'black')
    gamelib.draw_text('↤', 150, 520, fill = 'black', size = 14)

    gamelib.draw_rectangle(210, 480, 290, 530, fill = '#D5DCDE', outline = 'white')
    gamelib.draw_text('Rehacer', 250, 490, fill = 'black')
    gamelib.draw_text('Flecha der', 250, 510, bold = True, fill = 'black')
    gamelib.draw_text('↦', 250, 520, fill = 'black', size = 14)

    # Nueva hoja
    gamelib.draw_rectangle(305, 440, 340, 530, fill = 'gray', outline = 'white')
    gamelib.draw_text('N', 323, 425, fill = 'white', bold = True)
    gamelib.draw_text('N', 323, 455, fill = 'black')
    gamelib.draw_text('u', 324, 470, fill = 'black')
    gamelib.draw_text('e', 323, 485, fill = 'black')
    gamelib.draw_text('v', 323, 500, fill = 'black')
    gamelib.draw_text('o', 324, 515, fill = 'black')

    # Lapiz/Balde
    gamelib.draw_rectangle(10, 470, 90, 530, fill = 'gray', outline = 'white')
    gamelib.draw_text('Lapiz', 30, 480, fill = 'black')
    gamelib.draw_text('L', 30, 495, fill = 'black', bold = True)
    gamelib.draw_text('Balde', 70, 480, fill = 'black')
    gamelib.draw_text('B', 70, 495, fill = 'black', bold = True)

    if modo == 'lapiz':
        gamelib.draw_text('X', 30, 515, size = 15, fill = 'red')
    else:
        gamelib.draw_text('X', 70, 515, size = 15, fill = 'red')

    # Color seleccionado
    if tecla in (1, 2, 3, 4, 5, 6, 7):
        gamelib.draw_oval(20 + (tecla - 1) * 40, 380, 30 + (tecla - 1) * 40, 390)   # Marcar color seleccionado según tecla
    elif str(tecla).lower() == 'c':
        gamelib.draw_oval(320, 380, 330, 390)

    # Dibujo
    for (f, c), color in paint.items():
        # Esquina superior izquierda del pixel a colorear
        x1 = c * (350 // pixeles) + 5
        y1 = f * (350 // pixeles) + 5

        # Esquina inferior derecha del pixel a colorear
        x2, y2  = x1 + (350 // pixeles), y1 + (350 // pixeles)

        gamelib.draw_rectangle(x1, y1, x2, y2, fill = color)

    gamelib.draw_end()


def elegir_color(tecla):
    '''Devuelve el color elegido por el usuario
    según la tecla presionada'''
    for numero, color in COLORES:
        if numero == tecla:
            return color
    return None


def crear_color():
    '''Crea un nuevo color mediante un código
    hexadecimal ingresado por el usuario'''
    nuevo_color = gamelib.input('Escriba el color que desea en código hexadecimal:')

    if not nuevo_color:
        if nuevo_color is None:                    # Si se presionó 'cancelar'
            return None
        gamelib.say('Código inválido :(')          # Si nuevo_color es una cadena vacía
        return None

    # Verifica que se trate de un código válido
    if nuevo_color[0] == '#' and len(nuevo_color) == 7:
        nuevo_color = nuevo_color[1:]
    elif len(nuevo_color) != 6:
        gamelib.say('Código inválido :(')
        return None

    # Verifica que los caracteres ingresados sean correctos
    for c in nuevo_color:
        if c.lower() not in ('a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            gamelib.say('Código inválido :(')
            return None

    return ('#' + nuevo_color)


def pintar(paint, x, y, pixeles, color):
    '''Dado un color, pinta los pixeles correspondientes
    según los valores de x e y indicados'''
    fila = y // (350 // pixeles)
    columna = x // (350 // pixeles)
    paint[(fila, columna)] = color          # Agrego al diccionario la posición con el color correspondiente


def borrar(paint, x, y, pixeles):
    '''Pinta los pixeles correspondientes de
    blanco según los valores de x e y indicados'''
    fila = y // (350 // pixeles)
    columna = x // (350 // pixeles)
    if (fila, columna) in paint:
        paint.pop((fila, columna))          # Borro del diccionario al pintar con blanco (borrar)


def balde(paint, x, y, pixeles, color):
    '''Determina la fila, la columna y el color presionados y llama a la funcion recurisva'''
    fila = y // (350 // pixeles)
    columna = x // (350 // pixeles)
    color_tocado = paint.get((fila, columna), '#ffffff')
    if color_tocado != color:           # Solo pinta si el color tocado es diferente al seleccionado
        _pintar_con_balde(paint, fila, columna, color_tocado, color, pixeles)


def _pintar_con_balde(paint, fila, columna, color_tocado, color, pixeles):
    if paint.get((fila, columna), '#ffffff') != color_tocado or any([fila >= pixeles, fila < 0, columna >= pixeles, columna < 0]):
        return

    if color != '#ffffff':
        paint[(fila, columna)] = color
    else:
        paint.pop((fila, columna))

    _pintar_con_balde(paint, fila - 1, columna, color_tocado, color, pixeles)   # Celda de arriba
    _pintar_con_balde(paint, fila + 1, columna, color_tocado, color, pixeles)   # Celda de abajo
    _pintar_con_balde(paint, fila, columna + 1, color_tocado, color, pixeles)   # Celda de la derecha
    _pintar_con_balde(paint, fila, columna - 1, color_tocado, color, pixeles)   # Celda de la izquierda


def crear_hoja():
    '''Crea una nueva hoja vacía (blanca)'''
    nuevo = gamelib.input('Desea crear una hoja vacía? Oprima el boton "OK" para borrar todo')

    if nuevo is None:       # Si se presionó 'cancelar'
        return None
    return {}               # Si se presionó 'ok'


def abrir_ppm():
    '''Abre un archivo de dibujo
    de formato .ppm'''
    ruta = gamelib.input('Escriba la ruta del archivo .ppm que desea abrir:')

    if ruta is None:                        # Si se presionó 'cancelar'
        return None, None
    if any((ruta == ' ', ruta == '')):      # Si la ruta es inválida
        gamelib.say('Ruta inválida :(')
        return None, None

    nuevo_paint = {}        # Creo nuevo dibujo

    try:
        with open(ruta) as archivo:
            # Armo lista con cada dato
            dibujo = archivo.read().rstrip('\n')
            dibujo = dibujo.split()
            fila, columna = int(dibujo[1]), int(dibujo[2])        # Dimensión de la imagen

            n = 4                       # Indice de lista donde empiezan los colores
            for f in range(fila):
                for c in range(columna):
                    color = dibujo[n:n + 3]
                    if color == ['255', '255', '255']:          # Si el pixel no está pintado (blanco = borrar)
                        n += 3
                        continue
                    r, g, b = int(dibujo[n]), int(dibujo[n + 1]), int(dibujo[n + 2])
                    color_hex = dec_a_hex(r, g, b)
                    nuevo_paint[(f, c)] = color_hex
                    n += 3

            return nuevo_paint, fila               # Devuelvo también la dimensión de los pixeles del archivo para adaptar la hoja

    except FileNotFoundError:                       # Si el archivo no existe
        gamelib.say('Archivo no encontrado :(')
        return None, None


def guardar_ppm(paint, pixeles):
    '''Guarda el dibujo realizado por el usuario
    en un archivo de formato .ppm'''
    ruta = gamelib.input('Escriba la ruta donde desea guardar el archivo .ppm:')

    if ruta is None:                          # Si se presionó 'cancelar'
        return
    if any((ruta == ' ', ruta == '')):        # Si la ruta es inválida
        gamelib.say('Ruta inválida :(')
        return

    with open(ruta, 'w') as archivo:
        archivo.write('P3\n')                           # Encabezado
        archivo.write(f'{pixeles} {pixeles}\n')         # Dimensión
        archivo.write('255\n')                          # Intensidad máxima

        for f in range(pixeles):
            for c in range(pixeles):
                paint[(f, c)] = paint.get((f, c), '#ffffff')
                color = hex_a_dec(paint[(f, c)])

                # Escribo el color
                for n in range(len(color)):
                    if n == 2:
                        archivo.write(f'{color[n]}\n')    # Si es el ultimo numero del código decimal, no agrego espacio
                    else:
                        archivo.write(f'{color[n]} ')


def guardar_png(paint, pixeles):
    '''Guarda el dibujo realizado por el usuario
    en un archivo de formato .png'''
    ruta = gamelib.input('Escriba la ruta donde desea guardar el archivo .png:')

    if ruta is None:                             # Si se presionó 'cancelar'
        return
    if any((ruta == ' ', ruta == '')):          # Si la ruta es inválida
        gamelib.say('Ruta inválida :(')
        return

    # Armo archivo en formato png
    paleta = []
    imagen = []
    for f in range(pixeles):
        auxiliar = []
        for c in range(pixeles):
            paint[(f, c)] = paint.get((f, c), '#ffffff')
            color_dec = hex_a_dec(paint[(f, c)])
            if color_dec not in paleta:
                paleta.append(color_dec)              # Se va creando la paleta en base a los colores hallados
            auxiliar.append(paleta.index(color_dec))
        imagen.append(auxiliar)

    png.escribir(ruta, paleta, imagen)


def hex_a_dec(hex):
    '''Convierte un color dado en codigo
    hexadecimal a código decimal'''
    return (int(hex[1:3], 16), int(hex[3:5], 16), int(hex[5:7], 16))


def dec_a_hex(r, g, b):
    '''Convierte un color dado en codigo
    decimal a código hexadecimal'''
    return f'#{r:02x}{g:02x}{b:02x}'


def copiar_diccionario(dicc):
    '''Dado un diccionario, devuelve una copia del mismo'''
    nuevo = {}
    for k, v in dicc.items():
        nuevo[k] = v

    return nuevo
