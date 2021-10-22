from tkinter import *
import pygame


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


class Tiempo:
    def __init__(self,canvas_arriba,canvas,canvas_abajo,label_segs,label_puntaje,label_acumulado,pantalla_gameover,nombre):
        self.canvas_arriba = canvas_arriba
        self.canvas = canvas
        self.canvas_abajo = canvas_abajo
        self.seg = 0
        self.minute = 0
        self.puntaje = 0
        self.pantalla_gameover = pantalla_gameover
        self.nombre = nombre
        self.label_seg = label_segs
        self.label_puntaje = label_puntaje
        self.label_acumulado = label_acumulado
        self.puntajeMax = 0
        self.resultado = 0
        self.sonido = pygame.mixer.Sound("Musica/monstruo_roar.ogg")
        self.sonido.set_volume(0.2)

    def avance_1(self):  #AVANZA EL TIEMPO Y PUNTAJE DE 1 EN 1
        #print("segundo: ", self.seg)
        #print("minuto: ", self.minute)

        if self.seg <= 1000:
            self.seg = self.seg + 1
            self.puntaje = self.puntaje + 1

        self.resultado = self.seg + self.puntajeMax

        if self.seg == 40:
            return self.pantalla_gameover(self.canvas_arriba,self.canvas,self.canvas_abajo,self.nombre,self.resultado)
        if self.seg == 39:
            self.puntajeMax = self.puntajeMax + 20
        elif self.seg == 79:
            self.puntajeMax = self.puntajeMax + 20
        elif self.seg == 119:
            self.puntajeMax = self.puntajeMax + 20

        if self.seg == 0 or self.seg == 7 or self.seg == 13 or self.seg == 19 or self.seg == 26 or self.seg == 31 or self.seg == 38:
            self.sonido.play()  #INICIA EL SONIDO DEL MONSTRUO
        if self.seg >= 40:
            self.sonido.stop()  #DETIENE EL SONIDO DEL MONSTRUO


        self.canvas_abajo.after(1000,self.avance_1)  #ESPERA 1 SEGUNDO PARA EL CONTADOR
        self.label_seg.config(text=self.seg)
        self.label_puntaje.config(text=self.puntaje)
        self.label_acumulado.config(text=self.puntajeMax)

    def avance_2(self):  #AVANZA EL TIEMPO DE 1 EN 1 Y PUNTAJE DE 3 EN 3
        #print("segundo: ", self.seg)
        #print("minuto: ", self.minute)

        if self.seg <= 1000:
            self.seg = self.seg + 1
            self.puntaje = self.puntaje + 3

        self.resultado = self.puntaje + self.puntajeMax

        if self.seg == 40:
            return self.pantalla_gameover(self.canvas_arriba, self.canvas, self.canvas_abajo, self.nombre,self.resultado)
        if self.seg == 39:
            self.puntajeMax = self.puntajeMax + 20
        elif self.seg == 79:
            self.puntajeMax = self.puntajeMax + 20
        elif self.seg == 119:
            self.puntajeMax = self.puntajeMax + 20

        if self.seg == 0 or self.seg == 7 or self.seg == 13 or self.seg == 19 or self.seg == 26 or self.seg == 31 or self.seg == 38:
            self.sonido.play()
        if self.seg >= 40:
            self.sonido.stop()


        self.canvas_abajo.after(1000,self.avance_2)
        self.label_seg.config(text=self.seg)
        self.label_puntaje.config(text=self.puntaje)
        self.label_acumulado.config(text=self.puntajeMax)

    def avance_3(self):  #AVANZA EL TIEMPO DE 1 EN 1 Y PUNTAJE DE 5 EN 5
        #print("segundo: ", self.seg)
        #print("minuto: ", self.minute)

        if self.seg <= 1000:
            self.seg = self.seg + 1
            self.puntaje = self.puntaje + 5

        self.resultado = self.puntaje + self.puntajeMax

        if self.seg == 39:
            self.puntajeMax = self.puntajeMax + 20
        elif self.seg == 79:
            self.puntajeMax = self.puntajeMax + 20
        elif self.seg == 119:
            self.puntajeMax = self.puntajeMax + 20

        if self.seg == 0 or self.seg == 7 or self.seg == 13 or self.seg == 19 or self.seg == 26 or self.seg == 31 or self.seg == 38:
            self.sonido.play()
        if self.seg >= 40:
            self.sonido.stop()


        self.canvas_abajo.after(1000,self.avance_3)
        self.label_seg.config(text=self.seg)
        self.label_puntaje.config(text=self.puntaje)
        self.label_acumulado.config(text=self.puntajeMax)