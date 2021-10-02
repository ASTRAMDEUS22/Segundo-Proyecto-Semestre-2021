#BIBLIOTECAS A UTILIZAR
from tkinter import *
#import time
#import pygame

#CLASES
class Submarino:
    def __init__(self,canvas):
        #CONSTRUCTORES
        self.canvas = canvas
        self.x = 300
        self.y = 300
        self.move_x = 0
        self.move_y = 0
        self.imagen_parafondo = PhotoImage(file="imagenes/imagenes_fondos/abismo_nivel1.png")
        self.imagen_defondo = Label(canvas, image=self.imagen_parafondo)  # SE COLOCA LA IMAGEN
        #self.imagen_defondo.place(x=0, y=0)
        self.imagen = PhotoImage(file="imagenes/imagenes_cosas/submarino.png")
        self.submarino = self.canvas.create_image(self.x,self.y,image=self.imagen)


        self.move()


    def move(self):
        self.x_coords, self.y_coords = self.canvas.coords(self.submarino)
        print(self.y_coords)
        if self.y_coords >= 180:
            self.canvas.move(self.submarino, self.move_x, self.move_y)
            self.canvas.after(10, self.move)

        """
        if self.y_coords >= 140:
            self.canvas.move(self.submarino,self.move_x,self.move_y)
        else:
            self.canvas.move(self.submarino,0,0)
        if self.y_coords <= 600:
            self.canvas.move(self.submarino, self.move_x, self.move_y)
        else:
            self.canvas.move(self.submarino, 0, 0)
        """





    def arriba(self,event):
        print(event.keysym)
        if self.y_coords >= 180:
            self.move_x = 0
            self.move_y = -2
        else:
            self.move_x = 0
            self.move_y = 0




    def abajo(self,event):
        print(event.keysym)
        if self.y_coords >= 180:
            self.move_x = 0
            self.move_y = 2
        else:
            self.move_x = 0
            self.move_y = 0





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

    label_titulo = Label(canvas,text="SELECCIONA LA PROFUNDIDAD",bg=azul_oscuro,fg="snow3",                             #TITULO DEL NIVEL
    width=30,height=2,font=("SNAP ITC",20),relief="sunken",borderwidth=3)
    label_titulo.place(x=500,y=250)

    Label_ingreseNombre = Label(canvas,text="Ingrese su nombre :",bg=azul_oscuro2,                                      #CUADRO DE TEXTO DONDE INDICA AL JUGADOR QUE DEBE INGRESAR SU NOMBRE
    fg="snow3",width=20,font=("SNAP ITC",13))
    Label_ingreseNombre.place(x=480,y=380)

    Label_profundidad = Label(canvas,text="Profundidad :",bg=azul_oscuro2,fg="snow3",width=20,font=("SNAP ITC",13))     #INDICA LA ZONA DONDE EL JUGADOR ELIGE LA PROFUNDIDAD
    Label_profundidad.place(x=480,y=460)

    #BOTONES DE RADIO
    all_radiobutton = IntVar()                                                                                          #GUARDA EL VALOR DE LOS BOTONES DE RADIO

    radio_button_lvl1 = Radiobutton(canvas,text="4000 m",bg=azul_oscuro2,fg="white",                                    #BOTON DE RADIO CON VALOR 1
    font=("SNAP ITC",11),variable=all_radiobutton,value=1)
    radio_button_lvl1.place(x=730,y=460)

    radio_button_lvl2 = Radiobutton(canvas, text="7000 m",bg=azul_oscuro2,fg="white",                                   #BOTON DE RADIO CON VALOR 2
    font=("SNAP ITC",11), variable=all_radiobutton, value=2)
    radio_button_lvl2.place(x=850, y=460)

    radio_button_lvl3 = Radiobutton(canvas, text="10000 m",bg=azul_oscuro2,fg="white",                                  #BOTON DE RADIO CON VALOR 3
    font=("SNAP ITC",11), variable=all_radiobutton, value=3)
    radio_button_lvl3.place(x=970, y=460)

    #BOTONES
    empezar = Button(canvas,text="Empezar",bg=azul_oscuro,fg="snow3",width=20,font=("SNAP ITC",14),                     #INICIA LOS DEMÁS NIVELES DEL JUEGO
    command= lambda: (enviar_a_nivel(cuadro_nombre.get(),all_radiobutton.get())))
    empezar.place(x=680,y=520)

    #CUADRO DE NOMBRE
    cuadro_nombre = Entry(canvas,text="Ingrese su nombre",width=30,font=("Arial",16))                                   #ES DONDE SE INGRESA EL NOMBRE DEL JUGADOR
    cuadro_nombre.place(x=720,y=380)

    window.mainloop()                                                                                                   #MANTIENE MOSTRANDO LA IMAGEN CONSTANTEMENTE

def enviar_a_nivel(nombre_jugador,valor_radio):                                                                         #CONDICIONA QUE EL JUGADOR INGRESE UN NOMBRE Y SELECCIONE UNA PROFUNDIDAD
    if len(nombre_jugador) != 0 and valor_radio == 1:
        return nivel_Uno()
    elif len(nombre_jugador) != 0 and valor_radio == 2:
        return nivel_Dos()
    elif len(nombre_jugador) != 0 and valor_radio == 3:
        return nivel_Tres()
    elif len(nombre_jugador) != 0:                                                                                      #EN CASO DE NO SELECCIONAR PROFUNDIDAD, SE EMPEZARÁ EN EL NIVEL 1
        return nivel_Uno()


def nivel_Uno():                                                                                                        #NIVEL UNO O LA PRIMERA PROFUNDIDAD
    #CANVAS
    canvas = Canvas(window,bg=azul_oscuro2,width=1600,height=870)                                                       #CANVAS DONDE SE ALMACENARÁ TODO
    canvas.place(x=-2,y=-2)
    canvas_info_arriba= Canvas(canvas,bg=azul_oscuro3,width=1600,height=100,highlightthickness=0)                       #CANVAS DONDE IRÁ DISTINTA INFORMACIÓN RELACIONADA AL NIVEL
    canvas_info_arriba.place(x=2,y=0)
    canvas_info_abajo = Canvas(canvas,bg=azul_oscuro3,width=1600,height=100,highlightthickness=0)
    canvas_info_abajo.place(x=2,y=772)

    #LABELS
    label_nivel = Label(canvas_info_arriba,text="Profundidad-4000m",bg=azul_oscuro3,fg="white",
    font=("Bodoni MT Black",26))
    label_nivel.place(x=50,y=30)
    #BOTONES
    boton_pausa = Button(canvas_info_arriba,text="PAUSA",width=7,height=1,bg="white",fg=azul_oscuro3,
    font=("SNAP ITC",12))
    boton_pausa.place(x=1200,y=30)
    boton_regresar = Button(canvas_info_arriba, text="REGRESAR", width=10, height=1, bg="white", fg=azul_oscuro3,
    font=("SNAP ITC", 12),command=pantalla_selector_niveles)
    boton_regresar.place(x=1400, y=30)

    #INSTANCIA DE CLASE
    jugador = Submarino(canvas)


    #HABILITAR EL USO DE TECLAS
    window.bind("<Up>",lambda e:jugador.arriba(e))                                                                      #AL PRESIONAR LA TECLA, EJECUTA EL METODO DE LA CLASE PARA CAMBIAR LA DIRECCIÓN A ARRIBA
    window.bind("<Down>",lambda e:jugador.abajo(e))                                                                     #AL PRESIONAR LA TECLA, EJECUTA EL METODO DE LA CLASE PARA CAMBIAR LA DIRECCIÓN A ABAJO

    window.mainloop()                                                                                                   #BUCLE PARA MANTENER LA VENTANA ABIERTA

def nivel_Dos():                                                                                                        #NIVEL DOS
    #CANVAS
    canvas = Canvas(window,bg="green",width=1600,height=870)                                                            #CANVAS DONDE SE ALMACENA TODO
    canvas.place(x=-2,y=-2)


def nivel_Tres():                                                                                                       #NIVEL TRES
    #CANVAS
    canvas = Canvas(window,bg="blue",width=1600,height=870)                                                             #CANVAS DONDE SE ALMACENA TODO
    canvas.place(x=-2,y=-2)
























#LAS BASES DE LAS DIFERENTES PANTALLAS

window = Tk()
window.title("THE ABYSS")
window.geometry("1600x870")
window.resizable(False,False)
pantalla_main()