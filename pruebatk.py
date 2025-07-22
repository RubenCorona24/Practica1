import  tkinter as tk
from tkinter import BooleanVar, Button, Checkbutton, StringVar, Entry, Label, IntVar, Radiobutton, Toplevel, Menubutton
from tkinter.ttk import Checkbutton, Combobox


ventana = tk.Tk()
ventana.title("Prueba de tkinter 2")
#CHECKBUTTONS
variable_1chek = BooleanVar()
boton_booleano = Button(ventana,text='Botón',state='disabled')
#FUNCIÓN PARA HABILITAR BOTÓN
def habilitar():
    if variable_1chek.get():
        boton_booleano.config(state='normal')
    else:
        boton_booleano.config(state='disabled')
check1 = Checkbutton(ventana,text='Habilitar botón',variable=variable_1chek,command=habilitar)
boton_booleano.pack()
#CREAR UN LABEl
etiqueta1 = tk.Label(ventana,text='Hola, presiona b para cambiarme a rojo')
def on_key_press(event):
    if event.char == 'b':
        etiqueta1.config(text='Listo, me cambiaste de color',fg='red',font=('Arial',12,'bold'))
ventana.bind("<KeyPress>",on_key_press)

#MÁS PRÁCTICA CON LABEL

# Variables de control para los checkbuttons
mostrar_label1 = tk.BooleanVar()
mostrar_label2 = tk.BooleanVar()

# Etiquetas a mostrar/ocultar
label1 = tk.Label(ventana, text="Este es el texto 1", font=("Arial", 12), fg="green")
label2 = tk.Label(ventana, text="Este es el texto 2", font=("Arial", 12), fg="blue")
# Función para mostrar u ocultar
def actualizar_labels():
    if mostrar_label1.get():
        label1.pack()
    else:
        label1.pack_forget()

    if mostrar_label2.get():
        label2.pack()
    else:
        label2.pack_forget()

# Checkbuttons que controlan si se ven o no las etiquetas
#check1 = tk.Checkbutton(ventana, text="Mostrar texto 1", variable=mostrar_label1, command=actualizar_labels)
#check2 = tk.Checkbutton(ventana, text="Mostrar texto 2", variable=mostrar_label2, command=actualizar_labels)

#check1.pack(pady=5)
#check2.pack(pady=5)
#etiqueta1.pack()


#PRACTICAR CON VARIABLES DE CONTROL
texto = StringVar()
texto.set('texto añadido')

#EJEMPLO CON ETIQUETA
#entrada = Entry(ventana,textvariable=texto)
#entrada.pack()
#etiqueta = Label(ventana)
#etiqueta.pack()
#FUNCION DE ACTUALIZAR ETIQUETA
#def act_etiqueta(*args):
 #   etiqueta.config(text=texto.get())
#texto.trace('w',act_etiqueta)

#LAS Intvar()
#entero = IntVar(value=42)
#opcin1 = Radiobutton(ventana,text='Opción1',variable=entero,value=1)
#opcin1.pack()
#opcin2 = Radiobutton(ventana,text='Opción2',variable=entero,value=2)
#opcin2.pack()
#def actualizar(*args):
 #   print(entero.get())
#ntero.trace('w',actualizar)
#USAR DOUBLEVAR
#BOOLEANVAR
booleano = BooleanVar(value=True)
casilla = tk.Checkbutton(ventana,text='Aceptar',variable=booleano)
casilla.pack()
def actualizar(*args):
    print(f"Opción elegida: {booleano.get()}")
booleano.trace('w',actualizar)

labelmio = Label(ventana,text='PRIMERA OPCIÓN, SOY VERDE',fg='green')
labelmio.pack()

entero2 = IntVar(value=30)
radio = Radiobutton(ventana,text='Primera opción',variable=entero2,value=1)
radio2 = Radiobutton(ventana,text='Srgunda opción',variable=entero2,value=2)
radio.pack()
radio2.pack()
boton_comando = Button(ventana,text='OPCIÓN 1 PARA HABILITAR',state='disabled')
boton_comando.pack()
def mostrar(*args):
    if entero2.get() == 2:
        labelmio.config(text='SEGUNDA OPCIÓN, SOY ROJO',fg='red')
        boton_comando.config(text='OPCIÓN 1 PARA HABILITAR',state='disabled')
    elif entero2.get() == 1:
        labelmio.config(text='PRIMERA OPCIÓN. SOY VERDE', fg='green')
        boton_comando.config(state='normal',text='BOTÓN HABILITADO')

entero2.trace('w',mostrar)

#TRABAJAR CON TOP LEVEL
#def abrir_top_level():
  #  ventana_top_level = Toplevel(ventana)
 #   ventana_top_level.title("Ventana TopLevel")
  #  ventana_top_level.geometry('300x200+50+50')
#    labe_level = Label(ventana_top_level,text='Soy un label del Top Level')
#    labe_level.pack()
#    otro_boton = Button(ventana_top_level,text='SOY UN BOTON',state='disabled')
#    otro_boton.pack()
#    entrada = Entry(ventana_top_level)
#    entrada.insert(0,'NOMBRE')
#    label_ab = Label(ventana_top_level)
#    label_ab.pack()
 #   def actualizar(*args):
 #       label_ab.config(text=entrada.get())
 #   boton_actualizador = Button(ventana_top_level,text='MOSTRAR TEXTO EN LABEL',command=actualizar)
 #   boton_actualizador.pack()

#    entrada.pack()


 #   boton_cerrar = Button(ventana_top_level,text='CERRAR',fg='red',command=ventana_top_level.destroy)
 #   boton_cerrar.pack()
#oton_abrir = Button(ventana,text='ABRIR TOPLEVEL',command=abrir_top_level)

#TRABJAR MENUBUTTON
#menubutton = Menubutton(ventana,text='ARCHIVO')
#menubutton.pack()
#menu = tk.Menu(menubutton)
#menubutton.config(menu=menu)
#BARRAS DE MENÚ
#barra_menu = tk.Menu(ventana)
#ventana.config(menu=barra_menu)
#archivo_menu = tk.Menu(barra_menu)
#barra_menu.add_cascade(label='Archivo',menu=archivo_menu)
#archivo_menu.add_command(label='Nuevo')
#archivo_menu.add_command(label='Abrir')
#archivo_menu.add_separator()
#archivo_menu.add_command(label='Salir')
##AÑADIR UN MENU "Editar" A LA BARRA DE MENÚ
#editar_menu = tk.Menu(barra_menu)
#barra_menu.add_cascade(label='Editar',menu=editar_menu)
#editar_menu.add_command(label='Deshacer')
#editar_menu.add_command(label='Rehacer')
#MENU CPNTEXTUAL
#def mostrar_menu_contextual(event):
 #   menu_contextual.tk_popup(event.x_root,event.y_root)


#menu_contextual = tk.Menu(ventana,tearoff=0)
#menu_contextual.add_command(label='Cortar')
#menu_contextual.add_command(label='Copiar')
#menu_contextual.add_command(label='Pegar')
#menu_contextual.add_command(label='Abrir en terminal')
#mi_entrada = Entry(ventana)
#mi_entrada.pack()

#mi_entrada.bind("<Button-3>",mostrar_menu_contextual)
#boton_abrir.pack()
#TRABAJAR CON WIDGETS: TEXT
#from tkinter.scrolledtext import   ScrolledText
#texto = tk.Text(ventana,width=40,height=10,wrap='word',bg='green',fg='black',padx=10,pady=10,font=("Helvetica",12))
#texto.insert('1.0','Bienvenido a nuestro editor de texto')
#texto.pack()
#texto_desplazable = ScrolledText(ventana)
#texto_desplazable.pack()
#CON FUNCIONES
#def copiar():
#    texto.event_generate("<<Copy>>")
#def cortar():
 #   texto.event_generate("<<Cut>>")
#ef pegar():
  #  texto.event_generate("<<Paste>")
#boton_copiar = tk.Button(ventana,text='Copiar',command=copiar)
#boton_copiar.pack()
#boton_cortar = tk.Button(ventana,text='cortar',command=cortar)
#boton_cortar.pack()
#boton_pegar = tk.Button(ventana,text='pegar',command=pegar)
#boton_pegar.pack()
#WIDGETS DE LISTA(LISTBOX Y BOMBOBOX)
istbox = tk.Listbox(ventana,width=30,height=10,font=('Arial',12,'bold'))
istbox.insert(tk.END,'Primer elemento')
istbox.insert(1,'Segundo elemento')
istbox.insert(tk.END,'Tercer elemento')
istbox.insert(tk.END,'Cuarto elemento')
istbox.insert(0,'Cero elemento')
istbox.pack()
istbox.delete(0)
#ASOCIAR ELEMENTOS
def on_seleccionar(event):
    indice =  istbox.curselection()
    elemento = istbox.get(indice)
    print(f"Seleccionado: {elemento}")
istbox.bind("<<ListboxSelect>>",on_seleccionar)
combobox = Combobox(ventana,width=30,font=('Arial',12,'bold'),foreground='blue',background='white')
combobox.pack()
elementos = ['elemento 1','elemento 2','elemento 3']
combobox['values'] = elementos

def on_seleccionar(event):
    elemnt = combobox.get()
    print(f"Se ha seleccionado: {elemnt}")
from PIL import  Image, ImageTk

combobox.bind("<<ComboboxSelected>>",on_seleccionar)
#GESTIÓN DE IMÁGENES
imagen = tk.PhotoImage(file='images.png')
etiqueta = Label(ventana,image=imagen)
etiqueta.pack()
#OTRO MÉTODO
imagen_pil = Image.open('images.png')
imagen_redimensionada = imagen_pil.resize((100,100))
imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
boton = Button(ventana,image=imagen_tk)
boton.pack()
