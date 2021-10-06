#BIBLIOTECAS A UTILIZAR
from tkinter import *
import time
import pygame
import threading
from class_Submarino import *
from class_Tiempo import *
from class_Obstaculos import *
from class_leviatan import *
import random

def use_rgb(rgb):                                                                                                       #FUNCION PARA PODER USAR COLORES RGB EN TKINTER
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb

#VARIABLES PARA LOS COLORES                                                                                             #DISTINTOS COLORES
azul_marino_boton = use_rgb((0,112,153))
blanco_letras = use_rgb((173,171,159))
azul_oscuro = use_rgb((26,33,49))
azul_oscuro2 = use_rgb((40,51,75))
azul_oscuro3 = use_rgb((26,33,49))

def pantalla_main():                                                                                                    #PRESENTACIÓN DEL JUEGO
    #CANVAS
    canvas = Canvas(window,width=1600,height=870,bg="blue")                                                             #CANVAS BASE DONDE SE UBICARÁN LOS DISTINTOS WIDGETS
    canvas.place(x=-2,y=-2)
    #LABELS
    imagen_parafondo = PhotoImage(file="imagenes/imagenes_fondos/THE ABYSS FONDO.png")                                  #VARIABLE PARA ELEGIR UNA IMAGEN
    imagen_defondo = Label(canvas, image=imagen_parafondo)                                                              #ETQUETA DONDE SE COLOCARÁ LA IMAGEN
    imagen_defondo.place(x=0,y=0)
    #BOTON
    boton_empezar = Button(canvas,text="EMPEZAR",bg=azul_marino_boton,fg=blanco_letras,width=15,
    font=("SNAP ITC",20),relief="groove",command=pantalla_selector_niveles)
    boton_empezar.place(x=700,y=250)

    window.mainloop()                                                                                                   #MANTIENE MOSTRANDO LA IMAGEN CONSTANTEMENTE

def pantalla_selector_niveles():                                                                                        #SE SELECCIONA LA PROFUNDIDAD/VELOCIDAD A EMPEZAR
    #CANVAS
    canvas = Canvas(window,width=1600,height=870,bg="blue")                                                             #CANVAS DONDE SE COLOCARÁN TODOS LOS OBJETOS
    canvas.place(x=-2,y=-2)

    #LABELS
    imagen_parafondo = PhotoImage(file="imagenes/imagenes_fondos/abismo_menu.png")                                      #IMAGEN A UTILIZAR
    imagen_defondo = Label(canvas, image=imagen_parafondo)                                                              # ETQUETA DONDE SE COLOCARÁ LA IMAGEN
    imagen_defondo.place(x=0, y=0)

    label_titulo = Label(canvas,text="SELECCIONA LA PROFUNDIDAD",bg=azul_oscuro,fg="white",                             #TITULO DEL NIVEL
    width=30,height=2,font=("Press Start 2P",20),relief="sunken",borderwidth=3)
    label_titulo.place(x=450,y=250)

    Label_ingreseNombre = Label(canvas,text="Ingrese su nombre :",bg=azul_oscuro2,                                      #CUADRO DE TEXTO DONDE INDICA AL JUGADOR QUE DEBE INGRESAR SU NOMBRE
    fg="white",width=20,font=("Press Start 2P",10))
    Label_ingreseNombre.place(x=480,y=380)

    Label_profundidad = Label(canvas,text="Profundidad :",bg=azul_oscuro2,fg="white",width=20,                          #INDICA LA ZONA DONDE EL JUGADOR ELIGE LA PROFUNDIDAD
    font=("Press Start 2P",10))
    Label_profundidad.place(x=480,y=465)

    label_insis = Label(canvas,text="",bg=azul_oscuro2,fg="white",width=40,font=("SNAP ITC",12))                        #CUADRO DE TEXTO DONDE INDICA AL JUGADOR QUE DEBE PONER UN NOMBRE PEQUEÑO
    label_insis.place(x=1125,y=380)

    #BOTONES DE RADIO
    all_radiobutton = IntVar()                                                                                          #GUARDA EL VALOR DE LOS BOTONES DE RADIO

    radio_button_lvl1 = Radiobutton(canvas,text="4000 m",bg=azul_oscuro2,fg="white",                                    #BOTON DE RADIO CON VALOR 1
    font=("Press Start 2P",10),variable=all_radiobutton,value=1)
    radio_button_lvl1.place(x=760,y=460)

    radio_button_lvl2 = Radiobutton(canvas, text="7000 m",bg=azul_oscuro2,fg="white",                                   #BOTON DE RADIO CON VALOR 2
    font=("Press Start 2P",10), variable=all_radiobutton, value=2)
    radio_button_lvl2.place(x=880, y=460)

    radio_button_lvl3 = Radiobutton(canvas, text="10000 m",bg=azul_oscuro2,fg="white",                                  #BOTON DE RADIO CON VALOR 3
    font=("Press Start 2P",10), variable=all_radiobutton, value=3)
    radio_button_lvl3.place(x=1000, y=460)

    #BOTONES
    empezar = Button(canvas,text="Empezar",bg=azul_oscuro,fg="white",width=20,font=("Press Start 2P",14),                     #INICIA LOS DEMÁS NIVELES DEL JUEGO
    command= lambda: (enviar_a_nivel(cuadro_nombre.get(),all_radiobutton.get(),label_insis)))
    empezar.place(x=690,y=520)

    testing = Button(canvas,text="testing",command=game_over)
    testing.place(x=100,y=100)

    #CUADRO DE NOMBRE
    cuadro_nombre = Entry(canvas,text="Ingrese su nombre",width=30,font=("Arial",16))                                   #ES DONDE SE INGRESA EL NOMBRE DEL JUGADOR
    cuadro_nombre.place(x=780,y=380)

    window.mainloop()                                                                                                   #MANTIENE MOSTRANDO LA IMAGEN CONSTANTEMENTE

def enviar_a_nivel(nombre_jugador,valor_radio,label):                                                                         #CONDICIONA QUE EL JUGADOR INGRESE UN NOMBRE Y SELECCIONE UNA PROFUNDIDAD
    if len(nombre_jugador) != 0 and len(nombre_jugador) < 17 and valor_radio == 1:
        return nivel_Uno(nombre_jugador)
    if len(nombre_jugador) != 0 and len(nombre_jugador) < 17 and valor_radio == 2:
        return nivel_Dos(nombre_jugador)
    if len(nombre_jugador) != 0 and len(nombre_jugador) < 17 and valor_radio == 3:
        return nivel_Tres()
    if len(nombre_jugador) != 0 and len(nombre_jugador) < 17:                                                                                      #EN CASO DE NO SELECCIONAR PROFUNDIDAD, SE EMPEZARÁ EN EL NIVEL 1
        return nivel_Uno(nombre_jugador)
    else:
        return label.config(text="¡Error!: El nombre debe ser menor a 10 digitos")

def nivel_Uno(nombre):                                                                                                        #NIVEL UNO O LA PRIMERA PROFUNDIDAD


    #CANVAS
    canvas = Canvas(window,bg=azul_oscuro2,width=1600,height=870)  # CANVAS DONDE SE ALMACENARÁ TODO
    canvas.place(x=-2,y=-2)
    canvas_info_arriba= Canvas(canvas,bg=azul_oscuro3,width=1600,height=100,highlightthickness=0)  #CANVAS DONDE IRÁ DISTINTA INFORMACIÓN RELACIONADA AL NIVEL
    canvas_info_arriba.place(x=2,y=0)
    canvas_info_abajo = Canvas(canvas,bg=azul_oscuro3,width=1600,height=60,highlightthickness=0)  # CANVAS DONDE IRÁ LA INFO DEL JUGADOR, TIEMPO Y DEMÁS
    canvas_info_abajo.place(x=2,y=813)

    #LABELS
    label_nivel = Label(canvas_info_arriba,text="Profundidad-4000m",bg=azul_oscuro3,fg="white",  # UN SIMPLE LABEL QUE INDICA EL TITULO DEL NIVEL
    font=("Bodoni MT Black",26))
    label_nivel.place(x=50,y=30)

    label_nombre = Label(canvas_info_abajo,text="Capitán: " + nombre,bg=azul_oscuro3,fg="white",font=("Bodoni MT Black",16))
    label_nombre.place(x=50,y=20)

    label_segundos = Label(canvas_info_abajo,text="Segundos:",bg=azul_oscuro3,fg="white",font=("Bodoni MT Black",14))
    label_segundos.place(x=500,y=20)

    label_segundos2 = Label(canvas_info_abajo,text=0,bg=azul_oscuro3,fg="white",font=("Bodoni MT Black",14))
    label_segundos2.place(x=620,y=20)

    label_puntos = Label(canvas_info_abajo,text="Puntaje:",bg=azul_oscuro3,fg="white",font=("Bodoni MT Black",14))
    label_puntos.place(x=800,y=20)

    label_puntos2 = Label(canvas_info_abajo,text=0,bg=azul_oscuro3,fg="white",font=("Bodoni MT Black",14))
    label_puntos2.place(x=915,y=20)

    label_acuPuntos = Label(canvas_info_abajo, text="Puntos acumulados:", bg=azul_oscuro3, fg="white",font=("Bodoni MT Black", 14))
    label_acuPuntos.place(x=1250, y=20)

    label_acuPuntos2 = Label(canvas_info_abajo, text=0, bg=azul_oscuro3, fg="white",font=("Bodoni MT Black", 14))
    label_acuPuntos2.place(x=1500,y=20)



    #BOTONES
    boton_pausa = Button(canvas_info_arriba,text="PAUSA",width=7,height=1,bg="white",fg=azul_oscuro3,                   #ES EL BOTON DE PAUSA, SERÁ UTILIADO PARA DETENER LA FUNCIÓN DE LOS THREADS
    font=("SNAP ITC",12))
    boton_pausa.place(x=1200,y=30)
    boton_regresar = Button(canvas_info_arriba, text="REGRESAR", width=10, height=1, bg="white", fg=azul_oscuro3,       #BOTON UTILIZADO PARA VOLVER A LA PÁGINA DE SELECCIÓN DE NIVELES
    font=("SNAP ITC", 12),command=pantalla_selector_niveles)
    boton_regresar.place(x=1400, y=30)

    #INSTANCIA DE CLASE
    jugador = Submarino(canvas,game_over)                                                                                         #INSTANCIA DE LA CLASE SUBMARINO CON EL CANVAS DONDE SE MOSTRARÁ
    tempo = Tiempo(canvas_info_abajo,label_segundos2,label_puntos2,label_acuPuntos2)                                                                                   #INSTAMCIA DE LA CLASE TIEMPO CON EL CANVAS DONDE SE MOSTRARÁ
    leviatan = Leviatan(canvas)
    obstaculo = Obstaculos(canvas,1600,label_segundos2,-5,0)
    obstaculo2 = Obstaculos(canvas,2000, label_segundos2, -5, 0)
    obstaculo3 = Obstaculos(canvas,2400, label_segundos2, -5, 0)
    obstaculo4 = Obstaculos(canvas,2800, label_segundos2, -5, 0)

    #HILOS
    def all_Threads():  # EJECUTA LOS HILOS

        hilo_tempo = threading.Thread(target=tempo.avance_1)  # HILO QUE PROVOCA EL AVANCE CONTINUO DEL CONTADOR Y SE MUESTRA EN EL LABEL_SEG
        hilo_tempo.start()

        hilo_pez = threading.Thread(target=obstaculo.move)
        hilo_pez.start()
        hilo_pez2 = threading.Thread(target=obstaculo2.move)
        hilo_pez2.start()
        hilo_pez3 = threading.Thread(target=obstaculo3.move)
        hilo_pez3.start()
        hilo_pez4 = threading.Thread(target=obstaculo4.move)
        hilo_pez4.start()

        hil = threading.Thread(target=obstaculo.prueba)
        hil.start()

        hilo_submarino = threading.Thread(target=jugador.movement)
        hilo_submarino.start()

        hilo_levi = threading.Thread(target=leviatan.sprite)
        hilo_levi.start()
        hilo_P = threading.Thread(target=leviatan.prueba)
        hilo_P.start()

    thread_todo = threading.Thread(target=all_Threads)
    thread_todo.start()




    #HABILITAR EL USO DE TECLAS
    window.bind("<Up>",lambda e:jugador.arriba(e))  # AL PRESIONAR LA TECLA, EJECUTA EL METODO DE LA CLASE PARA CAMBIAR LA DIRECCIÓN A ARRIBA
    window.bind("<Down>",lambda e:jugador.abajo(e))  # AL PRESIONAR LA TECLA, EJECUTA EL METODO DE LA CLASE PARA CAMBIAR LA DIRECCIÓN A ABAJO
    window.bind("<Right>",lambda e:jugador.derecha(e))  # AL PRESIONAR LA TECLA, EJECUTA EL METODO DE LA CLASE PARA CAMBIAR LA DIRECCIÓN A DERECHA
    window.bind("<Left>", lambda e: jugador.izquierda(e))  # AL PRESIONAR LA TECLA, EJECUTA EL METODO DE LA CLASE PARA CAMBIAR LA DIRECCIÓN A IZQUIERDA


    window.mainloop()                                                                                                   #BUCLE PARA MANTENER LA VENTANA ABIERTA



def nivel_Dos(nombre):                                                                                                  #NIVEL DOS
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
    label_nivel = Label(canvas_info_arriba, text="Profundidad-4000m", bg=azul_oscuro3, fg="white", # UN SIMPLE LABEL QUE INDICA EL TITULO DEL NIVEL
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
                            font=("SNAP ITC", 12), command=pantalla_selector_niveles)
    boton_regresar.place(x=1400, y=30)

    # INSTANCIA DE CLASE
    jugador = Submarino(canvas, game_over)  # INSTANCIA DE LA CLASE SUBMARINO CON EL CANVAS DONDE SE MOSTRARÁ
    tempo = Tiempo(canvas_info_abajo, label_segundos2, label_puntos2,
                   label_acuPuntos2)  # INSTAMCIA DE LA CLASE TIEMPO CON EL CANVAS DONDE SE MOSTRARÁ
    obstaculo = Obstaculos(canvas, 1600, label_segundos2, -5, 0)
    obstaculo2 = Obstaculos(canvas, 2000, label_segundos2, -5, 0)
    obstaculo3 = Obstaculos(canvas, 2400, label_segundos2, -5, 0)
    obstaculo4 = Obstaculos(canvas, 2800, label_segundos2, -5, 0)

    # HILOS
    def all_Threads():
        hilo_tempo = threading.Thread(target=tempo.avance_2)  # HILO QUE PROVOCA EL AVANCE CONTINUO DEL CONTADOR Y SE MUESTRA EN EL LABEL_SEG
        hilo_tempo.start()  # EJECUTA EL HILO

        hilo_pez = threading.Thread(target=obstaculo.move)
        hilo_pez.start()
        hilo_pez2 = threading.Thread(target=obstaculo2.move)
        hilo_pez2.start()
        hilo_pez3 = threading.Thread(target=obstaculo3.move)
        hilo_pez3.start()
        hilo_pez4 = threading.Thread(target=obstaculo4.move)
        hilo_pez4.start()

        hil = threading.Thread(target=obstaculo.prueba)
        hil.start()

        hilo_submarino = threading.Thread(target=jugador.movement)
        hilo_submarino.start()

    thread_todo = threading.Thread(target=all_Threads)
    thread_todo.start()

    # HABILITAR EL USO DE TECLAS
    window.bind("<Up>", lambda e: jugador.arriba(e))  # AL PRESIONAR LA TECLA, EJECUTA EL METODO DE LA CLASE PARA CAMBIAR LA DIRECCIÓN A ARRIBA
    window.bind("<Down>", lambda e: jugador.abajo(e))  # AL PRESIONAR LA TECLA, EJECUTA EL METODO DE LA CLASE PARA CAMBIAR LA DIRECCIÓN A ABAJO
    window.bind("<Right>", lambda e: jugador.derecha(e))  # AL PRESIONAR LA TECLA, EJECUTA EL METODO DE LA CLASE PARA CAMBIAR LA DIRECCIÓN A DERECHA
    window.bind("<Left>", lambda e: jugador.izquierda(e))  # AL PRESIONAR LA TECLA, EJECUTA EL METODO DE LA CLASE PARA CAMBIAR LA DIRECCIÓN A IZQUIERDA

    window.mainloop()  # BUCLE PARA MANTENER LA VENTANA ABIERTA

    window.mainloop()



def nivel_Tres():                                                                                                       #NIVEL TRES
    #CANVAS
    canvas = Canvas(window,bg="blue",width=1600,height=870)                                                             #CANVAS DONDE SE ALMACENA TODO
    canvas.place(x=-2,y=-2)

def game_over():
    #CANVAS
    canvas = Canvas(window,width=1600,height=870,bg="black")
    canvas.place(x=-2,y=-2)

    #LABELS
    label_titulo = Label(canvas,text="JUEGO TERMINADO",font=("Press Start 2P",40),bg="black",fg="white")
    label_titulo.place(x=400,y=300)

    imagen_destroy = PhotoImage(file="imagenes/imagenes_cosas/submarino_destruido.png")
    label_destroy = Label(canvas, image=imagen_destroy,highlightthickness=0,bd=0)
    label_destroy.place(x=1260,y=250)

    #BOTONES
    volver = Button(canvas,text="VOLVER",font=("Press Start 2P",20),bg="black",fg="white",command=pantalla_selector_niveles)
    volver.place(x=400,y=500)

    puntajes = Button(canvas,text="PUNTAJES",font=("Press Start 2P",20),bg="black",fg="white")
    puntajes.place(x=800,y=500)

    window.mainloop()






















#LAS BASES DE LAS DIFERENTES PANTALLAS

window = Tk()
window.title("THE ABYSS")
window.geometry("1600x870")
window.resizable(False,False)
pantalla_main()