from tkinter import *

from functions.camera_functions import open_camera_tkinter
#-------------------------------------------------------------------
#      Creación ventana
#-------------------------------------------------------------------

myWindow = Tk()
myWindow.geometry("985x450")
myWindow.title("Detección de Cámara")
myWindow['bg'] = '#060836'

Titulo=Label(text="Detección de Cámara" ,font=("Cambria",15),fg="#060836" , bg="#703ABE", width="893", height="3")

Titulo.pack()

#-------------------------------------------------------------------
#      Box_1: Cámara Inferior
#-------------------------------------------------------------------
box1=Label(bg="#1E136E", width="40", height="20")
box1.place(x=25, y=100)

titulo_camara_inferior = Label(text = "Cámara Inferior", font=("Cambria",15),fg="#1EEB74" , bg="#1E136E", width="25", height="1")
titulo_camara_inferior.place(x=40, y=100)

f=Frame(myWindow,height=1,width=260,bg="#1EEB74")
f.place(x=40, y=133)

dimensiones_camara_inferior = Label(text = "Dimensiones de la Cámara Inferior", font=("Cambria",15),fg="#1EEB74" , bg="#1E136E", width="25", height="1")
dimensiones_camara_inferior.place(x=50, y=150)


ancho_camara_inferior = Label(text = "Ancho: ", font=("Cambria",15),fg="#1EEB74" , bg="#1E136E")
ancho_camara_inferior.place(x=50, y=200)
ancho_camara_inferior_input = Entry(width = "6",bg="#B6ADE4", fg="#000000")
ancho_camara_inferior_input.insert(END, '640')
ancho_camara_inferior_input.place(x=100, y=200)


alto_camara_inferior = Label(text = "Alto: ", font=("Cambria",15),fg="#1EEB74" , bg="#1E136E")
alto_camara_inferior.place(x=190, y=200)
alto_camara_inferior_input = Entry(width = "6",bg="#B6ADE4", fg="#000000")
alto_camara_inferior_input.insert(END, '480')
alto_camara_inferior_input.place(x=240, y=200)

color_camara_inferior = Label(text = "Colores de la Cámara Inferior", font=("Cambria",15),fg="#1EEB74" , bg="#1E136E", width="25", height="1")
color_camara_inferior.place(x=50, y=270)

min_color_inferior = Label(text = " Min: ", font=("Cambria",15),fg="#1EEB74" , bg="#1E136E")
min_color_inferior.place(x=40, y=320)
min_color_inferior_input = Entry(width = "10",bg="#B6ADE4", fg="#000000")
min_color_inferior_input.insert(END, '50 50 100')
min_color_inferior_input.place(x=80, y=320)

max_color_inferior = Label(text = "Max: ", font=("Cambria",15),fg="#1EEB74" , bg="#1E136E")
max_color_inferior.place(x=185, y=320)
max_color_inferior_input = Entry(width = "10",bg="#B6ADE4", fg="#000000")
max_color_inferior_input.insert(END, '80 80 255')
max_color_inferior_input.place(x=220, y=320)

abrir_camara_inferior = Button(myWindow, text = "Abrir Camara", width="28", bg="#B6ADE4", command=lambda: open_camera_tkinter(
    0, #Numero de la Camara
    ancho_camara_inferior_input.get(),
    alto_camara_inferior_input.get(),
    min_color_inferior_input.get(),
    max_color_inferior_input.get()
))
abrir_camara_inferior.place(x=40, y=380)

#-------------------------------------------------------------------
#      Box_2: Cámara Superior
#-------------------------------------------------------------------
box2=Label(bg="#1E136E", width="40", height="20")
box2.place(x=350, y=100)

titulo_camara_superior = Label(text = "Cámara Superior", font=("Cambria",15),fg="#1EEB74" , bg="#1E136E", width="25", height="1")
titulo_camara_superior.place(x=350, y=100)

f1=Frame(myWindow,height=1,width=260,bg="#1EEB74")
f1.place(x=350, y=133)


dimensiones_camara_superior = Label(text = "Dimensiones de la Cámara Superior", font=("Cambria",15),fg="#1EEB74" , bg="#1E136E", width="25", height="1")
dimensiones_camara_superior.place(x=350, y=150)

ancho_camara_superior = Label(text = "Ancho:", font=("Cambria",15),fg="#1EEB74" , bg="#1E136E")
ancho_camara_superior.place(x=350, y=200)
ancho_camara_superior_input = Entry(width = "6",bg="#B6ADE4", fg="#000000")
ancho_camara_superior_input.insert(END, '640')
ancho_camara_superior_input.place(x=400, y=200)


alto_camara_superior = Label(text = "Alto: ", font=("Cambria",15),fg="#1EEB74" , bg="#1E136E")
alto_camara_superior.place(x=490, y=200)
alto_camara_superior_input = Entry(width = "6",bg="#B6ADE4", fg="#000000")
alto_camara_superior_input.insert(END, '480')
alto_camara_superior_input.place(x=540, y=200)

color_camara_superior = Label(text = "Colores de la Cámara Superior", font=("Cambria",15),fg="#1EEB74" , bg="#1E136E", width="25", height="1")
color_camara_superior.place(x=350, y=270)

min_color_superior = Label(text = " Min: ", font=("Cambria",15),fg="#1EEB74" , bg="#1E136E")
min_color_superior.place(x=340, y=320)
min_color_superior_input = Entry(width = "10",bg="#B6ADE4", fg="#000000")
min_color_superior_input.insert(END, 'R G B')
min_color_superior_input.place(x=380, y=320)

max_color_superior = Label(text = "Max: ", font=("Cambria",15),fg="#1EEB74" , bg="#1E136E")
max_color_superior.place(x=485, y=320)
max_color_superior_input = Entry(width = "10",bg="#B6ADE4", fg="#000000")
max_color_superior_input.insert(END, 'R G B')
max_color_superior_input.place(x=520, y=320)

abrir_camara_superior = Button(myWindow, text = "Abrir Camara", width="28", bg="#B6ADE4", command=lambda: open_camera_tkinter(
    1, # Numero de la camara
    ancho_camara_superior_input.get(),
    alto_camara_superior_input.get(),
    min_color_superior_input.get(),
    max_color_superior_input.get()
))
abrir_camara_superior.place(x=340, y=380)

#-------------------------------------------------------------------
#      Box_3: ...
#-------------------------------------------------------------------
box3=Label(bg="#1E136E", width="40", height="20")
box3.place(x=675, y=100)

titulo_aux = Label(text = "...",font=("Cambria",15),fg="#1EEB74" , bg="#1E136E", width="25", height="1")
titulo_aux.place(x=680, y=100)

f2=Frame(myWindow,height=1,width=260,bg="#1EEB74")
f2.place(x=685, y=133)

myWindow.mainloop()