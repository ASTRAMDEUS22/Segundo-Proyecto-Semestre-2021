from tkinter import *
import random

class Obstaculos:
    def __init__(self,canvas,xPosition,label_segundos,velocidad_x,velocidad_y):
        self.canvas = canvas
        self.x_velocidad = velocidad_x
        self.y_velocidad = velocidad_y
        self.segundos = label_segundos
        self.xPosition = xPosition
        self.image = PhotoImage(file="imagenes/imagenes_cosas/obstaculo_pez2.png")
        self.obstaculo = self.canvas.create_image(self.xPosition, random.randrange(100,790), image=self.image)
        self.p = 0


    def move(self):
        self.x,self.y = self.canvas.coords(self.obstaculo)
        #print(self.x,self.y)
        self.impacto = False

        if self.x <= -1700:
            self.x = self.xPosition
            self.y = random.randrange(100,790)
            self.canvas.coords(self.obstaculo,self.x,self.y)
        self.canvas.move(self.obstaculo,self.x_velocidad,self.y_velocidad)
        self.canvas.after(10,self.move)

    def prueba(self):
        #print(self.p)
        if self.p <= 1000:
            self.p = self.p + 1
        self.canvas.after(1000,self.prueba)
