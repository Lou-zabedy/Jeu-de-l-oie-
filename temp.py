import random
from tkinter import *
from random import choice
import tkinter.font as font
from tkinter import messagebox

#variables
x=460 #position x en départ image pion noir
y=700  #position y en départ image pion noir

x1=420 #position x de depart image pion vert
y1=690 #position y de depart image pion vert
nb1=0 #valeur du dé 1 noir
numcase=1 #numéro du case pour pion noir

nb2=0 #valeur du dé 2 vert
numcaseV=1 #numéro du case pour pion vert
casexV=[460,530,620,720,820,920,1020,1120,1120,1120,1120,1120,1120,1120,1120,1000,900,800,700,620,520,420,
       420,420,420,420,420,420,520,620,720,820,920,1020,1020,1020,1020,1020,1020,920,820,720,620,520,520,
       520,520,520,620,720,820,920,920,920,920,820,720,620,620,620,720,820,780]

caseyV=[700,700,700,700,700,700,700,700,600,500,400,300,200,100,25,25,25,25,25,25,25,25,130,235,320,420,520,
       610,610,610,610,610,610,610,510,410,310,210,120,120,120,120,120,120,220,320,420,520,520,520,520,520,
       420,320,220,220,220,220,320,420,420,420,320]

casex=[460,530,620,720,820,920,1020,1120,1120,1120,1120,1120,1120,1120,1120,1000,900,800,700,620,520,420,
       420,420,420,420,420,420,520,620,720,820,920,1020,1020,1020,1020,1020,1020,920,820,720,620,520,520,
       520,520,520,620,720,820,920,920,920,920,820,720,620,620,620,720,820,780]

casey=[700,700,700,700,700,700,700,700,600,500,400,300,200,100,25,25,25,25,25,25,25,25,130,235,320,420,520,
       610,610,610,610,610,610,610,510,410,310,210,120,120,120,120,120,120,220,320,420,520,520,520,520,520,
       420,320,220,220,220,220,320,420,420,420,320]

#création de la fenetre d'accueil du jeu
def create():
    fen_principale = Toplevel(root)
root = Tk()
root.title("Jeu de l'oie created by 1.3.1.2")
root.geometry('1200x800+0+0')

canvas1=Canvas(root,width=1200,height=800,bg='white')
bb=PhotoImage(file='11854.png')
item3=canvas1.create_image(0,0,image=bb,anchor=NW)

start=PhotoImage(file="text.png")
btn = Button(root,image=start,width=320,height=130,command =root.destroy)

btn.place(x=520,y=650)

canvas1.pack()

root.mainloop()

#création de la deuxième fenetre du jeu
fen_principale = Tk()
fen_principale.title("Jeu de l'oie")
fen_principale.geometry('1280x800+0+0')


def lancer():  #fonction permettant le lancer aléatoire du dé + déplacement du pion noir
    global numcase
    nb1 = random.randint(1,6)

    numero['text'] = "Résultat : %s" % nb1
    numcase=numcase+nb1
    while numcase>62:
        numcase=numcase-nb1
        item2.place(x=casex[numcase], y=casey[numcase])

    if numcase==62:#affichage du message du gagnant

        messagebox.showinfo("Chkoun rba7", "Eli yal3b bnoir saha lik sahbi")


#tous les conditions du jeu
    # condition1
    if numcase==5:
        numcase = numcase + 6
        item2.place(x=casex[numcase], y=casey[numcase])
    # condition2
    if numcase == 11:
        numcase = numcase - 2
        item2.place(x=casex[numcase], y=casey[numcase])
    # condition3
    if numcase == 17:
        numcase = numcase + 15
        item2.place(x=casex[numcase], y=casey[numcase])
    # condition4
    if numcase == 23:
        numcase = numcase - 8
        item2.place(x=casex[numcase], y=casey[numcase])
    # condition5
    if numcase == 29:
        numcase = numcase + 6
        item2.place(x=casex[numcase], y=casey[numcase])
    # condition6
    if numcase == 35:
        numcase = numcase - 2
        item2.place(x=casex[numcase], y=casey[numcase])
    # condition7
    if numcase == 41:
        numcase = numcase + 30
        item2.place(x=casex[numcase], y=casey[numcase])
        # condition8
    if numcase == 47:
        numcase = numcase - 40
        item2.place(x=casex[numcase], y=casey[numcase])
    # condition9
    if numcase == 53:
        numcase = numcase + 10
        item2.place(x=casex[numcase], y=casey[numcase])
    # condition10
    if numcase == 59:
        numcase = numcase - 20
        item2.place(x=casex[numcase], y=casey[numcase])

    item2.place(x=casex[numcase],y=casey[numcase])


def lancerV():  # fonction permettant le lancer aléatoire du dé + déplacement du pion vert
    global numcaseV
    nb2 = random.randint(1,6)

    numero['text'] = "Résultat : %s" % nb2
    numcaseV = numcaseV + nb2
    while numcaseV>62:
        numcaseV=numcaseV-nb2
        item3.place(x=casexV[numcaseV], y=caseyV[numcaseV])

    if numcaseV==62:

        messagebox.showinfo("Chkoun rba7", "Eli yal3b bvert saha lik sahbi")

    # condition1
    if numcaseV == 5:
        numcaseV = numcaseV + 6
        item3.place(x=casexV[numcaseV], y=caseyV[numcaseV])
    # condition2
    if numcaseV == 11:
        numcaseV = numcaseV - 2
        item3.place(x=casexV[numcaseV], y=caseyV[numcaseV])
    # condition3
    if numcaseV == 17:
        numcaseV = numcaseV + 15
        item3.place(x=casexV[numcaseV], y=caseyV[numcaseV])
    # condition4
    if numcaseV == 23:
        numcaseV = numcaseV - 8
        item3.place(x=casexV[numcaseV], y=caseyV[numcaseV])
    # condition5
    if numcaseV == 29:
        numcaseV = numcaseV + 6
        item3.place(x=casexV[numcaseV], y=caseyV[numcaseV])
    # condition6
    if numcaseV == 35:
        numcaseV = numcaseV - 2
        item3.place(x=casexV[numcaseV], y=caseyV[numcaseV])
    # condition7
    if numcaseV == 41:
        numcaseV = numcaseV + 30
        item3.place(x=casexV[numcaseV], y=caseyV[numcaseV])
        # condition8
    if numcaseV == 47:
        numcaseV = numcaseV - 40
        item3.place(x=casexV[numcaseV], y=caseyV[numcaseV])
    # condition9
    if numcaseV == 53:
        numcaseV = numcaseV + 10
        item3.place(x=casexV[numcaseV], y=caseyV[numcaseV])
    # condition10
    if numcaseV == 59:
        numcaseV = numcaseV - 20
        item3.place(x=casexV[numcase], y=caseyV[numcase])
    item3.place(x=casexV[numcaseV], y=caseyV[numcaseV])


#premier dé noir
de = Button(fen_principale,text="lancer le dé N", width=12, command=lancer)
de.place(x=20, y=350)

#deuxième dé vert
deV=Button(fen_principale,text="lancer le dé V",width=12,command=lancerV)
deV.place(x=20,y=430)


#ce que le dé 1 affiche
numero = Label(fen_principale, text="Résultat :  ", width=14)
numero.pack(padx=20, pady=20, side="left")


canvas=Canvas(fen_principale,width=940,height=800,bg='white')
canvas.pack()

pic=PhotoImage(file='3.gif')
pion=PhotoImage(file='pion noir.png')
pionVert=PhotoImage(file='pion2.png')

item1=canvas.create_image(0,0,image=pic,anchor=NW)#tapis du jeu


item2=Label(image=pion,width=34,height=63 )#pion noir
item2.place(x=460,y=700)

item3=Label(image=pionVert,width=31,height=61)#pion vert
item3.place(x=420,y=690)


fen_principale.mainloop()