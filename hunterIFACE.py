from customtkinter import *
set_appearance_mode("dark")


pegar=0
class  hunter_studio:
    def __init__(self,*,nome,tamanho,):
       
        self.iniciar=CTk()
        self.titulo=self.iniciar.title(nome)
        self.tamanho=self.iniciar.geometry(tamanho)   
        self.entrada=CTkEntry(self.iniciar)  
    def botao(self,texto, cor ,comando,x,y):
        btn=CTkButton(self.iniciar,text=texto,command=comando,corner_radius=100,fg_color=cor)
        btn.place(x=x,y=y)
    def texto(self,texto,x,y):
        label=CTkLabel(self.iniciar,text=texto)
        label.place(x=x,y=y)
   # def barra_de_progresso(self,x,y,*valor,com,alt):
      #  pross=CTkProgressBar(self.iniciar,width=com,height=alt)
     #   pross.place(x=x,y=y)
      #  pross.set(valor)
    def caixa(*,self,comprimento,altura,cor,x,y):
        frame=CTkFrame(self.iniciar,width=comprimento,height=altura,fg_color=cor)
        frame.place(x=x,y=y)
    def botao_de_check(*,self,texto,x,y):
        check=CTkCheckBox(self.iniciar,text=texto)
        check.place(x=x,y=y)
    





             
            












