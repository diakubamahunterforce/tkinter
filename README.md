# Esta biblioteca é uma versão do customtkinter em portugues simples de se usar
# primeiro instala customtkinter,no terminal  ou cmd   digita o  seguinte comando
# pip install customtkinter       para   windows
# sudo pip3 install customtkinter linux [ ubuntu  debian etc]
# pip3 install custontkinter   mac os

# depois de ter instalado, clona o repositorio com git clone ou baixa o arquivo hunterIFACE.py.
# Com  sua ide como, pycharm  vs code jupyter ou outro.
# Abra o arquivo  hunterIFACE.py, no vs code ou pycharm 
# depois cria um novo arquivo. 
# neste novo arquivo  podes importar o modulo

from hunterIFACE.py import *

# iniciar  o modulo cria uma varial exemplo programa

programa=hunter_studio(nome=" test" ,tamanho="300x30")
# nome sera o  titulo do programa tamanho  tem haver com grandeza da tela podes por seu gosto mais coloca sempre virugulas altas-- "500x300~" 
programa.texto(texto="ola mundo",x=150,y=0)
# o parametro "texto" ele te permite emprir um texto na tela  texto="ola mundo"  x e y te ajuda  cordernar o posiçao do texto  x 
programa.iniciar.mainloop()
no final  do programa  colocar parametro iniciar . mainloop() para programa funciona  

# Lista de comando

# programa=hunter_studio(nome=" test" ,tamanho="300x30")
# programa.botao(texto="ok", cor="blue", comando=sd, x=150,y=1)
# comando tem haver com função  que ela vai chamar 
# programa.texto(texto="ola mundo",x=12,y=0)
# programa.botao_de_check(texto="confirma",x=0,y=1);
# programpa.caixa(comprimento=29,altura=20,cor=blue,x=20,y=10)
# programa.entrada().get()
# programa.entrada.place(x=12,y=39)
# podes criar uma função  para utilizar o  get a entrada
# exemplo

from hunterIFACE import *

def  serial():
   print(" ola mundo")
   programa.texto(texto="ola",x=150,y=40)
   
programa=hunter_studio(nome="ola",tamanho="300x300")
programa.botao(texto="escreva",cor="blue",comando=serial,x=95,y=0)

programa.iniciar.mainloop()












