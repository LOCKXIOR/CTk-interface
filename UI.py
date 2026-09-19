from customtkinter import*

screen=CTk()
screen.geometry("400x200")

Liste_nom=[]

Texte=CTkLabel(screen, text="Saisie ton nom", font=("Calibri",15));Texte.pack(pady=10)

entrée=CTkEntry(screen, width=220);entrée.pack(pady=25)
kk=False

def vali():
    a=entrée.get().strip().replace(" ","").title()
    entrée.delete(0,"end")
    Liste_nom.append(a)
    if kk==False:
        Texte.configure(text=f"Bonjour {a} !")
    else:
        Texte.configure(text=f"Noms : {', '.join(Liste_nom)}")
        
def initia():
    Texte.configure(text="Saisie ton nom", font=("Calibri",15))
    Noms.pack()
    retour.pack_forget()
    
def liste_n():
    global kk
    kk=True
    Texte.configure(text=f"Noms : {', '.join(Liste_nom)}")
    retour.pack()
    Noms.pack_forget()
    
Vaal=CTkButton(screen, text="Cliquez",command=vali);Vaal.pack(pady=5)
Noms=CTkButton(screen, text="Liste de noms",command=liste_n);Noms.pack()
retour=CTkButton(screen, text="Retour", fg_color="dark red",command=initia)
screen.mainloop()
