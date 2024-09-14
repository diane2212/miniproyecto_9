import random
import tkinter
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import simpledialog, messagebox

#crear una ventana y configurarla
ventana = tkinter.Tk ()
ventana.title("Menu")
ventana.geometry("400x550")
ventana.resizable(0,0)
ventana.config(bg= "black")

#insertar una imagen en la ventana
logo_image = Image.open("Imagenes/Menu.png")
logo_image = logo_image.resize((400,550))
logo_image= ImageTk.PhotoImage(logo_image)
logo_Label= tkinter.Label(ventana, image=logo_image)
logo_Label.pack()


#imagen del boton 
Imagen_pil = Image.open("Imagenes/pedido.png")
Imagen_resize = Imagen_pil.resize((30,30))
Image_tk = ImageTk.PhotoImage(Imagen_resize)


#funciones de la ventana_pedidos
def actualizar_total(checkbuttons, total_label):
    precio_total = sum(precio for checkbutton, var, precio, Pedidos in checkbuttons if var.get())
    total_label.config(text=f"Total: ${precio_total:.2f}")
    total_label.place(x= 3, y= 500)

def mostrar_pedido(checkbuttons, pedido_label):
    Pedidos_seleccionados = [Pedidos for checkbutton, var, precio, Pedidos in checkbuttons if var.get()]
    if Pedidos_seleccionados:
        pedido = "🛒 Tu pedido:\n" + "\n".join(Pedidos_seleccionados)
    else:
        pedido = "Seleccione un producto."
    pedido_label.config(text=pedido, font= ("Tahoma",8))  
    pedido_label.place(x= 180, y=500)

def crear_ventana_pedidos():
    ventana_pedidos = tkinter.Toplevel(background="#8B0A1A")
    ventana_pedidos.title("Menu Fo9d")
    ventana_pedidos.geometry("300x650")
    ventana_pedidos.resizable(0,0)
    

    # Lista con precios categorizadas
    Pedidos = {
        "Bebidas": [
            ("Agua Sin gas/con gas", 150.50),
            ("Coca-Cola", 230.00),
            ("Pepsi", 210.00),
            ("Mirinda", 190.00),
        ],
        "Comidas": [
            ("Hamburguesa comun", 3500.00),
            ("Hamburguesa especial", 4500.00),
            ("Pizza Especial", 5000.00),
            ("Pizza Margarita", 5200.00),
            ("Pizza Tropical", 8700.00),
        ],
        "Cafeteria": [
            ("Cafe con leche", 3500.00),
            ("Capuchino", 3000.00),
            ("Medialunas", 2000.00),
            ("Tostado de JyQ", 4500.00),
        ],
    }
    
    frame = ttk.Frame(ventana_pedidos)
    frame.pack(padx=10, pady=10, fill=tkinter.BOTH)
    
    checkbuttons = []

    for categoria, lista_pedidos in Pedidos.items():
        # Título de la categoría
        titulo = ttk.Label(frame, text=categoria, font=("Helvetica", 12,))
        titulo.pack(pady=(10, 5), anchor='w')
        
        # Línea separadora
        separador = ttk.Separator(frame, orient='horizontal')
        separador.pack(fill='x', pady=3)
        
        for Pedidos, precio in lista_pedidos:
            row = ttk.Frame(frame)
            row.pack(fill=tkinter.X, pady=3)
            #Posicion de las comidas en lista (lado izquierdo)
            label = ttk.Label(row, text=f"{Pedidos} - ${precio:.2f}")
            label.pack(side=tkinter.LEFT, padx=5)
            #posicion de los botones check (lado derecho)
            var = tkinter.BooleanVar()
            checkbutton = ttk.Checkbutton(row, variable=var, command=lambda: actualizar_total(checkbuttons, total_label))
            checkbutton.pack(side=tkinter.RIGHT)
            
            checkbuttons.append((checkbutton, var, precio, Pedidos))
            
    #posicion del texto (total) bajo la lista
    total_label = ttk.Label(ventana_pedidos, text="Total: $0.00", font= "Pacifico", background= "gray")
    total_label.place(x= 3, y= 500)

    #configuracion del texto (tu pedido)
    pedido_label = ttk.Label(ventana_pedidos, text="", background= "gray")

    frame_botones= ttk.Frame(ventana_pedidos)
    frame_botones.pack(side=tkinter.LEFT)

    #BOTON ver tu orden
    boton_pedir = ttk.Button(frame_botones, text="Ver tu Orden", width=20, command=lambda: mostrar_pedido(checkbuttons, pedido_label))
    boton_pedir.pack()
    
    
    #BOTON confirmar pedido
    btn_conf_pedido = ttk.Button(frame_botones, text="Confirmar Pedido", width=20, command=lambda:confirmar_pedido(ventana_pedidos))
    btn_conf_pedido.pack()
    

    #funcion para  confirmar pedido
    def confirmar_pedido(ventana_pedidos):
      ventana_confirmar_pedido = tkinter.Toplevel()
      ventana_confirmar_pedido.title("Confirma tu pedido")
      ventana_confirmar_pedido.geometry("300x400")
      ventana_confirmar_pedido.config(bg= "white")



    #crear un titulo/etiqueta entrada de texto1
      Label = tkinter.Label(ventana_confirmar_pedido, text = "Nombre y Apellido", font = ("Tahoma", 10), foreground= "gray" )
      Label.place(x= 20, y= 10)
    #crear una entrada de texto
      entrada_text = tkinter.Text(ventana_confirmar_pedido, height= 1, width= 15, font=("Tahoma", 10), highlightbackground= "black", highlightthickness= 1)
      entrada_text.place(x=20, y= 40)

    #crear un titulo/etiqueta para entrada de texto2
      Label = tkinter.Label(ventana_confirmar_pedido, text = "¿Cómo te gustaría realizar la entrega? \n ♦️Delivery \n ♦️Retiro por el local", font = ("Tahoma", 10), foreground= "gray")
      Label.place(x= 20, y= 80)
    #crear una entrada de texto
      entrada_text = tkinter.Text(ventana_confirmar_pedido, height= 1, width= 15, font=("Tahoma", 10), highlightbackground= "black", highlightthickness= 1)
      entrada_text.place(x=20, y=150)
      #crear un titulo/etiqueta para entrada de texto3
      Label = tkinter.Label(ventana_confirmar_pedido, text = "Escribe tu número de telefono para finalizar📲", font = ("Tahoma", 10), foreground= "gray")
      Label.place(x=20, y=190)
    #crear una entrada de texto
      entrada_text = tkinter.Text(ventana_confirmar_pedido, height= 1, width= 30, font=("Tahoma", 10), highlightbackground= "black", highlightthickness= 1)
      entrada_text.place(x= 20, y=220)
      Label= tkinter.Label(ventana_confirmar_pedido, text= "📞 Nos comunicaremos contigo brevemente...\n Gracias por confiar en nosotros", font = ("Tahoma", 10), foreground= "gray")
      Label.place(x=20, y= 300)
        #funsion para cerrar app
      def cerrar_ventanas(ventana):
          ventana.destroy()

      #BOTON para finalizar pedido
      boton_enviar= tkinter.Button(ventana_confirmar_pedido, text="Enviar y Salir", width= 20, height= 1, bg= "light green", command=lambda: cerrar_ventanas(ventana))
      boton_enviar.place(x= 50, y=370)
    
        
#BOTON para ordenar
boton_pedidos = tkinter.Button(ventana, text = "Inicia tu orden aqui!", font= ("Calibri", 10), width= 200, height= 30, background= "#8B0A0A", highlightthickness= 2, borderwidth= 2, relief= "solid", command=crear_ventana_pedidos)
boton_pedidos.config(image= Image_tk, compound="left")
boton_bebidas_image= Image_tk
#Posicion del boton en ventana
boton_pedidos.pack(pady= 30 , padx = 0, side= tkinter.TOP , anchor = "s")
boton_pedidos.place(x=100, y=350)




ventana.mainloop()

