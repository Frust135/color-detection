from tkinter import *

from functions.camera_functions import initialize_camera, open_camera_with_mask
#-------------------------------------------------------------------
#      Creación ventana
#-------------------------------------------------------------------

myWindow = Tk()
myWindow.geometry("985x450")
myWindow.title("Detección de Cámara")
myWindow['bg'] = '#060836'

tabla_hash = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
hash_texto = ''

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


largo_camara_inferior = Label(text = "Largo: ", font=("Cambria",15),fg="#1EEB74" , bg="#1E136E")
largo_camara_inferior.place(x=50, y=200)
largo_camara_inferior_input = Entry(width = "6",bg="#B6ADE4")
largo_camara_inferior_input.place(x=100, y=200)


largo_camara_inferior = Label(text = "Archo: ", font=("Cambria",15),fg="#1EEB74" , bg="#1E136E")
largo_camara_inferior.place(x=190, y=200)
ancho_camara_inferior_input = Entry(width = "6",bg="#B6ADE4")
ancho_camara_inferior_input.place(x=240, y=200)

color_camara_inferior = Label(text = "Colores de la Cámara Inferior", font=("Cambria",15),fg="#1EEB74" , bg="#1E136E", width="25", height="1")
color_camara_inferior.place(x=50, y=270)

min_color_inferior = Label(text = " Min: ", font=("Cambria",15),fg="#1EEB74" , bg="#1E136E")
min_color_inferior.place(x=40, y=320)
min_color_inferior_input = Entry(width = "10",bg="#B6ADE4")
min_color_inferior_input.place(x=80, y=320)

largo_camara_inferior = Label(text = "Max: ", font=("Cambria",15),fg="#1EEB74" , bg="#1E136E")
largo_camara_inferior.place(x=185, y=320)
ancho_camara_inferior_input = Entry(width = "10",bg="#B6ADE4")
ancho_camara_inferior_input.place(x=220, y=320)

abrir_camara_inferior = Button(myWindow, text = "Abrir Camara", width="28", bg="#B6ADE4")
abrir_camara_inferior.place(x=40, y=380)

# abrir_camara_inferior = Button(myWindow, text = "Abrir Camara", width="34", bg="#B6ADE4", command=lambda: insertar_hash(ingreso_nombre_archivo.get(),[nombre_ruta.get(), ingreso_clave_publica.get(),usbReader()], tabla_hash))
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

largo_camara_superior = Label(text = "Largo: ", font=("Cambria",15),fg="#1EEB74" , bg="#1E136E")
largo_camara_superior.place(x=350, y=200)
largo_camara_superior_input = Entry(width = "6",bg="#B6ADE4")
largo_camara_superior_input.place(x=400, y=200)


largo_camara_superior = Label(text = "Archo: ", font=("Cambria",15),fg="#1EEB74" , bg="#1E136E")
largo_camara_superior.place(x=490, y=200)
ancho_camara_superior_input = Entry(width = "6",bg="#B6ADE4")
ancho_camara_superior_input.place(x=540, y=200)

color_camara_superior = Label(text = "Colores de la Cámara Superior", font=("Cambria",15),fg="#1EEB74" , bg="#1E136E", width="25", height="1")
color_camara_superior.place(x=350, y=270)

min_color_superior = Label(text = " Min: ", font=("Cambria",15),fg="#1EEB74" , bg="#1E136E")
min_color_superior.place(x=340, y=320)
min_color_superior_input = Entry(width = "10",bg="#B6ADE4")
min_color_superior_input.place(x=380, y=320)

largo_camara_superior = Label(text = "Max: ", font=("Cambria",15),fg="#1EEB74" , bg="#1E136E")
largo_camara_superior.place(x=485, y=320)
ancho_camara_superior_input = Entry(width = "10",bg="#B6ADE4")
ancho_camara_superior_input.place(x=520, y=320)

abrir_camara_superior = Button(myWindow, text = "Abrir Camara", width="28", bg="#B6ADE4")
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
# cap = initialize_camera(640, 480)
# open_camera_with_mask(cap, [50,50,100], [80,80,255])