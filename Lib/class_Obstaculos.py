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
        self.resultado = self.tiempo.resultado
        #print(xsub,ysub)
        #print("coords",self.x2,self.y2)

        #SUBMARINO
        self.canvas_submarino = self.submarino.canvas
        self.jugador = self.submarino.submarino
        self.colision_jugador = self.canvas_submarino.bbox(self.jugador)
        #print(self.colision_jugador)

        #OBSTACULO
        self.colision_obstaculo = self.canvas.bbox(self.obstaculo)
        #print(self.colision_obstaculo)

        if self.x2 <= -1700:  # SI EL OBSTACULO TOCA LA IZQUIERDA, SE VUELVE A "GENERAR" EN UNA POSICION EN Y ALEATORIA ENTRE 100 Y 790
            self.x2 = self.xPosition
            self.y2 = random.randrange(100,790)
            self.canvas.coords(self.obstaculo,self.x2,self.y2)
        if self.colision_obstaculo[2]>self.colision_jugador[0]>self.colision_obstaculo[0] and self.colision_obstaculo[2]<self.colision_jugador[3]<self.colision_obstaculo[3]:
            return self.pantalla_gamerover(self.canva_arriba,self.canvas,self.canva_abajo,self.nombre,self.resultado)


        self.canvas.move(self.obstaculo,self.x_velocidad,self.y_velocidad)
        self.canvas.after(10,self.move)  # HACE UN AFTER DE 10 MS PARA "ANIMAR" LOS OBSTACULOS

    def prueba(self):  #INNECESARIO
        #print(self.p)
        if self.p <= 1000:
            self.p = self.p + 1
        #self.canvas.after(1000,self.prueba)
