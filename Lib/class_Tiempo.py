from tkinter import *


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
    def __init__(self,canvas,label_segs,label_puntaje,label_acumulado):
        self.canvas = canvas
        self.seg = 0
        self.minute = 0
        self.puntaje = 0
        self.label_seg = label_segs
        self.label_puntaje = label_puntaje
        self.label_acumulado = label_acumulado
        self.puntajeMax = 0


    def avance_1(self):
        #print("segundo: ", self.seg)
        #print("minuto: ", self.minute)

        if self.seg <= 1000:
            self.seg = self.seg + 1
            self.puntaje = self.puntaje + 1
        #else:
         #   self.minute = self.minute + 1
            #self.seg = 0

        if self.seg == 40:
            self.puntajeMax = self.puntajeMax + 20
        elif self.seg == 80:
            self.puntajeMax = self.puntajeMax + 20
        elif self.seg == 120:
            self.puntajeMax = self.puntajeMax + 20


        self.canvas.after(1000,self.avance_1)
        self.label_seg.config(text=self.seg)
        self.label_puntaje.config(text=self.puntaje)
        self.label_acumulado.config(text=self.puntajeMax)

    def avance_2(self):
        #print("segundo: ", self.seg)
        #print("minuto: ", self.minute)

        if self.seg <= 1000:
            self.seg = self.seg + 1
            self.puntaje = self.puntaje + 3
        #else:
         #   self.minute = self.minute + 1
            #self.seg = 0

        if self.seg == 40:
            self.puntajeMax = self.puntajeMax + 20
        elif self.seg == 80:
            self.puntajeMax = self.puntajeMax + 20
        elif self.seg == 120:
            self.puntajeMax = self.puntajeMax + 20


        self.canvas.after(1000,self.avance_2)
        self.label_seg.config(text=self.seg)
        self.label_puntaje.config(text=self.puntaje)
        self.label_acumulado.config(text=self.puntajeMax)

    def avance_3(self):
        #print("segundo: ", self.seg)
        #print("minuto: ", self.minute)

        if self.seg <= 1000:
            self.seg = self.seg + 1
            self.puntaje = self.puntaje + 5
        #else:
         #   self.minute = self.minute + 1
            #self.seg = 0

        if self.seg == 40:
            self.puntajeMax = self.puntajeMax + 20
        elif self.seg == 80:
            self.puntajeMax = self.puntajeMax + 20
        elif self.seg == 120:
            self.puntajeMax = self.puntajeMax + 20


        self.canvas.after(1000,self.avance_3)
        self.label_seg.config(text=self.seg)
        self.label_puntaje.config(text=self.puntaje)
        self.label_acumulado.config(text=self.puntajeMax)