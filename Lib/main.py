# BIBLIOTECAS A UTILIZAR
from tkinter import *
import time
import pygame
import threading
from class_Submarino import *
from class_Tiempo import *
from class_Obstaculos import *
from class_leviatan import *
import random
pygame.mixer.init()


def use_rgb(rgb):  # FUNCION PARA PODER USAR COLORES RGB EN TKINTER
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb


# VARIABLES PARA LOS COLORES                                                                                             #DISTINTOS COLORES
azul_marino_boton = use_rgb((0, 112, 153))
blanco_letras = use_rgb((173, 171, 159))
azul_oscuro = use_rgb((26, 33, 49))
azul_oscuro2 = use_rgb((40, 51, 75))
azul_oscuro3 = use_rgb((26, 33, 49))
azulito = use_rgb((3, 27, 39))
cafe_madera = use_rgb((184,146,93))


def pantalla_main():  # PRESENTACIÓN DEL JUEGO
    # CANVAS
    canvas = Canvas(window, width=1600, height=870, bg="blue")  # CANVAS BASE DONDE SE UBICARÁN LOS DISTINTOS WIDGETS
    canvas.place(x=-2, y=-2)
    # LABELS
    imagen_parafondo = PhotoImage(
        file="imagenes/imagenes_fondos/THE ABYSS FONDO.png")  # VARIABLE PARA ELEGIR UNA IMAGEN
    imagen_defondo = Label(canvas, image=imagen_parafondo)  # ETQUETA DONDE SE COLOCARÁ LA IMAGEN
    imagen_defondo.place(x=0, y=0)

    # BOTON
    boton_empezar = Button(canvas, text="EMPEZAR", bg=azul_marino_boton, fg=blanco_letras, width=15,
                           font=("SNAP ITC", 20), relief="groove", command=pantalla_selector_niveles)
    boton_empezar.place(x=700, y=250)

    window.mainloop()  # MANTIENE MOSTRANDO LA IMAGEN CONSTANTEMENTE


def pantalla_selector_niveles():  # SE SELECCIONA LA PROFUNDIDAD/VELOCIDAD A EMPEZAR
    pygame.mixer.music.load("Musica/Musica_menu.ogg")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)

    # CANVAS
    canvas = Canvas(window, width=1600, height=870, bg="blue")  # CANVAS DONDE SE COLOCARÁN TODOS LOS OBJETOS
    canvas.place(x=-2, y=-2)

    # LABELS
    imagen_parafondo = PhotoImage(file="imagenes/imagenes_fondos/abismo_menu.png")  # IMAGEN A UTILIZAR
    imagen_defondo = Label(canvas, image=imagen_parafondo)  # ETQUETA DONDE SE COLOCARÁ LA IMAGEN
    imagen_defondo.place(x=0, y=0)

    label_titulo = Label(canvas, text="SELECCIONA LA PROFUNDIDAD", bg=azul_oscuro, fg="white",  # TITULO DEL NIVEL
                         width=30, height=2, font=("Press Start 2P", 20), relief="sunken", borderwidth=3)
    label_titulo.place(x=450, y=250)

    Label_ingreseNombre = Label(canvas, text="Ingrese su nombre :", bg=azul_oscuro2,
                                # CUADRO DE TEXTO DONDE INDICA AL JUGADOR QUE DEBE INGRESAR SU NOMBRE
                                fg="white", width=20, font=("Press Start 2P", 10))
    Label_ingreseNombre.place(x=480, y=380)

    Label_profundidad = Label(canvas, text="Profundidad :", bg=azul_oscuro2, fg="white", width=20,
                              # INDICA LA ZONA DONDE EL JUGADOR ELIGE LA PROFUNDIDAD
                              font=("Press Start 2P", 10))
    Label_profundidad.place(x=480, y=465)

    label_insis = Label(canvas, text="", bg=azul_oscuro2, fg="white", width=40, font=(
    "SNAP ITC", 12))  # CUADRO DE TEXTO DONDE INDICA AL JUGADOR QUE DEBE PONER UN NOMBRE PEQUEÑO
    label_insis.place(x=1125, y=380)

    # BOTONES DE RADIO
    all_radiobutton = IntVar()  # GUARDA EL VALOR DE LOS BOTONES DE RADIO

    radio_button_lvl1 = Radiobutton(canvas, text="4000 m", bg=azul_oscuro2, fg="white",  # BOTON DE RADIO CON VALOR 1
                                    font=("Press Start 2P", 10), variable=all_radiobutton, value=1)
    radio_button_lvl1.place(x=760, y=460)

    radio_button_lvl2 = Radiobutton(canvas, text="7000 m", bg=azul_oscuro2, fg="white",  # BOTON DE RADIO CON VALOR 2
                                    font=("Press Start 2P", 10), variable=all_radiobutton, value=2)
    radio_button_lvl2.place(x=880, y=460)

    radio_button_lvl3 = Radiobutton(canvas, text="10000 m", bg=azul_oscuro2, fg="white",  # BOTON DE RADIO CON VALOR 3
                                    font=("Press Start 2P", 10), variable=all_radiobutton, value=3)
    radio_button_lvl3.place(x=1000, y=460)

    # BOTONES
    empezar = Button(canvas, text="Empezar", bg=azul_oscuro, fg="white", width=20, font=("Press Start 2P", 14),
                     # INICIA LOS DEMÁS NIVELES DEL JUEGO
                     command=lambda: (enviar_a_nivel(cuadro_nombre.get(), all_radiobutton.get(), label_insis)))
    empezar.place(x=690, y=520)

    boton_puntajes = Button(canvas,text="PUNTAJES",bg=azul_oscuro,fg="white",width=20,font=("Press Start 2P", 14),command=pantalla_puntajes)
    boton_puntajes.place(x=690,y=700)

    # testing = Button(canvas,text="testing",command=lambda:game_over)
    # testing.place(x=100,y=100)

    about = Button(canvas, text="ABOUT", command=pantalla_about)
    about.place(x=100, y=200)

    # CUADRO DE NOMBRE
    cuadro_nombre = Entry(canvas, text="Ingrese su nombre", width=30,
                          font=("Arial", 16))  # ES DONDE SE INGRESA EL NOMBRE DEL JUGADOR
    cuadro_nombre.place(x=780, y=380)

    window.mainloop()  # MANTIENE MOSTRANDO LA IMAGEN CONSTANTEMENTE


def enviar_a_nivel(nombre_jugador, valor_radio,
                   label):  # CONDICIONA QUE EL JUGADOR INGRESE UN NOMBRE Y SELECCIONE UNA PROFUNDIDAD
    if len(nombre_jugador) != 0 and len(nombre_jugador) < 17 and valor_radio == 1:
        return nivel_Uno(nombre_jugador)
    if len(nombre_jugador) != 0 and len(nombre_jugador) < 17 and valor_radio == 2:
        return nivel_Dos(nombre_jugador)
    if len(nombre_jugador) != 0 and len(nombre_jugador) < 17 and valor_radio == 3:
        return nivel_Tres(nombre_jugador)
    if len(nombre_jugador) != 0 and len(
            nombre_jugador) < 17:  # EN CASO DE NO SELECCIONAR PROFUNDIDAD, SE EMPEZARÁ EN EL NIVEL 1
        return nivel_Uno(nombre_jugador)
    else:
        return label.config(text="¡Error!: El nombre debe ser menor a 10 digitos")


def nivel_Uno(nombre):  # NIVEL UNO O LA PRIMERA PROFUNDIDAD
    #MUSICA
    pygame.mixer.music.load("Musica/musica_lvl1.ogg")
    pygame.mixer.music.play(-1)
    pygame.mixer.Sound("Musica/monstruo_roar.ogg")

    # CANVAS
    canvas = Canvas(window, bg=azul_oscuro2, width=1600, height=870)  # CANVAS DONDE SE ALMACENARÁ TODO
    canvas.place(x=-2, y=-2)
    canvas_info_arriba = Canvas(canvas, bg=azul_oscuro3, width=1600, height=100,
                                highlightthickness=0)  # CANVAS DONDE IRÁ DISTINTA INFORMACIÓN RELACIONADA AL NIVEL
    canvas_info_arriba.place(x=2, y=0)
    canvas_info_abajo = Canvas(canvas, bg=azul_oscuro3, width=1600, height=60,
                               highlightthickness=0)  # CANVAS DONDE IRÁ LA INFO DEL JUGADOR, TIEMPO Y DEMÁS
    canvas_info_abajo.place(x=2, y=813)

    # LABELS
    label_nivel = Label(canvas_info_arriba, text="Profundidad-4000m", bg=azul_oscuro3, fg="white",
                        # UN SIMPLE LABEL QUE INDICA EL TITULO DEL NIVEL
                        font=("Bodoni MT Black", 26))
    label_nivel.place(x=50, y=30)

    label_nombre = Label(canvas_info_abajo, text="Capitán: " + nombre, bg=azul_oscuro3, fg="white",
                         font=("Bodoni MT Black", 16))  # LABEL DEL NOMBRE DEL JUGADOR
    label_nombre.place(x=50, y=20)

    label_segundos = Label(canvas_info_abajo, text="Segundos:", bg=azul_oscuro3, fg="white",  # LABEL QUE DEMARCA SEGUNDOS
                           font=("Bodoni MT Black", 14))
    label_segundos.place(x=500, y=20)

    label_segundos2 = Label(canvas_info_abajo, text=0, bg=azul_oscuro3, fg="white", font=("Bodoni MT Black", 14))
    label_segundos2.place(x=620, y=20)  # LABEL DONDE SE EDITAN LOS SEGUNDOS

    label_puntos = Label(canvas_info_abajo, text="Puntaje:", bg=azul_oscuro3, fg="white", font=("Bodoni MT Black", 14))
    label_puntos.place(x=800, y=20)  # LABEL DONDE SE DEMARCA PUNTAJE

    label_puntos2 = Label(canvas_info_abajo, text=0, bg=azul_oscuro3, fg="white", font=("Bodoni MT Black", 14))
    label_puntos2.place(x=915, y=20)  # LABEL DONDE SE EDITA LOS PUNTOS

    label_acuPuntos = Label(canvas_info_abajo, text="Puntos acumulados:", bg=azul_oscuro3, fg="white",
                            font=("Bodoni MT Black", 14))  #lABEL QUE DEMARCA PUNTOS ACUMULADOS
    label_acuPuntos.place(x=1250, y=20)

    label_acuPuntos2 = Label(canvas_info_abajo, text=0, bg=azul_oscuro3, fg="white", font=("Bodoni MT Black", 14))
    label_acuPuntos2.place(x=1500, y=20)  #LABEL DONDE SE EDITAN LOS PUNTOS ACUMULADOS

    # BOTONES
    boton_pausa = Button(canvas_info_arriba, text="PAUSA", width=7, height=1, bg="white", fg=azul_oscuro3,
                         # ES EL BOTON DE PAUSA, SERÁ UTILIADO PARA DETENER LA FUNCIÓN DE LOS THREADS
                         font=("SNAP ITC", 12))
    boton_pausa.place(x=1200, y=30)
    boton_regresar = Button(canvas_info_arriba, text="REGRESAR", width=10, height=1, bg="white", fg=azul_oscuro3,
                            # BOTON UTILIZADO PARA VOLVER A LA PÁGINA DE SELECCIÓN DE NIVELES
                            font=("SNAP ITC", 12), command=lambda: (destruccion(),pantalla_selector_niveles()))
    boton_regresar.place(x=1400, y=30)

    def destruccion():  # DESTRUYE TODOS LOS CANVAS EN CASO DE CERRAR EL JUEGO
        canvas.destroy()
        canvas_info_arriba.destroy()
        canvas_info_abajo.destroy()

    # INSTANCIA DE CLASE

    tempo = Tiempo(canvas_info_arriba, canvas, canvas_info_abajo, label_segundos2, label_puntos2, label_acuPuntos2,
                   game_over, nombre)  # INSTAMCIA DE LA CLASE TIEMPO
    jugador = Submarino(canvas,2,game_over, canvas_info_arriba, canvas_info_abajo, tempo,
                        nombre)  # INSTANCIA DE LA CLASE SUBMARINO
    leviatan = Leviatan(canvas)
    obstaculo1 = Obstaculos(canvas, 1600, -5, 0, jugador, game_over, canvas_info_arriba, canvas_info_abajo, tempo,
                            nombre)  # OBSTACULO 1
    obstaculo2 = Obstaculos(canvas, 2000, -5, 0, jugador, game_over, canvas_info_arriba, canvas_info_abajo, tempo,
                            nombre)  # OBSTACULO 2
    obstaculo3 = Obstaculos(canvas, 2400, -5, 0, jugador, game_over, canvas_info_arriba, canvas_info_abajo, tempo,
                            nombre)  # OBSTACULO 3
    obstaculo4 = Obstaculos(canvas, 2800, -5, 0, jugador, game_over, canvas_info_arriba, canvas_info_abajo, tempo,
                            nombre)  # OBSTACULO 4

    # HILOS
    def all_Threads():  # EJECUTA LOS HILOS

        hilo_tempo = threading.Thread(
            target=tempo.avance_1)  # HILO QUE PROVOCA EL AVANCE CONTINUO DEL CONTADOR Y SE MUESTRA EN EL LABEL_SEG
        hilo_tempo.start()

        #HILO DE LOS OBSTACULOS
        hilo_pez = threading.Thread(target=obstaculo1.move)
        hilo_pez.start()
        hilo_pez2 = threading.Thread(target=obstaculo2.move)
        hilo_pez2.start()
        hilo_pez3 = threading.Thread(target=obstaculo3.move)
        hilo_pez3.start()
        hilo_pez4 = threading.Thread(target=obstaculo4.move)
        hilo_pez4.start()

        hil = threading.Thread(target=obstaculo1.prueba)
        hil.start()

        #HILO JUGADOR
        hilo_submarino = threading.Thread(target=jugador.movement)
        hilo_submarino.start()

        #HILO MONSTRUP
        hilo_levi = threading.Thread(target=leviatan.sprite)
        hilo_levi.start()
        hilo_P = threading.Thread(target=leviatan.prueba)
        hilo_P.start()

    thread_todo = threading.Thread(target=all_Threads)  # HILO QUE INICIA TODOS LOS THREADS
    thread_todo.start()

    # HABILITAR EL USO DE TECLAS
    window.bind("<Up>", lambda e: jugador.arriba(
        e))  # AL PRESIONAR LA TECLA, EJECUTA EL METODO DE LA CLASE PARA CAMBIAR LA DIRECCIÓN A ARRIBA
    window.bind("<Down>", lambda e: jugador.abajo(
        e))  # AL PRESIONAR LA TECLA, EJECUTA EL METODO DE LA CLASE PARA CAMBIAR LA DIRECCIÓN A ABAJO
    window.bind("<Right>", lambda e: jugador.derecha(
        e))  # AL PRESIONAR LA TECLA, EJECUTA EL METODO DE LA CLASE PARA CAMBIAR LA DIRECCIÓN A DERECHA
    window.bind("<Left>", lambda e: jugador.izquierda(
        e))  # AL PRESIONAR LA TECLA, EJECUTA EL METODO DE LA CLASE PARA CAMBIAR LA DIRECCIÓN A IZQUIERDA

    window.mainloop()  # BUCLE PARA MANTENER LA VENTANA ABIERTA


def nivel_Dos(nombre):  # NIVEL DOS
    # MUSICA
    pygame.mixer.music.load("Musica/musica_lvl2.ogg")
    pygame.mixer.music.play(-1)
    pygame.mixer.Sound("Musica/monstruo_roar.ogg")

    # CANVAS
    canvas = Canvas(window, bg=azul_oscuro2, width=1600, height=870)  # CANVAS DONDE SE ALMACENARÁ TODO
    canvas.place(x=-2, y=-2)
    canvas_info_arriba = Canvas(canvas, bg=azul_oscuro3, width=1600, height=100,
                                highlightthickness=0)  # CANVAS DONDE IRÁ DISTINTA INFORMACIÓN RELACIONADA AL NIVEL
    canvas_info_arriba.place(x=2, y=0)
    canvas_info_abajo = Canvas(canvas, bg=azul_oscuro3, width=1600, height=60,
                               highlightthickness=0)  # CANVAS DONDE IRÁ LA INFO DEL JUGADOR, TIEMPO Y DEMÁS
    canvas_info_abajo.place(x=2, y=813)

    # LABELS
    label_nivel = Label(canvas_info_arriba, text="Profundidad-7000m", bg=azul_oscuro3, fg="white",
                        # UN SIMPLE LABEL QUE INDICA EL TITULO DEL NIVEL
                        font=("Bodoni MT Black", 26))
    label_nivel.place(x=50, y=30)

    label_nombre = Label(canvas_info_abajo, text="Capitán: " + nombre, bg=azul_oscuro3, fg="white",
                         font=("Bodoni MT Black", 16))
    label_nombre.place(x=50, y=20)

    label_segundos = Label(canvas_info_abajo, text="Segundos:", bg=azul_oscuro3, fg="white",
                           font=("Bodoni MT Black", 14))
    label_segundos.place(x=500, y=20)

    label_segundos2 = Label(canvas_info_abajo, text=0, bg=azul_oscuro3, fg="white", font=("Bodoni MT Black", 14))
    label_segundos2.place(x=620, y=20)

    label_puntos = Label(canvas_info_abajo, text="Puntaje:", bg=azul_oscuro3, fg="white", font=("Bodoni MT Black", 14))
    label_puntos.place(x=800, y=20)

    label_puntos2 = Label(canvas_info_abajo, text=0, bg=azul_oscuro3, fg="white", font=("Bodoni MT Black", 14))
    label_puntos2.place(x=915, y=20)

    label_acuPuntos = Label(canvas_info_abajo, text="Puntos acumulados:", bg=azul_oscuro3, fg="white",
                            font=("Bodoni MT Black", 14))
    label_acuPuntos.place(x=1250, y=20)

    label_acuPuntos2 = Label(canvas_info_abajo, text=0, bg=azul_oscuro3, fg="white", font=("Bodoni MT Black", 14))
    label_acuPuntos2.place(x=1500, y=20)

    # BOTONES
    boton_pausa = Button(canvas_info_arriba, text="PAUSA", width=7, height=1, bg="white", fg=azul_oscuro3,
                         # ES EL BOTON DE PAUSA, SERÁ UTILIADO PARA DETENER LA FUNCIÓN DE LOS THREADS
                         font=("SNAP ITC", 12))
    boton_pausa.place(x=1200, y=30)
    boton_regresar = Button(canvas_info_arriba, text="REGRESAR", width=10, height=1, bg="white", fg=azul_oscuro3,
                            # BOTON UTILIZADO PARA VOLVER A LA PÁGINA DE SELECCIÓN DE NIVELES
                            font=("SNAP ITC", 12), command=lambda: (destruccion(),pantalla_selector_niveles()))
    boton_regresar.place(x=1400, y=30)

    def destruccion():  # DESTRUYE TODOS LOS CANVAS
        canvas.destroy()
        canvas_info_arriba.destroy()
        canvas_info_abajo.destroy()

    # INSTANCIA DE CLASE

    tempo = Tiempo(canvas_info_arriba, canvas, canvas_info_abajo, label_segundos2, label_puntos2, label_acuPuntos2,
                   game_over, nombre)  # INSTAMCIA DE LA CLASE TIEMPO
    jugador = Submarino(canvas,-3, game_over, canvas_info_arriba, canvas_info_abajo, tempo,
                        nombre)  # INSTANCIA DE LA CLASE SUBMARINO
    leviatan = Leviatan(canvas)

    #INSTANCIA OBSTACULOS
    obstaculo1 = Obstaculos(canvas, 1600, -7, 0, jugador, game_over, canvas_info_arriba, canvas_info_abajo, tempo,
                            nombre)
    obstaculo2 = Obstaculos(canvas, 2000, -7, 0, jugador, game_over, canvas_info_arriba, canvas_info_abajo, tempo,
                            nombre)
    obstaculo3 = Obstaculos(canvas, 2400, -7, 0, jugador, game_over, canvas_info_arriba, canvas_info_abajo, tempo,
                            nombre)
    obstaculo4 = Obstaculos(canvas, 2800, -7, 0, jugador, game_over, canvas_info_arriba, canvas_info_abajo, tempo,
                            nombre)

    # HILOS
    def all_Threads():  # EJECUTA LOS HILOS

        hilo_tempo = threading.Thread(
            target=tempo.avance_2)  # HILO QUE PROVOCA EL AVANCE CONTINUO DEL CONTADOR Y SE MUESTRA EN EL LABEL_SEG
        hilo_tempo.start()
        hilo_pez = threading.Thread(target=obstaculo1.move)
        hilo_pez.start()
        hilo_pez2 = threading.Thread(target=obstaculo2.move)
        hilo_pez2.start()
        hilo_pez3 = threading.Thread(target=obstaculo3.move)
        hilo_pez3.start()
        hilo_pez4 = threading.Thread(target=obstaculo4.move)
        hilo_pez4.start()

        hil = threading.Thread(target=obstaculo1.prueba)
        hil.start()

        hilo_submarino = threading.Thread(target=jugador.movement)
        hilo_submarino.start()

        hilo_levi = threading.Thread(target=leviatan.sprite)
        hilo_levi.start()
        hilo_P = threading.Thread(target=leviatan.prueba)
        hilo_P.start()

    thread_todo = threading.Thread(target=all_Threads)
    thread_todo.start()

    # HABILITAR EL USO DE TECLAS
    window.bind("<Up>", lambda e: jugador.arriba(
        e))  # AL PRESIONAR LA TECLA, EJECUTA EL METODO DE LA CLASE PARA CAMBIAR LA DIRECCIÓN A ARRIBA
    window.bind("<Down>", lambda e: jugador.abajo(
        e))  # AL PRESIONAR LA TECLA, EJECUTA EL METODO DE LA CLASE PARA CAMBIAR LA DIRECCIÓN A ABAJO
    window.bind("<Right>", lambda e: jugador.derecha(
        e))  # AL PRESIONAR LA TECLA, EJECUTA EL METODO DE LA CLASE PARA CAMBIAR LA DIRECCIÓN A DERECHA
    window.bind("<Left>", lambda e: jugador.izquierda(
        e))  # AL PRESIONAR LA TECLA, EJECUTA EL METODO DE LA CLASE PARA CAMBIAR LA DIRECCIÓN A IZQUIERDA

    window.mainloop()  # BUCLE PARA MANTENER LA VENTANA ABIERTA


def nivel_Tres(nombre):  # NIVEL TRES
    # CANVAS
    # MUSICA
    pygame.mixer.music.load("Musica/musica_lvl3.ogg")
    pygame.mixer.music.play(-1)
    pygame.mixer.Sound("Musica/monstruo_roar.ogg")

    # CANVAS
    canvas = Canvas(window, bg=azul_oscuro2, width=1600, height=870)  # CANVAS DONDE SE ALMACENARÁ TODO
    canvas.place(x=-2, y=-2)
    canvas_info_arriba = Canvas(canvas, bg=azul_oscuro3, width=1600, height=100,
                                highlightthickness=0)  # CANVAS DONDE IRÁ DISTINTA INFORMACIÓN RELACIONADA AL NIVEL
    canvas_info_arriba.place(x=2, y=0)
    canvas_info_abajo = Canvas(canvas, bg=azul_oscuro3, width=1600, height=60,
                               highlightthickness=0)  # CANVAS DONDE IRÁ LA INFO DEL JUGADOR, TIEMPO Y DEMÁS
    canvas_info_abajo.place(x=2, y=813)

    # LABELS
    label_nivel = Label(canvas_info_arriba, text="Profundidad-10000m", bg=azul_oscuro3, fg="white",
                        # UN SIMPLE LABEL QUE INDICA EL TITULO DEL NIVEL
                        font=("Bodoni MT Black", 26))
    label_nivel.place(x=50, y=30)

    label_nombre = Label(canvas_info_abajo, text="Capitán: " + nombre, bg=azul_oscuro3, fg="white",
                         font=("Bodoni MT Black", 16))
    label_nombre.place(x=50, y=20)

    label_segundos = Label(canvas_info_abajo, text="Segundos:", bg=azul_oscuro3, fg="white",
                           font=("Bodoni MT Black", 14))
    label_segundos.place(x=500, y=20)

    label_segundos2 = Label(canvas_info_abajo, text=0, bg=azul_oscuro3, fg="white", font=("Bodoni MT Black", 14))
    label_segundos2.place(x=620, y=20)

    label_puntos = Label(canvas_info_abajo, text="Puntaje:", bg=azul_oscuro3, fg="white", font=("Bodoni MT Black", 14))
    label_puntos.place(x=800, y=20)

    label_puntos2 = Label(canvas_info_abajo, text=0, bg=azul_oscuro3, fg="white", font=("Bodoni MT Black", 14))
    label_puntos2.place(x=915, y=20)

    label_acuPuntos = Label(canvas_info_abajo, text="Puntos acumulados:", bg=azul_oscuro3, fg="white",
                            font=("Bodoni MT Black", 14))
    label_acuPuntos.place(x=1250, y=20)

    label_acuPuntos2 = Label(canvas_info_abajo, text=0, bg=azul_oscuro3, fg="white", font=("Bodoni MT Black", 14))
    label_acuPuntos2.place(x=1500, y=20)

    # BOTONES
    boton_pausa = Button(canvas_info_arriba, text="PAUSA", width=7, height=1, bg="white", fg=azul_oscuro3,
                         # ES EL BOTON DE PAUSA, SERÁ UTILIADO PARA DETENER LA FUNCIÓN DE LOS THREADS
                         font=("SNAP ITC", 12))
    boton_pausa.place(x=1200, y=30)
    boton_regresar = Button(canvas_info_arriba, text="REGRESAR", width=10, height=1, bg="white", fg=azul_oscuro3,
                            # BOTON UTILIZADO PARA VOLVER A LA PÁGINA DE SELECCIÓN DE NIVELES
                            font=("SNAP ITC", 12), command=lambda: (destruccion(),pantalla_selector_niveles()))
    boton_regresar.place(x=1400, y=30)

    def destruccion():  #DESTRUYE TODOS LOS CANVAS
        canvas.destroy()
        canvas_info_arriba.destroy()
        canvas_info_abajo.destroy()

    # INSTANCIA DE CLASE

    tempo = Tiempo(canvas_info_arriba, canvas, canvas_info_abajo, label_segundos2, label_puntos2, label_acuPuntos2,
                   game_over, nombre)  # INSTAMCIA DE LA CLASE TIEMPO
    jugador = Submarino(canvas,-4, game_over, canvas_info_arriba, canvas_info_abajo, tempo,
                        nombre)  # INSTANCIA DE LA CLASE SUBMARINO
    leviatan = Leviatan(canvas)

    #OBSTACULOS INSTANCIAS
    obstaculo1 = Obstaculos(canvas, 1600, -9, 0, jugador, game_over, canvas_info_arriba, canvas_info_abajo, tempo,
                            nombre)
    obstaculo2 = Obstaculos(canvas, 2000, -9, 0, jugador, game_over, canvas_info_arriba, canvas_info_abajo, tempo,
                            nombre)
    obstaculo3 = Obstaculos(canvas, 2400, -9, 0, jugador, game_over, canvas_info_arriba, canvas_info_abajo, tempo,
                            nombre)
    obstaculo4 = Obstaculos(canvas, 2800, -9, 0, jugador, game_over, canvas_info_arriba, canvas_info_abajo, tempo,
                            nombre)

    # HILOS
    def all_Threads():  # EJECUTA LOS HILOS

        hilo_tempo = threading.Thread(
            target=tempo.avance_3)  # HILO QUE PROVOCA EL AVANCE CONTINUO DEL CONTADOR Y SE MUESTRA EN EL LABEL_SEG
        hilo_tempo.start()
        hilo_pez = threading.Thread(target=obstaculo1.move)
        hilo_pez.start()
        hilo_pez2 = threading.Thread(target=obstaculo2.move)
        hilo_pez2.start()
        hilo_pez3 = threading.Thread(target=obstaculo3.move)
        hilo_pez3.start()
        hilo_pez4 = threading.Thread(target=obstaculo4.move)
        hilo_pez4.start()

        hil = threading.Thread(target=obstaculo1.prueba)
        hil.start()

        hilo_submarino = threading.Thread(target=jugador.movement)
        hilo_submarino.start()

        hilo_levi = threading.Thread(target=leviatan.sprite)
        hilo_levi.start()
        hilo_P = threading.Thread(target=leviatan.prueba)
        hilo_P.start()

    thread_todo = threading.Thread(target=all_Threads)  # TODOS LOS THREADS
    thread_todo.start()

    # HABILITAR EL USO DE TECLAS
    window.bind("<Up>", lambda e: jugador.arriba(
        e))  # AL PRESIONAR LA TECLA, EJECUTA EL METODO DE LA CLASE PARA CAMBIAR LA DIRECCIÓN A ARRIBA
    window.bind("<Down>", lambda e: jugador.abajo(
        e))  # AL PRESIONAR LA TECLA, EJECUTA EL METODO DE LA CLASE PARA CAMBIAR LA DIRECCIÓN A ABAJO
    window.bind("<Right>", lambda e: jugador.derecha(
        e))  # AL PRESIONAR LA TECLA, EJECUTA EL METODO DE LA CLASE PARA CAMBIAR LA DIRECCIÓN A DERECHA
    window.bind("<Left>", lambda e: jugador.izquierda(
        e))  # AL PRESIONAR LA TECLA, EJECUTA EL METODO DE LA CLASE PARA CAMBIAR LA DIRECCIÓN A IZQUIERDA

    window.mainloop()  # BUCLE PARA MANTENER LA VENTANA ABIERTA


def game_over(canva_arriba, canva, canva_abajo, nombre, puntos):
    pygame.mixer.music.load("Musica/sonido_gameover.ogg")
    pygame.mixer.music.play(1)
    #pygame.mixer.Sound.stop()
    # CANVAS
    canvas = Canvas(window, width=1600, height=870, bg="black")  # CANVAS PRINCIPAL
    canvas.place(x=-2, y=-2)

    # LABELS
    label_titulo = Label(canvas, text="JUEGO TERMINADO", font=("Press Start 2P", 40), bg="black", fg="white")
    label_titulo.place(x=400, y=200)

    imagen_destroy = PhotoImage(file="imagenes/imagenes_cosas/submarino_destruido.png")
    label_destroy = Label(canvas, image=imagen_destroy, highlightthickness=0, bd=0)
    label_destroy.place(x=1260, y=150)

    label_puntaje = Label(canvas, text="Capitan " + nombre + " usted obtuvo: " + str(puntos) + " puntos",font=("Press Start 2P", 15)).place(x=450, y=400)  #ESTE LABEL MUESTRA TEMPORALMENTE AL JUGADOR QUE PUNTAJE OBTUVO

    # BOTONES
    volver = Button(canvas, text="VOLVER", font=("Press Start 2P", 20), bg="black", fg="white",command=pantalla_selector_niveles)
    volver.place(x=400, y=500)

    puntajes = Button(canvas, text="PUNTAJES", font=("Press Start 2P", 20), bg="black", fg="white",command=pantalla_puntajes)
    puntajes.place(x=800, y=500)

    #EDICION DEL ARCHIVO DE TEXTO
    texto = nombre + " --> " + str(puntos) + "\n"  # SE MESTRA QUE SE ESCRIBIRÁ EN EL RENGLON
    archivo = open("PUNTAJES.txt","a")  #SE ABRE EL ARCHIVO EN MODO EDICION
    archivo.write(texto)  # SE ESCRIBE UN FORMATO EN EL ARCHIVP
    archivo.close()  #SE CIERRA EL ARCHIVO

    canva_arriba.destroy()  # CON ESTO SE DESTRUYE EL CANVAS DE ARRIBA
    canva.destroy()  # CON ESTO SE DESTRUYE EL CANVAS DEL MEDIO
    canva_abajo.destroy()  # CON ESTO SE DESTRUYE EL CANVAS DE ABAJO

    window.mainloop()


def pantalla_puntajes():
    pygame.mixer.music.load("Musica/Musica_puntaje.ogg")
    pygame.mixer.music.play()
    # CANVAS
    canvas = Canvas(window, bg="snow4", width=1600, height=870)
    canvas.place(x=-2, y=-2)

    # LABEL
    fondo_imagen = PhotoImage(file="imagenes/imagenes_fondos/tabla_puntos.png")
    label_fondo = Label(canvas, image=fondo_imagen).place(x=0, y=0)

    # BOTON
    boton_regresar = Button(canvas, text="VOLVER", bg=cafe_madera,fg="white",font=("Press Start 2P", 13), width=15, height=2,command=pantalla_selector_niveles)
    boton_regresar.place(x=20, y=700)

    #LEER EL TEXTO
    lista = open("PUNTAJES.txt", "r")

    def funcion(texto):  #ESTA FUNCION GENERA LABELS QUE MUESTRAN LAS PUNTUACIONES
        y = 100
        cont = 0
        for i in texto:
            if cont >= 5:  # SI HAY MAS DE 5 LABELS, DEJA DE CREAR
                break
            else:
                print(i)
                Label(canvas, text=i, width=20, height=3,bg=cafe_madera,fg="white",font=("Press Start 2P", 10),bd=5,relief="groove").place(x=700, y=y)
                y += 150
                cont += 1

    hilo = threading.Thread(target=funcion, args=(lista,))
    hilo.start()

    window.mainloop()


def pantalla_about():
    pygame.mixer.music.load("Musica/Musica_about.ogg")
    pygame.mixer.music.play(-1)
    #MUSICA
    pygame.mixer.music.load("Musica/Musica_about.ogg")
    pygame.mixer.music.play(-1)
    # CANVAS
    canvas = Canvas(window, width=1600, height=870, bg="blue")
    canvas.place(x=-2, y=-2)
    # LABELS
    imagen = PhotoImage(file="imagenes/imagenes_fondos/under_weather.png")
    label_imagen = Label(canvas, image=imagen)
    label_imagen.place(x=0, y=0)

    pais = "Costa Rica"

    texto = """
        ABOUT:

        Pais: """ + pais + """

        Universidad y Carrera: TEC Costa Rica, ingeniería en computadores(CE)

        Intro y taller a la programación Grupo 1

        Nombre del profesor: Jeff Schmidth Peralta

        Version del programa: 1.0

        Autor: Josthin Soto Sánchez

        """
    texto2 = """
        FUNCIONES EXTERNAS A USAR:

        Movimiento del submarino = www.geeksforgeeks.org/python-tkinter-moving-objects-using-canvas-move-method/

        Usar colores RGB = stackoverflow.com/questions/51591456/can-i-use-rgb-in-tkinter/51592104

        """
    label_deco = Label(canvas, bg="white", width=130, height=21)
    label_deco.place(x=345, y=100)
    info_about = Label(canvas, text=texto, bg=azulito, fg="white", font=("Times New Romman", 13), width=100)
    info_about.place(x=350, y=105)
    label_deco2 = Label(canvas, bg="white", width=130, height=11)
    label_deco2.place(x=345, y=448)
    label_modulo = Label(canvas, text=texto2, bg=azulito, fg="white", font=("Times New Romman", 13), width=100)
    label_modulo.place(x=350, y=455)

    # BUTTON
    boton = Button(canvas, text="Volver", command=pantalla_selector_niveles)
    boton.place(x=100, y=550)
    window.mainloop()

# LAS BASES DE LAS DIFERENTES PANTALLAS

window = Tk()
window.title("THE ABYSS")
window.geometry("1600x870")
window.resizable(False, False)
pantalla_main()
