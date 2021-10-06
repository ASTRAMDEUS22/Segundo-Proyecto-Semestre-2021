from tkinter import *

class Leviatan:
    def __init__(self,canvas):
        #CONSTRUCTOR
        self.canvas = canvas
        self.p = 0
        #IMAGENES
        self.image1 = PhotoImage(file="imagenes/imagenes_cosas/leviatan_1.png")
        self.image3 = PhotoImage(file="imagenes/imagenes_cosas/leviatan_3.png")
        #INSTAN IMAGENES
        self.leviatan_1 = self.canvas.create_image(102 ,-2000,image=self.image1)
        self.leviatan_3 = self.canvas.create_image(102, -2000, image=self.image3)

    def sprite(self):
        self.x1_coords,self.y1_coords = self.canvas.coords(self.leviatan_1)
        self.x3_coords, self.y3_coords = self.canvas.coords(self.leviatan_3)
        """
        if self.p == 5:
            self.x1_coords = 102
            self.y1_coords = 440
            self.canvas.coords(self.leviatan_1,self.x1_coords,self.y1_coords)
        else:
            self.x1_coords = 102
            self.y1_coords = -2000
            self.canvas.coords(self.leviatan_1, self.x1_coords, self.y1_coords)
        if self.p == 6:
            self.x2_coords = 102
            self.y2_coords = 440
            self.canvas.coords(self.leviatan_2, self.x2_coords, self.y2_coords)
        else:
            self.x2_coords = 102
            self.y2_coords = -2000
            self.canvas.coords(self.leviatan_2, self.x2_coords, self.y2_coords)
        if self.p == 7:
            self.x3_coords = 102
            self.y3_coords = 440
            self.canvas.coords(self.leviatan_3, self.x3_coords, self.y3_coords)
        else:
            self.x3_coords = 102
            self.y3_coords = -2000
            self.canvas.coords(self.leviatan_3, self.x3_coords, self.y3_coords)
            """

        if (self.p % 2) == 0:
            self.x1_coords = 102
            self.y1_coords = 440
            self.canvas.coords(self.leviatan_1, self.x1_coords, self.y1_coords)
        else:
            self.x1_coords = 102
            self.y1_coords = -2000
            self.canvas.coords(self.leviatan_1, self.x1_coords, self.y1_coords)
        if (self.p % 2) == 1:
            self.x3_coords = 102
            self.y3_coords = 440
            self.canvas.coords(self.leviatan_3, self.x3_coords, self.y3_coords)
        else:
            self.x3_coords = 102
            self.y3_coords = -2000
            self.canvas.coords(self.leviatan_3, self.x3_coords, self.y3_coords)



        self.canvas.after(1000,self.sprite)

    def prueba(self):
        print(self.p)
        if self.p <= 1000:
            self.p = self.p + 1
        self.canvas.after(1000,self.prueba)