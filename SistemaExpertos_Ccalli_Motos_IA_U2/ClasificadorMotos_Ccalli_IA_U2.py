from ctypes import sizeof
from lib2to3.pgen2.token import LEFTSHIFT
from logging import RootLogger
from operator import length_hint
from select import select
from tkinter import *
from tkinter import filedialog as fd
import shutil
import copy
import os
import tkinter
from turtle import width  
from PIL import ImageTk,Image
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import threading
import os
import random
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#Frame utilizado para mostrar los graficos
class graph_frame(Frame):
    def __init__(self):
        Frame.__init__(self,root)
       
    
    def add_graph(self,fig):
        self.mpl_canvas=FigureCanvasTkAgg(fig,self)
        
        self.mpl_canvas.get_tk_widget().pack(fill=BOTH,expand=True)
        self.mpl_canvas._tkcanvas.pack( fill=BOTH, expand=True)
    def remove_graph(self):
        self.mpl_canvas.get_tk_widget().pack_forget()
        self.mpl_canvas._tkcanvas.pack_forget()
        del self.mpl_canvas

class bird:
    def __init__(self)->None:
        self.name=""
        self.size=""
        self.description=""
        self.habitat=""
        self.comments=""
        self.other_names=""
        self.distribution=""
        self.jalisco_distribution=""
        self.image="sources/default.jpeg"

        #Caracteristics
        self.caracteristics={}
        

class visualizer:
    def __init__(self,menu,frame1,bird,rules,clasifier)->None:
        self.frame1=frame1
        self.clasifier=clasifier
        self.name=Label(self.frame1,text="AVE",background='#353437')
        self.name.configure(font=("Arial",50))
        
        openImage=Image.open(bird.image)
        img=openImage.resize((200,300))
        self.photo=ImageTk.PhotoImage(img)
        self.image=Label(self.frame1,image=self.photo)

        self.size=Label(self.frame1,text="AVE",background='#353437')
        self.size.configure(font=("Arial",40))
        self.description=Label(self.frame1,text="AVE",background='#353437')
        self.description.configure(font=("Arial",40))
        self.habitat=Label(self.frame1,text="AVE",background='#353437')
        self.habitat.configure(font=("Arial",40))
        self.comments=Label(self.frame1,text="AVE",background='#353437')
        self.comments.configure(font=("Arial",40))
        self.explanation=Label(self.frame1,text="AVE",background='#353437')
        self.explanation.configure(font=("Arial",40))
        self.menu_window=menu
        self.bird=bird
        self.rules=rules
        self.addButton=Button(self.frame1,text="Agregar Moto",command=self.add_bird,bg="#7a7b7c", fg="white")
        self.addButton.config(height=2,width=15)
        self.menuButton=Button(self.frame1,text="Menu Principal",command=self.main_window,bg="#7a7b7c", fg="white")
        self.menuButton.config(height=2,width=15)
        self.showBird()


    def add_bird(self):
        self.addfunction=addBird(self.menu_window,self.frame1,self.clasifier)
        self.hide()
        self.addfunction.show()

    def show(self):
        self.name.pack()
        self.image.pack()
        self.size.pack()
        self.description.pack()
        self.habitat.pack()
        self.comments.pack()
        self.explanation.pack()

        if(self.bird.name=="Desconocida"):
            self.addButton.pack(side=TOP)
        self.menuButton.pack(side=TOP)
    
    #Oculta la vista de la descripción del ave
    def hide(self):
        self.name.pack_forget()
        self.image.pack_forget()
        self.size.pack_forget()
        self.description.pack_forget()
        self.habitat.pack_forget()
        self.comments.pack_forget()
        self.explanation.pack_forget()
        if(self.bird.name=="Desconocida"):
            self.addButton.pack_forget()
        self.menuButton.pack_forget()

    def showBird(self):
        self.name=Label(self.frame1,text=self.bird.name,background='#353437',fg="white")
        self.name.configure(font=("Arial",35))

        openImage=Image.open(self.bird.image)
        img=openImage.resize((200,200))
        self.photo=ImageTk.PhotoImage(img)       
        self.image=Label(self.frame1,image=self.photo)

        self.size=Label(self.frame1,text=self.bird.size,wraplength=1200,background='#353437',fg="white")
        self.size.configure(font=("Arial",14))
        self.description=Label(self.frame1,text=self.bird.description,wraplength=1200,background='#353437',fg="white")
        self.description.configure(font=("Arial",14))
        self.habitat=Label(self.frame1,text=self.bird.habitat,wraplength=1200,background='#353437',fg="white")
        self.habitat.configure(font=("Arial",14))
        self.comments=Label(self.frame1,text=self.bird.comments,wraplength=1200,background='#353437',fg="white")
        self.comments.configure(font=("Arial",14))
        exp="\n\n\nLa Moto fue encontrada en base a las siguientes características:\n"
        for key in self.rules.keys():
            exp+=key+":"+self.rules[key]+"\n"

        self.explanation=Label(self.frame1,text=exp,wraplength=1200,background='#353437',fg="white")
        self.explanation.configure(font=("Arial",14))

    

    #Muestra la vista principal
    def main_window(self):
        self.hide()
        self.menu_window.show()
    
    def closing(self):
        del self

class addBird:
    def __init__(self,menu,frame1,clasifier)->None:
        self.frame1=frame1
        self.main_menu=menu
        self.clasifier=clasifier
        self.load_caracteristics()
        # self.name=Label(self.frame1,text="AVE",background='#353437')
        # self.name.configure(font=("Arial",50))

        # openImage=Image.open(bird.image)
        # img=openImage.resize((200,300))
        # self.photo=ImageTk.PhotoImage(img)
        # self.image=Label(self.frame1,image=self.photo)
        self.labels = []
        self.entries = []

        for caracteristic in self.caracteristics:
            self.labels.append(Label(self.frame1,text=caracteristic.capitalize(),background='#353437',fg="white"))
            if(caracteristic=="descripcion" or caracteristic=="habitat" or caracteristic=="comentarios"):
                self.entries.append(Text(self.frame1, height=2, width=45))
            else:
                self.entries.append(Entry(self.frame1,width=60))

        




        # self.description=Label(self.frame1,text="AVE",background='#353437')
        # self.description.configure(font=("Arial",40))
        # self.habitat=Label(self.frame1,text="AVE",background='#353437')
        # self.habitat.configure(font=("Arial",40))
        # self.comments=Label(self.frame1,text="AVE",background='#353437')
        # self.comments.configure(font=("Arial",40))
        # self.explanation=Label(self.frame1,text="AVE",background='#353437')
        # self.explanation.configure(font=("Arial",40))
        # self.menu_window=menu
        # self.bird=bird
        # self.rules=rules
        # self.menuButton=Button(self.frame1,text="Menu Principal",command=self.main_window,bg="#7a7b7c", fg="white")
        # self.menuButton.config(height=2,width=15)
        # self.showBird()
    def load_caracteristics(self):
        self.caracteristics = []
        self.caracteristics.append("nombre")
        self.caracteristics.append("descripcion")
        self.caracteristics.append("comentarios")     
        self.caracteristics.append("Carenado")
    
    def show(self):
        self.title=Label(self.frame1,text="Agregar Moto",background='#353437',fg="white")
        self.title.configure(font=("Arial",20))
        self.title.grid(column=1,row=1,columnspan=5)
        self.currentpos=3
        for i in range(len(self.labels)):
            self.labels[i].configure(font=("Arial",15))
            self.labels[i].grid(column=1,row=self.currentpos)
            self.entries[i].grid(column=2, row=self.currentpos)
            if(self.caracteristics[i]=="comentarios"):
                self.currentpos+=1
                self.instructions=Label(self.frame1,text="Indique los colores de la Moto",background='#353437',fg="white")
                self.instructions.configure(font=("Arial",20))
                self.instructions.grid(column=1, row=self.currentpos,columnspan=2)
            self.currentpos+=1

        self.filename=StringVar()
        self.image=Label(self.frame1,text="Imagen",background='#353437',fg="white")
        self.image.configure(font=("Arial",15))
        self.image.grid(column=1,row=23)
        self.showRute=Entry(self.frame1,textvariable=self.filename)
        self.showRute.config(state='disabled',width=60)
        self.showRute.grid(column=2,row=23)
        self.chooseImage=Button(self.frame1,text="Seleccionar Imagen",command=self.selectImage,bg="#7a7b7c",fg="white")
        self.chooseImage.config(height=1,width=15)
        self.chooseImage.grid(column=3,row=23)
        self.saveButton=Button(self.frame1,text="Guardar",command=self.save,bg="#7a7b7c",fg="white")
        self.saveButton.config(height=2,width=15)
        self.saveButton.grid(column=2,row=27)
        self.menuButton=Button(self.frame1,text="Menu Principal",command=self.main_window,bg="#7a7b7c", fg="white")
        self.menuButton.config(height=2,width=15)
        self.menuButton.grid(column=1,row=27)

    def selectImage(self):
        self.filename.set(fd.askopenfilename(initialdir = "/",title = "Seleccionar imagen",filetypes = (("jpeg files","*.jpg"),("all files","*.*"))))
        

    def hide(self):
        self.title.grid_remove()
        for i in range(len(self.labels)):
            self.labels[i].grid_remove()
            self.entries[i].grid_remove()
        self.chooseImage.grid_remove()
        self.instructions.grid_remove()
        self.image.grid_remove()
        self.showRute.grid_remove()
        self.saveButton.grid_remove()
        self.menuButton.grid_remove()
        

    def save(self):
        self.aux = bird()
        for i in range(len(self.entries)):
            if(self.caracteristics[i]=="descripcion" or self.caracteristics[i]=="habitat" or self.caracteristics[i]=="comentarios"):
                if(self.caracteristics[i]=="descripcion"):
                    self.aux.description=self.entries[i].get(1.0,"end-1c")
                elif(self.caracteristics[i]=="habitat"):
                    self.aux.habitat=self.entries[i].get(1.0,"end-1c")
                elif(self.caracteristics[i]=="comentarios"):
                    self.aux.comments=self.entries[i].get(1.0,"end-1c")
            else:
                if(self.entries[i].get()!=""):
                    if(self.caracteristics[i]=="nombre"):
                        self.aux.name=self.entries[i].get()
                    else:
                        self.aux.caracteristics[self.caracteristics[i]]=self.entries[i].get()
        self.currentpath = os.getcwd()
        self.currentpath+="\\sources\\"
        shutil.copy(self.filename.get(),self.currentpath)
        self.words=self.filename.get().split("/")
        self.aux.image="sources/"+self.words[-1]
        self.clasifier.aves.append(self.aux)
        self.hide()
        self.main_menu.show()
    
    def main_window(self):
        self.hide()
        self.main_menu.show()


        
#En esta clase se tienen los metodos para clasificar
class clasifier:
    #Constructor de la clase
    def __init__(self,menu,frame1) -> None:
        self.menu_window=menu
        self.frame1=frame1
        self.title=Label(self.frame1,text="Clasificador de Motos",background='#353437',fg="white")
        self.title.configure(font=("Arial",35))

        self.menuButton=Button(self.frame1,text="Main Menu",command=self.main_window,bg="#7a7b7c",fg="white")
        self.menuButton.config(height=10,width=50)
        self.aves=[]
        self.default_ave=bird()
        self.load_birds()
        self.loadall()
        
    def loadall(self):
        
        self.good=False
        self.doing=True
        
        
        # self.load_birds()
        self.rules={}
        self.decition=self.aves[0]
        self.visual=visualizer(self.menu_window,self.frame1,self.decition,self.rules,self)
        self.possible_rules={}
        self.possible_aves=[]

        
        
    def load_birds(self):
        self.default_ave.name="Desconocida"
        self.default_ave.image="sources/default.jpeg"
        
        self.aux=bird()
        self.aux.name="Yamaha YZF-R1"
        self.aux.description="La Yamaha YZF-R1 es una motocicleta deportiva fabricada por Yamaha Motor Company."
        self.aux.habitat="Es conocida por su potente motor de cuatro cilindros en línea y su diseño aerodinámico."
        self.aux.comments="La R1 ha sido una de las motocicletas deportivas líderes en el mercado desde su introducción en 1998."
        self.aux.caracteristics["Carenado"]="Azul"
        self.aux.caracteristics["pico"]="negro"
        self.aux.caracteristics["loras"]="amarillo"
        self.aux.caracteristics["cuerpo"]="blanco"
        self.aux.caracteristics["tarsos"]="negro"
        self.aux.image="sources/garceta_pie_dorado.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="Honda CBR1000RR"
        self.aux.description="La Honda CBR1000RR, también conocida como Fireblade, es una motocicleta deportiva fabricada por Honda."
        self.aux.habitat="Ha sido aclamada por su equilibrio entre rendimiento en pista y facilidad de conducción en carreteras públicas."
        self.aux.comments="La CBR1000RR ha sido actualizada a lo largo de los años con mejoras en la potencia del motor, aerodinámica y tecnología electrónica."
        self.aux.caracteristics["Carenado"]="Rojo"
        self.aux.caracteristics["pico"]="negro con base amarillenta"
        self.aux.caracteristics["alas"]="verde oscuro"
        self.aux.caracteristics["cola"]="verde oscuro"
        self.aux.caracteristics["tarsos"]="amarillos"
        self.aux.image="sources/garceta_verde.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="Kawasaki ZX-10R"
        self.aux.description="La Kawasaki Ninja ZX-10R es una motocicleta deportiva fabricada por Kawasaki Heavy Industries."
        self.aux.habitat="Conocida por su potente motor de cuatro cilindros en línea y su agresivo diseño de carenado."
        self.aux.comments="La ZX-10R ha sido exitosa en competiciones de superbike y ha ganado múltiples campeonatos en todo el mundo."
        self.aux.caracteristics["Carenado"]="Verde"
        self.aux.caracteristics["pico"]="negro"
        self.aux.caracteristics["corona"]="negro"
        self.aux.caracteristics["garganta"]="blanquecino"
        self.aux.caracteristics["pecho"]="grisáceo"
        self.aux.caracteristics["vientre"]="grisáceo"
        self.aux.caracteristics["espalda"]="negro"
        self.aux.caracteristics["alas"]="gris"
        self.aux.caracteristics["cola"]="gris"
        self.aux.image="sources/pedrete_corona_negra.jpg"
        self.aves.append(self.aux)

        self.aux=bird()
        self.aux.name="BMW S1000RR"
        self.aux.description="La BMW S1000RR es una motocicleta deportiva fabricada por BMW Motorrad."
        self.aux.habitat="Es reconocida por su motor de cuatro cilindros en línea de alta potencia y su chasis ligero."
        self.aux.comments="La S1000RR ha sido diseñada tanto para el rendimiento en pista como para la comodidad en carreteras públicas, con características como modos de conducción ajustables y sistemas de asistencia electrónica."
        self.aux.caracteristics["Carenado"]="Gris"
        self.aux.caracteristics["pico"]="negro"
        self.aux.caracteristics["cabeza"]="grisácea"
        self.aux.caracteristics["cuerpo"]="negruzco"
        self.aux.caracteristics["cola"]="negro"
        self.aux.image="sources/zopilote_comun.jpg"
        self.aves.append(self.aux)

        #self.aves.append(self.aux)

    def question(self,q,opt):
        options=[]
        options.append("Otro")
        for key in opt.keys():
            options.append(key)
        self.selection=StringVar()
        self.chooses=StringVar()
        self.chooses.set("Otro")
        self.instructions=Label(self.frame1,text="Seleccione el color de la moto:\n\n",background='#353437',fg="white")
        self.instructions.configure(font=("Arial",25))
        self.instructions.pack()
        # self.image=ImageTk.PhotoImage(Image.open("bird_main_menu.png"))
        # self.panel=Label(self.frame1,image=self.image)
        # self.panel.pack(side="bottom",fill="both",expand="yes")
        self.caracteristica=Label(self.frame1,text=q,background='#353437',fg="white")
        self.caracteristica.configure(font=("Arial",25))
        self.caracteristica.pack()
        self.drop=OptionMenu(self.frame1,self.chooses,*options)
        self.drop.config(height=1,width=20)
        self.drop.pack()
        self.button=Button(self.frame1,text="Siguiente",command=self.clicked,bg="#7a7b7c",fg="white")
        self.button.config(height=2,width=10)
        self.button.pack()
        self.button.wait_variable(self.selection)
        self.cont = 0
        self.listo = False
        # self.panel.pack_forget()
        self.instructions.pack_forget()
        self.drop.pack_forget()
       # self.panel.pack_forget()
        self.button.pack_forget()
        self.caracteristica.pack_forget()
        return self.selection
        
    def clicked(self):
        print(self.chooses.get())
        self.selection.set(self.chooses.get())




    def clasify(self):
        #self.load_birds()
        self.loadall()
        self.possible_aves=copy.copy(self.aves)
        self.possible_rules={}
        self.rules={}
        other=True
        while(other):
            self.possible_rules={}
            for ave in self.possible_aves:
                for key in ave.caracteristics.keys():
                    if(key not in self.rules):
                        if(key not in self.possible_rules):
                            self.possible_rules[key]={}
                        if(ave.caracteristics[key] not in self.possible_rules[key]):
                            self.possible_rules[key][ave.caracteristics[key]]=1
                        else:
                            self.possible_rules[key][ave.caracteristics[key]]+=1
                        
            color=StringVar()
            caracteristic=""
            for key in self.possible_rules.keys():
                color.set(self.question(key,self.possible_rules[key]).get())
                caracteristic=key
                self.rules[key]=color.get()
                print(color.get())
                break
            index=0
            elements=len(self.possible_aves)
            while index < elements:
                print(self.possible_aves[index].name)
                if(caracteristic not in self.possible_aves[index].caracteristics):
                    self.possible_aves[index].caracteristics[caracteristic]="otro"
                if(self.possible_aves[index].caracteristics[caracteristic]!=color.get()):
                    del self.possible_aves[index]
                    elements-=1
                else:
                    index+=1
            
            
            if(len(self.possible_aves)<2):
                other=False
            
        
        if(len(self.possible_aves)==1):
            avetoshow=self.possible_aves[0]

            self.visual=visualizer(self.menu_window,self.frame1,avetoshow,self.rules,self)
        else:
            self.visual=visualizer(self.menu_window,self.frame1,self.default_ave,self.rules,self)
        
        self.visual.show()
    

    def show(self):
        self.title.pack()
        self.clasify()
        

    #Oculta la vista del apartado de clasificación
    def hide(self):
        self.title.pack_forget()
        self.menuButton.pack_forget()
        
  
    #Muestra la vista principal
    def main_window(self):
        self.hide()
        
        self.menu_window.show()

    def closing(self):
        self.visual.closing()
        del self

   

class main_menu:
    def __init__(self) -> None:
        
        
        openImage=Image.open("sources/bird.jpg")
        img=openImage.resize((1550,800))
        # self.image=ImageTk.PhotoImage(img)
                
        # self.panel=Label(root,image=self.image)
        self.frame1 = Frame(root,background='#353437')
        self.title=Label(self.frame1, text="Clasificador de Motos\n\n\n",font=("Arial",25),background='#353437',fg="white")
        self.clasifier_button=Button(self.frame1,text="Encontrar Moto",command=self.show_clasifier_window,bg="#7a7b7c",fg="white")
        self.clasifier_button.config(height=5,width=30)
        self.clasifier_window = clasifier(self,self.frame1)

    #Muestra la vista principal
    def show(self):
        
        # self.panel.place(x=0,y=0)
        self.frame1.pack(pady = 20 )
        self.title.pack()
        self.clasifier_button.pack()
    
    #Oculta la vista principal
    def hide(self):
        self.title.pack_forget()
        self.clasifier_button.pack_forget()

    #Muestra la vista del clasificador
    def show_clasifier_window(self):
        self.hide()
        
        #self.clasifier_window.load_birds()
        self.clasifier_window.clasify()

    #Funcion para terminar los procesos 
    def closing(self):
        self.clasifier_window.closing()
        del self


if __name__ == "__main__":
    try:
        root = Tk()
        def on_closing():
            program.closing()
            root.destroy()
            
        root.protocol("WM_DELETE_WINDOW", on_closing)
        root.title("Sistema experto")
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.geometry("%dx%d" % (w, h))
        root.configure(bg='#353437')
        program=main_menu()
        program.show()
        root.mainloop()
    except:
        quit()