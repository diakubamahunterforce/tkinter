#Hunter estudio  apresenta   um novo modelo #
#para customtkinter   

from hunterIFACE import *





def  serial():
   print(" ola mundo")
   programa.texto(texto="ola",x=150,y=40)
   
programa=hunter_studio(nome="ola",tamanho="300x300")
programa.botao(texto="escreva",cor="blue",comando=serial,x=95,y=0)

programa.iniciar.mainloop()
