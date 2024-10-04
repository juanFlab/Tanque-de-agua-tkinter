import tkinter as tk
from tkinter import ttk
import time
import random


class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.crear_botones()
        self.val = 450
        self.val2=1200
       
        
        self.canvas1=tk.Canvas(self.ventana1, width=900, height=1700, background="#334444")
        self.canvas1.grid(column=0, row=1) 
  
        self.ventana1.mainloop()
       
    def crear_botones(self):
        self.labelframe1=ttk.LabelFrame(self.ventana1,text="Control nivel de agua")
        self.labelframe1.grid(column=0, row=0 ,sticky="w", padx=10, pady=10)  
        self.boton2=ttk.Button(self.labelframe1, text="VaciarT1", command=self.vaciar)
        self.boton2.grid(column=2, row=0, padx=5)
        self.bt2up=ttk.Button(self.labelframe1,text="VaciarT2",command=self.vaciarT2)
        self.bt2up.grid(column=2,row=1,padx=10,pady=20)
        self.bt2=ttk.Button(self.labelframe1,text="LlenarT2",command=self.llenarT2)
        self.bt2.grid(column=1,row=1,padx=5,pady=20)
   
        self.bt1up=ttk.Button(self.labelframe1,text="LlenarT1",command=self.llenar)
        self.bt1up.grid(column=1,row=0,padx=20)
        self.btCerrar=ttk.Button(self.labelframe1,text="Cerrar",command=self.cerrar)
        self.btCerrar.grid(column=1,row=4,pady=30)
       
     
    def cerrar(self):
        quit()
        
        
  

    def vaciarT2(self):
       
        if True:
	        if self.val2<1100:
	        	self.canvas1.delete("nivel2")
	        	
	       
		        self.nivel=self.canvas1.create_text(150,1350,text=str(1270-self.val2)+" Litros",tag="nivel2",fill="white")
		        self.tanque2(40,700,500,"#888888")
		        self.val2 +=50
    	

    def vaciar(self):
       
        if True:
	        if self.val <450:
	        	self.canvas1.delete("nivel")
	       
		        self.nivel=self.canvas1.create_text(150,650,text=str(1270-self.val)+" Litros",tag="nivel",fill="white")
		        self.tanque(40,20,500,"#888888")
		        
		  
		        self.val+=50
		        if self.val>450:
		        	self.level= self.canvas1.create_text(210,700,text="NIVEL  MUY BAJO!!",tag="vacio",fill="red")
		        	


   
    	
    	
    	
    	
    
    	
    def tanque(self,x,y,litros,color):
    	
    	
    
    
    	ancho= litros /2
    	alto=litros
    	espesor=(x+ancho)*.030
    	self.canvas1.delete("aqua")
    	self.canvas1.delete("vacio")
    	
    	     	
    	 
    	self.exterior=self.canvas1.create_rectangle(x,y,x+ancho,y+alto,fill=color,width=4)
    	self.interior=self.canvas1.create_rectangle(x+espesor,y+espesor,ancho+x-espesor,alto-espesor*6,fill="#666666")
    	self.deIzq=self.canvas1.create_rectangle(x,alto,x+espesor*3,alto+alto/6,fill=color,width=4)
    	self.deDer=self.canvas1.create_rectangle(ancho-(espesor*3),alto,ancho,alto+alto/6,fill=color,width=4)
    	self.traIzq=self.canvas1.create_rectangle(ancho/2,alto,ancho/2+espesor*3,alto+alto/9,fill=color,width=4)
    	self.aqua=self.canvas1.create_rectangle(x+espesor,self.val,x+ancho-espesor,alto-espesor*6,fill="aqua",tag="aqua")
    	
    	
 
    	
    def tanque2(self,x,y,litros,color):
    	
    	
    
    
    	x2= x+litros /2
    	y2=y+litros
    	espesor=(x+x2)*.030
    	self.canvas1.delete("aqua2")
    	self.canvas1.delete("vacio2")
    	
    	     	
    	 
    	self.exterior=self.canvas1.create_rectangle(x,y,x2,y2,fill=color,width=4)
    	self.interior=self.canvas1.create_rectangle(x+espesor,y+espesor,x2-espesor,y2-espesor*6,fill="#666666")
    	self.deIzq=self.canvas1.create_rectangle(x,y2,x+espesor*3,y2+y2/14,fill=color,width=4)
    	self.deDer=self.canvas1.create_rectangle(x2-(espesor*3),y2,x2,y2+y2/14,fill=color,width=4)
    	self.traIzq=self.canvas1.create_rectangle(x2/2,y2,x2/2+espesor*3,y2+y2/16,fill=color,width=4)
    	self.aqua=self.canvas1.create_rectangle(x+espesor,self.val2,x2-espesor,y2-espesor*6,fill="aqua",tag="aqua2")	
    		
    def llenarT2(self):
    	if self.val2>780:
    						self.val2-=35
    						self.tanque2(40,700,500,"#888888")
    						self.canvas1.delete("nivel2")
    						self.nivel2=self.canvas1.create_text(150,1350,text=str(1370-self.val)+"Litros",tag="nivel2",fill="white")
    						
    	
    def llenar(self):
    	
   
    
    	if self.val >80:		
  
    		self.val -=35
	    
	    	self.tanque(40,20,500,"#888888")
	    
	    	self.canvas1.delete("nivel")
	    	self.nivel=self.canvas1.create_text(150,650,text=str(1270-self.val)+" Litros",tag="nivel",fill="white")
	 
	    	if self.val<120:
	    		self.peligro= self.canvas1.create_text(160,200,text=" PELIGRO\n POSIBLE \n DERRAME!",tag="peligro",fill="red")
	    		
	    	
	    		
    	
    
    	

app=Aplicacion()


