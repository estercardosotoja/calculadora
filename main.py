# Importando Tkinter
from tkinter import *
from tkinter import ttk

# Definindo Cores
cor1 = "#1b1c1b" # Black
cor2 = "#e6ede6" # White
cor3 = "#022a5c" # Blue
cor4 = "#39444d" # Gray
cor5 = "#c4690e" # Orange

# Criando popup
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=cor1)

# Criando Frames
frame_tela = Frame(janela, width=235, height=50)
frame_tela.grid(row=0, column=0)
frame_tela.config(bg=cor4)

frame_body = Frame(janela, width=235, height=268)
frame_body.grid(row=1, column=0)
frame_body.config(bg=cor3)

# Logica da Calculadora
value_text = StringVar()
every_value = " "


def entry_value(event):
    global every_value
    every_value = every_value + str(event)
    value_text.set(every_value)


def calculation():
    result = eval(every_value)
    print(result)
    value_text.set(str(result))

def clean():
    global every_value
    every_value = " "
    value_text.set(' ')


# Crindo Label
app_label = Label(frame_tela, textvariable=value_text, width=16, height=2, padx=7,  font='Ivy 18', relief=FLAT,
                  anchor="e", justify=RIGHT, bg=cor3, fg=cor2)
app_label.place(x=0, y=0)


# Criando Botões
bC = Button(frame_body, command=clean ,  text="C", width=11, height=2, bg=cor2, font='Ivy 12 bold', relief=RAISED,
            overrelief=RIDGE)
bC.place(x=0, y=0)
bPorc = Button(frame_body, command=lambda: entry_value('%'), text="%", width=5, height=2, bg=cor2, font='Ivy 12 bold',
               relief=RAISED, overrelief=RIDGE)
bPorc.place(x=118, y=0)
bDiv = Button(frame_body, command=lambda: entry_value('/'), text="/", width=5, height=2, bg=cor5, font='Ivy 12 bold',
              relief=RAISED, overrelief=RIDGE)
bDiv.place(x=176, y=0)

b7 = Button(frame_body, command=lambda: entry_value('7'), text="7", width=5, height=2, bg=cor2, font='Ivy 12 bold',
            relief=RAISED, overrelief=RIDGE)
b7.place(x=0, y=52)
b8 = Button(frame_body, command=lambda: entry_value('8'), text="8", width=5, height=2, bg=cor2, font='Ivy 12 bold',
            relief=RAISED, overrelief=RIDGE)
b8.place(x=59, y=52)
b9 = Button(frame_body, command=lambda: entry_value('9'), text="9", width=5, height=2, bg=cor2, font='Ivy 12 bold',
            relief=RAISED, overrelief=RIDGE)
b9.place(x=118, y=52)
bMul = Button(frame_body, command=lambda: entry_value('*'), text="*", width=5, height=2, bg=cor5, font='Ivy 12 bold',
              relief=RAISED, overrelief=RIDGE)
bMul.place(x=177, y=52)

b4 = Button(frame_body, command=lambda: entry_value('4'), text="4", width=5, height=2, bg=cor2, font='Ivy 12 bold',
            relief=RAISED, overrelief=RIDGE)
b4.place(x=0, y=104)
b5 = Button(frame_body, command=lambda: entry_value('5'), text="5", width=5, height=2, bg=cor2, font='Ivy 12 bold',
            relief=RAISED, overrelief=RIDGE)
b5.place(x=59, y=104)
b6 = Button(frame_body, command=lambda: entry_value('6'), text="6", width=5, height=2, bg=cor2, font='Ivy 12 bold',
            relief=RAISED, overrelief=RIDGE)
b6.place(x=118, y=104)
bSub = Button(frame_body, command=lambda: entry_value('-'), text="-", width=5, height=2, bg=cor5, font='Ivy 12 bold',
              relief=RAISED, overrelief=RIDGE)
bSub.place(x=177, y=104)

b3 = Button(frame_body, command=lambda: entry_value('3'), text="3", width=5, height=2, bg=cor2, font='Ivy 12 bold',
            relief=RAISED, overrelief=RIDGE)
b3.place(x=0, y=156)
b2 = Button(frame_body, command=lambda: entry_value('2'), text="2", width=5, height=2, bg=cor2, font='Ivy 12 bold',
            relief=RAISED, overrelief=RIDGE)
b2.place(x=59, y=156)
b1 = Button(frame_body, command=lambda: entry_value('1'), text="1", width=5, height=2, bg=cor2, font='Ivy 12 bold',
            relief=RAISED, overrelief=RIDGE)
b1.place(x=118, y=156)
bSoma = Button(frame_body, command=lambda: entry_value('+'), text="+", width=5, height=2, bg=cor5, font='Ivy 12 bold',
               relief=RAISED, overrelief=RIDGE)
bSoma.place(x=177, y=156)

b0 = Button(frame_body, command=lambda: entry_value('0'), text="0", width=11, height=2, bg=cor2, font='Ivy 12 bold',
            relief=RAISED, overrelief=RIDGE)
b0.place(x=0, y=208)
bPonto = Button(frame_body, command=lambda: entry_value('.'), text=".", width=5, height=2, bg=cor2, font='Ivy 12 bold',
                relief=RAISED, overrelief=RIDGE)
bPonto.place(x=118, y=208)
bIgual = Button(frame_body, command=calculation, text="=", width=5, height=2, bg=cor5, font='Ivy 13 bold',
                relief=RAISED, overrelief=RIDGE)
bIgual.place(x=176, y=208)


janela.mainloop()
