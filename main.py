from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

# ________Constantes_____________________

corFundo = '#333333'
corFonte = '#3b3b3b'
corBorda = '#00aa00'
corTitulo = '#48b3e0'

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

# ________Janela aux_______________


def jan_game():
    jGame = Toplevel(main)
    jGame.title("Stop Game")
    jGame.geometry("700x1000")
    janGame= Frame(jGame, width=750, height=1000, bg=corBorda, pady=0, padx=0, relief='flat')
    janGame.place(x=0, y=0)
    
    b1 = Button(jGame, text="Sortear",width=5, height=1, relief='flat', anchor='nw', overrelief='solid', font=('Ivy 6'), bg=corTitulo, fg=corFundo)
    letra = Label(jGame, text="Z", height=1, padx=1,pady=1, relief='flat', anchor='center', font=('Ivy 14'), bg=corFundo, fg=corTitulo)
    b2 = Button(jGame, text="Stop",width=5, height=1, relief='flat', anchor='nw', overrelief='solid', font=('Ivy 6'), bg=corTitulo, fg=corFundo)
    time = Label(jGame, text="00 : 00", height=1, padx=1,pady=1, relief='flat', anchor='center', font=('Ivy 10'), bg=corFundo, fg=corTitulo)
        
    bp1 = Button(jGame, text="+5", width=1, height=1, font=("Ivy 4"), bg=corFundo, fg=corTitulo)
    bp2 = Button(jGame, text="+5", width=1, height=1, font=("Ivy 4"), bg=corFundo, fg=corTitulo)
    bp3 = Button(jGame, text="+5", width=1, height=1, font=("Ivy 4"), bg=corFundo, fg=corTitulo)
    bp4 = Button(jGame, text="+5", width=1, height=1, font=("Ivy 4"), bg=corFundo, fg=corTitulo)
    bp5 = Button(jGame, text="+5", width=1, height=1, font=("Ivy 4"), bg=corFundo, fg=corTitulo)
    bp6 = Button(jGame, text="+5", width=1, height=1, font=("Ivy 4"), bg=corFundo, fg=corTitulo)
    bp7 = Button(jGame, text="+5", width=1, height=1, font=("Ivy 4"), bg=corFundo, fg=corTitulo)
    bp8 = Button(jGame, text="+5", width=1, height=1, font=("Ivy 4"), bg=corFundo, fg=corTitulo)
    bp9 = Button(jGame, text="+5", width=1, height=1, font=("Ivy 4"), bg=corFundo, fg=corTitulo)
    bp0 = Button(jGame, text="+5", width=1, height=1, font=("Ivy 4"), bg=corFundo, fg=corTitulo)

    ent1 = Input(jGame,width=13,placeholder="Nome")
    ent2 = Input(jGame,width=13,placeholder="Cor")
    ent3 = Input(jGame,width=13,placeholder="Comida")
    ent4 = Input(jGame,width=13,placeholder="Objeto")
    ent5 = Input(jGame,width=13,placeholder="Idioma")
    ent6 = Input(jGame,width=13,placeholder="Esporte")
    ent7 = Input(jGame,width=13,placeholder="Local")
    ent8 = Input(jGame,width=13,placeholder="Filme")
    ent9 = Input(jGame,width=13,placeholder="Animal")
    ent0 = Input(jGame,width=13,placeholder="Anatomia")
    
    pontuacao = Label(jGame, text="Total : 0", height=1, padx=1,pady=1, relief='flat', anchor='center', font=('Ivy 13'), bg=corFundo, fg=corTitulo)
    
    b1.place(x=10,y=10)
    letra.place(x=250, y=10)
    b2.place(x=340,y=10)
    time.place(x=550, y=10)
    
    bp1.place(x=250,y=130)
    bp2.place(x=600,y=130)
    bp3.place(x=250,y=200)
    bp4.place(x=600,y=200)
    bp5.place(x=250,y=270)
    bp6.place(x=600,y=270)
    bp7.place(x=250,y=340)
    bp8.place(x=600,y=340)
    bp9.place(x=250,y=410)
    bp0.place(x=600,y=410)
    
    ent1.place(x=10,y=130)
    ent2.place(x=360,y=130)
    ent3.place(x=10,y=200)
    ent4.place(x=360,y=200)
    ent5.place(x=10,y=270)
    ent6.place(x=360,y=270)
    ent7.place(x=10,y=340)
    ent8.place(x=360,y=340)
    ent9.place(x=10,y=410)
    ent0.place(x=360,y=410)
    
    pontuacao.place(x=250,y=500)

def jan_person():
    jPerson = Toplevel(main)
    jPerson.title("Personalizar Jogo")
    jPerson.geometry("700x1000")
    janPerson= Frame(jPerson, width=750, height=1000, bg=corBorda, pady=0, padx=0, relief='flat')
    janPerson.place(x=0, y=0)
    
main = Tk()
main.title("Stoppy")
main.configure(bg=corFundo)

# ________Janela Principal____________

janMain = Frame(main, width=750, height=1000, bg=corBorda, pady=0, padx=0, relief='flat')
janMain.place(x=0, y=0)


# ________Estilo para janela________________

estilo = ttk.Style(main)
estilo.theme_use("clam")

# ______Elementos Janela Principal__________

l_titulo = Label(janMain, text="Salada De Frutas", height=2, padx=200,pady=1, relief='flat', anchor='center', font=('Ivy 10  bold'), bg=corFundo, fg=corTitulo)

l_titulo.place(x=1, y=1)

b1 = Button(janMain, text="Iniciar",width=larguraBotao, height=alturaBotao, command=jan_game, relief='flat', anchor='nw', overrelief='solid', font=('Ivy 8  bold'), bg=corTitulo, fg=corFundo)

b1.place(x=250,y=150)

b2 = Button(janMain, text="Config",width=larguraBotao-1, height=alturaBotao-1, relief='flat', anchor='nw', overrelief='solid', font=('Ivy 8  bold'), bg=corTitulo, fg=corFundo)

b2.place(x=250,y=300)

b3 = Button(janMain, text="Personalizar",width=larguraBotao, height=alturaBotao, command=jan_person, relief='flat', anchor='nw', overrelief='solid', font=('Ivy 8  bold'), bg=corTitulo, fg=corFundo)

b3.place(x=250,y=400)

main.mainloop()