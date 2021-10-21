from tkinter import *
import random

class Obstaculos:
    def __init__(self,canvas,xPosition,velocidad_x,velocidad_y,submarino,pantalla_gameover,canva_arriba,canva_abajo,tiempo,nombre):
        self.canvas = canvas
        self.canva_arriba = canva_arriba
        self.canva_abajo = canva_abajo
        self.submarino = submarino
        self.x_velocidad = velocidad_x
        self.y_velocidad = velocidad_y
        self.nombre = nombre  # NOMBRE DEL JUGADOR
        self.tiempo = tiempo  #TIEMPO Y PUNTAJES DEL JUGADOR

        self.xPosition = xPosition
        self.pantalla_gamerover = pantalla_gameover
        self.image = PhotoImage(file="imagenes/imagenes_cosas/obstaculo_pez2.png")
        self.obstaculo = self.canvas.create_image(self.xPosition, random.randrange(100,790), image=self.image)
        self.p = 0


    def move(self):  #MUEVE LOS OBSTACULOS
        self.x2,self.y2 = self.canvas.coords(self.obstaculo)
        xsub = self.submarino.x
        ysub = self.submarino.y
        self.impacto = False
        self.resultado = self.tiempo.resultado
        #print(xsub,ysub)
        #print("coords",self.x2,self.y2)

        if self.x2 <= -1700:  # SI EL OBSTACULO TOCA LA IZQUIERDA, SE VUELVE A "GENERAR" EN UNA POSICION EN Y ALEATORIA ENTRE 100 Y 790
            self.x2 = self.xPosition
            self.y2 = random.randrange(100,790)
            self.canvas.coords(self.obstaculo,self.x2,self.y2)
        if xsub <= self.x2 <= xsub and ysub <= self.y2 <= ysub + 20:  #CHOQUE CON EL JUGADOR
            return self.pantalla_gamerover(self.canva_arriba,self.canvas,self.canva_abajo,self.nombre,self.resultado)


        self.canvas.move(self.obstaculo,self.x_velocidad,self.y_velocidad)
        self.canvas.after(10,self.move)  # HACE UN AFTER DE 10 MS PARA "ANIMAR" LOS OBSTACULOS

    def prueba(self):
        #print(self.p)
        if self.p <= 1000:
            self.p = self.p + 1
        self.canvas.after(1000,self.prueba)
