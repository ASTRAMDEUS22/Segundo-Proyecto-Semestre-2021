from tkinter import *
from class_Obstaculos import *


class Submarino:
    def __init__(self,canvas,x_velocity,pantalla_Gameover,canvas_arriba,canvas_abajo,tiempo,nombre):

        #CONSTRUCTORES
        self.canvas = canvas
        self.canvas_arriba = canvas_arriba
        self.canvas_abajo = canvas_abajo
        self.x = 600  #POSICION EN X INICIAL
        self.y = 425  #POSICION EN Y INICIAL
        self.x_velocity = x_velocity  #VELOCIDAD EN EL EJE X
        self.y_velocity = 0  #VELOCIDAD EN EL EJE Y
        self.pantalla_Gameover = pantalla_Gameover  #PANTALLA EN CASO DE PERDER
        self.imagen = PhotoImage(file="imagenes/imagenes_cosas/submarino1.png")  #SE ESCOGE LA FOTO DEL SUBMARINO
        self.submarino = self.canvas.create_image(self.x,self.y,image=self.imagen)  #SE CREA UN SUBMARINO
        self.nombre = nombre  #NOMBRE DEL JUGADOR
        self.tiempo = tiempo  #TIEMPO EN EL JUEGO


    def movement(self):
        self.x_coords,self.y_coords = self.canvas.coords(self.submarino)  #COORDS DEL SUBMARINO
        self.x,self.y = self.x_coords,self.y_coords  # LAS COORDENADAS EN X y Y DEL SUBMARINO SE EDITAN
        self.canvas.move(self.submarino,self.x_velocity - 5,self.y_velocity)  # SE MUEVE EL SUBMARINO CONSTANTEMENTE HACIA EL BORDE IZQUIERDO
        self.resultado = self.tiempo.resultado  # SE ENVIA A LA PANTALLA GAME OVER EL RESULTADO DE LA SUMA ENTRE PUNTOS ACUMULADOS Y LOS PUNTOS DEL NIVEL

        if self.x_coords >= 1480:  #DELIMITA EL CHOQUE CON EL BORDE DERECHO
            self.canvas.coords(self.submarino,1479,self.y_coords)
        if self.y_coords <= 169:  #DELIMITA EL CHOQUE CON EL BORDE SUPERIOR
            self.canvas.coords(self.submarino,self.x_coords,170)
        if self.y_coords >= 750:  #DELIMITA EL CHOQUE CON EL BORDE INFERIOR
            self.canvas.coords(self.submarino,self.x_coords,749)
        self.choca = False  #  MATIENE INFORMANDO SI EL SUBMARINO NO HA TOCADO EL BORDE IZQUIERDO

        if self.x_coords < 0:  # SI EL SUBMARINO SE VA MUY A LA IZQUIERDA "CHOCA CON EL BORDE"
            self.choca = True

        if self.choca is True:  # SI CHOCA CON LA IZQUIERSA EL JUGADOR MUERE
            return self.pantalla_Gameover(self.canvas_arriba,self.canvas,self.canvas_abajo,self.nombre,self.resultado)

        self.canvas.after(10, self.movement)

    def arriba(self, event):  # MOVIMIENTO HACIA ARRIBA
        #print(self.x_velocity, self.y_velocity)
        #print(event.keysym)

        self.x_velocity = 0
        self.y_velocity = -10


    def abajo(self, event):  # MOVIMIENTO HACIA ABAJO
        #print(self.x_velocity, self.y_velocity)
        #print(event.keysym)

        self.x_velocity = -1
        self.y_velocity = 10

    def derecha(self,event):  # MOVIMIENTO HACIA DERECHA
        #print(self.x_velocity, self.y_velocity)
        #print(event.keysym)

        self.x_velocity = 10
        self.y_velocity = 0

    def izquierda(self,event):  # MOVIMIENTO HACIA IZQUIERDA
        #print(self.x_velocity, self.y_velocity)
        #print(event.keysym)

        self.x_velocity = -10
        self.y_velocity = 0