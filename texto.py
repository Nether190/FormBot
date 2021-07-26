from tkinter import Tk, Label, Entry, Button

my_w = Tk()
my_w.geometry("300x350")  
my_w.title('My Title')
my_w.wm_iconbitmap('logo_forms.ico')

l0 = Label(my_w,  text='E-mail', width=10 )
l0.pack() 

t0 = Entry(my_w, bg='white')
t0.pack(ipady=3)

l1 = Label(my_w,  text='Nome', width=10 )
l1.pack() 

t1 = Entry(my_w, bg='white')
t1.pack(ipady=3) 

l2 = Label(my_w, text='Número', width=10 ) 
l2.pack() 

t2 = Entry(my_w, bg='white')
t2.pack(ipady=3) 

l3 = Label(my_w,  text='Turma', width=10 ) 
l3.pack() 

t3 = Entry(my_w, bg='white')
t3.pack(ipady=3) 

l4 = Label(my_w,  text='Grupamento', width=10 ) 
l4.pack() 

t4 = Entry(my_w, bg='white')
t4.pack(ipady=3)

l5 = Label(my_w,  text='Camil/Cauni', width=10 ) 
l5.pack() 

t5 = Entry(my_w, bg='white')
t5.pack(ipady=3)

def printValue():
    valor = []
    if len(valor) == 6:
        pass
    else:
        n0 = t0.get()
        n1 = t1.get()
        n2 = t2.get()
        n3 = t3.get()
        n4 = t4.get()
        n5 = t5.get()
        valor.append(n0)
        valor.append(n1)
        valor.append(n2)
        valor.append(n3)
        valor.append(n4)
        valor.append(n5)
        with open('dados.txt', 'w') as nota:
            for x in valor:
                nota.write(x+"\n")


Button(
    my_w,
    text="Registrar", 
    padx=10, 
    pady=5,
    bg='lightgreen',
    command=lambda:printValue()
    ).pack(pady=10)

my_w.mainloop()