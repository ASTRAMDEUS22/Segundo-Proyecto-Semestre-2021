from tkinter import *

class Submarino:
    def __init__(self,canvas,pantalla_Gameover):

        #CONSTRUCTORES
        self.canvas = canvas
        self.x = 450
        self.y = 425
        self.x_velocity = 0
        self.y_velocity = 0
        self.pantalla_Gameover = pantalla_Gameover
        """
        # IMAGENES
        self.image_1 = PhotoImage(file="imagenes/imagenes_cosas/submarino1.png")
        self.image_2 = PhotoImage(file="imagenes/imagenes_cosas/submarino2.png")
        self.image_3 = PhotoImage(file="imagenes/imagenes_cosas/submarino3.png")
        self.image_4 = PhotoImage(file="imagenes/imagenes_cosas/submarino4.png")
        self.lista_sprite = [self.image_1, self.image_2, self.image_3, self.image_4]
        """

        self.imagen = PhotoImage(file="imagenes/imagenes_cosas/submarino1.png")
        self.submarino = self.canvas.create_image(self.x,self.y,image=self.imagen)


    def movement(self):
        self.x_coords,self.y_coords = self.canvas.coords(self.submarino)
        self.canvas.move(self.submarino,self.x_velocity - 2,self.y_velocity)

        self.choca = False
        if self.x_coords < 0:
            self.choca = True
        if self.choca is True:
            return self.pantalla_Gameover()
        self.canvas.after(10, self.movement)

    def arriba(self, event):
        #print(self.x_velocity, self.y_velocity)
        print(event.keysym)

        self.x_velocity = 0
        self.y_velocity = -10

    def abajo(self, event):
        #print(self.x_velocity, self.y_velocity)
        print(event.keysym)

        self.x_velocity = -1
        self.y_velocity = 10

    def derecha(self,event):
        #print(self.x_velocity, self.y_velocity)
        print(event.keysym)

        self.x_velocity = 10
        self.y_velocity = 0

    def izquierda(self,event):
        #print(self.x_velocity, self.y_velocity)
        print(event.keysym)

        self.x_velocity = -10
        self.y_velocity = 0