from  customtkinter  import  *
from HunterStudio import enviar_dados,desligar

def en():
    chave="ativar"
    enviar_dados(chave)
set_appearance_mode("dark") 
tela=CTk()
tela.title("cender led")
tela.geometry("500x500")

btn=CTkButton(tela,text="ligar",command=enviar_dados)
btn.place(x=20,y=300)
btn1=CTkButton(tela,text="desligar",command=desligar)
btn1.place(x=50,y=400)
tela.mainloop()