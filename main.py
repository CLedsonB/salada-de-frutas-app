from tkinter import *
from tkinter import ttk
import string as st
import random
import time
#from PIL import ImageTk, Image

# ________Constantes_____________________

corFundo = '#333333'
corFonte = '#3b3b3b'
corBorda = '#00aa00'
corTitulo = '#48b3e0'

temas = ["Nome","Cor","Comida",
                "Objeto","Idioma","Esporte",
                "Local","Filme","Animal",
                "Anatomia"]

alturaJanela = 1000
larguraJanela = 750
larguraBotao = 9
alturaBotao = 2

#__________Class__________________

class Input(Entry):
    def __init__(self, master=None, placeholder="", **kwargs):
        super().__init__(master, **kwargs)
        self.placeholder = placeholder
        self.tem_placeholder = True
        self.insert(0, self.placeholder)
        self.config(fg='grey')
        self.bind("<FocusIn>", self.remover_placeholder)
        self.bind("<FocusOut>", self.adicionar_placeholder)

    def remover_placeholder(self, event):
        if self.tem_placeholder:
            self.delete(0, END)
            self.config(fg='black')
            self.tem_placeholder = False

    def adicionar_placeholder(self, event):
        if not self.get():
            self.insert(0, self.placeholder)
            self.config(fg='grey')
            self.tem_placeholder = True

#________Funcoes aux_____________

idCont = None
andamentoCont = False

def sortear(letra):
        letraSort = random.choice(st.ascii_uppercase)
        letra.config(text=letraSort)
 
def contaTempo(cont, min,seg):
    global idCont
    global andamentoCont
    
    if min == 0 and seg == 0:
        andamentoCont = False
        return
    cont.config(text=f"{min:02d}:{seg:02d}")
    if seg > 0:
        idCont = cont.after(1000, contaTempo, cont, min, seg-1)
    else:
        idCont = cont.after(1000, contaTempo, cont, min-1, 59)
        
def iniciarContagem(cont,min,seg):
    global idCont
    global andamentoCont
    if andamentoCont:
        pararContagem();
    andamentoCont = True    
    cont.config(text=f"{min:02d}:{seg:02d}")
    contaTempo(cont,min,seg)

def pararContagem(cont):
    global idCont
    global andamentoCont
    if idCont is not None:
        cont.after_cancel(idCont)
        idCont = None
        andamentoCont = False
        
def gerenciaTempo(contador):
     pararContagem(contador)
     iniciarContagem(contador,5,0)
     
# ________Janela game_______________


def jan_game():
    jGame = Toplevel(main)
    jGame.title("Stop Game")
    jGame.geometry("700x1000")
    janGame= Frame(jGame, width=750, height=1000, bg=corBorda, pady=0, padx=0, relief='flat')
    janGame.place(x=0, y=0)
    
# DISTRIBUICAO DE ENTRADAS

    for i in range(5):
       ent = Input(jGame,width=13,placeholder=temas[i])
       ent.place(x=10,y=130+70*i)

    for j in range(5):
       ent = Input(jGame,width=13,placeholder=temas[j+5])
       ent.place(x=360,y=130+70*j)
                

# DISTRIBUICAO DE BOTOES +5

    for i in range(5):
        bp = Button(jGame, text="+5", width=1, height=1, font=("Ivy 4"), bg=corFundo, fg=corTitulo)
        bp.place(x=250,y=130+70*i)
        
    for j in range(5):
        bp = Button(jGame, text="+5", width=1, height=1, font=("Ivy 4"), bg=corFundo, fg=corTitulo)
        bp.place(x=600,y=130+70*j)
        
# DEMAIS ELEMENTOS

    b1 = Button(jGame, text="Sortear",width=5, height=1,command=lambda:[sortear(letra),gerenciaTempo(contador)], relief='flat', anchor='nw', overrelief='solid', font=('Ivy 6'), bg=corTitulo, fg=corFundo)
    letra = Label(jGame, text="?", height=1, padx=1,pady=1, relief='flat', anchor='center', font=('Ivy 14'), bg=corFundo, fg=corTitulo)
    b2 = Button(jGame, text="Stop",width=5, height=1, relief='flat', anchor='nw', overrelief='solid', font=('Ivy 6'), bg=corTitulo, fg=corFundo)
    contador = Label(jGame, text="00 : 00", height=1, padx=1,pady=1, relief='flat', anchor='center', font=('Ivy 10'), bg=corFundo, fg=corTitulo)
    pontuacao = Label(jGame, text="Total : 0", height=1, padx=1,pady=1, relief='flat', anchor='center', font=('Ivy 13'), bg=corFundo, fg=corTitulo)

    b1.place(x=10,y=10)
    letra.place(x=250, y=10)
    b2.place(x=340,y=10)
    contador.place(x=550, y=10)
    pontuacao.place(x=250,y=500)

# ______Janela personalizar_____________

def jan_person():
    jPerson = Toplevel(main)
    jPerson.title("Personalizar Jogo")
    jPerson.geometry("700x1000")
    janPerson= Frame(jPerson, width=750, height=1000, bg=corBorda, pady=0, padx=0, relief='flat')
    janPerson.place(x=0, y=0)
    
# DISTRIBUICAO DE ENTRADAS

    for i in range(10):
       ent = Input(jPerson,width=13,placeholder=temas[i])
       ent.place(x=200,y=130+70*i)
       
# DEMAIS ELEMENTOS

    titulo = Label(jPerson, text="Altere os temas da partida!!", height=1, padx=1,pady=1, relief='flat', anchor='center', font=('Ivy 13'), bg=corFundo, fg=corTitulo)
    bc = Button(jPerson, text="V", width=1, height=1, font=("Ivy 4"), bg=corFundo, fg=corTitulo)
    be = Button(jPerson, text="X", width=1, height=1, font=("Ivy 4"), bg=corFundo, fg=corTitulo) 
    
    titulo.place(x=60,y=20)
    bc.place(x=60,y=930)
    be.place(x=550,y=930)

# ________Janela Principal____________

main = Tk()
main.title("Stoppy")
main.configure(bg=corFundo)

janMain = Frame(main, width=750, height=1000, bg=corBorda, pady=0, padx=0, relief='flat')
janMain.place(x=0, y=0)


# ______Estilo para janela______________

estilo = ttk.Style(main)
estilo.theme_use("clam")

# ____Elementos Janela Principal________

l_titulo = Label(janMain, text="Salada De Frutas", height=2, padx=200,pady=1, relief='flat', anchor='center', font=('Ivy 10  bold'), bg=corFundo, fg=corTitulo)

l_titulo.place(x=1, y=1)

b1 = Button(janMain, text="Iniciar",width=larguraBotao, height=alturaBotao, command=jan_game, relief='flat', anchor='nw', overrelief='solid', font=('Ivy 8  bold'), bg=corTitulo, fg=corFundo)

b1.place(x=250,y=150)

b2 = Button(janMain, text="Config",width=larguraBotao-1, height=alturaBotao-1, relief='flat', anchor='nw', overrelief='solid', font=('Ivy 8  bold'), bg=corTitulo, fg=corFundo)

b2.place(x=250,y=300)

b3 = Button(janMain, text="Personalizar",width=larguraBotao, height=alturaBotao, command=jan_person, relief='flat', anchor='nw', overrelief='solid', font=('Ivy 8  bold'), bg=corTitulo, fg=corFundo)

b3.place(x=250,y=400)

main.mainloop()
