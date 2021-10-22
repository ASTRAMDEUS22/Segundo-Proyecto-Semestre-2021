from tkinter import *

class imagen:
    def __init__(self,canvas,x_velocity):
        self.canvas = canvas
        self.x_velocity = x_velocity
        self.image1 = PhotoImage(file="imagenes/imagenes_fondos/fondo1.gif")
        self.fondo1 = self.canvas.create_image(802,437,image=self.image1)  #ESTA VA EN X EN 802
        self.image2 = PhotoImage(file="imagenes/imagenes_fondos/fondo2.gif")
        self.fondo2 = self.canvas.create_image(2402,437,image=self.image2)

    def movimient(self):
        self.xcoords_imagen1,self.ycoords_imagen1 = self.canvas.coords(self.fondo1)
        #print(self.xcoords_imagen1,self.ycoords_imagen1)
        self.xcoords_imagen2, self.ycoords_imagen2 = self.canvas.coords(self.fondo2)
        #print(self.xcoords_imagen2, self.ycoords_imagen2)

        if self.xcoords_imagen1 < -800:
            self.canvas.coords(self.fondo1,2395,437)
        if self.xcoords_imagen2 < -797:
            self.canvas.coords(self.fondo2,2402,437)

        self.canvas.move(self.fondo1,self.x_velocity,0)
        self.canvas.move(self.fondo2, self.x_velocity, 0)
        self.canvas.after(10,self.movimient)