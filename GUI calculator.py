from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
          value = int(scvalue.get())
        else:
            value = eval(screen.get())
            
        scvalue.set(value)
        screen.update()
        
    elif text == "C":
        scvalue.set(" ")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update
     
root = Tk()
root.geometry("230x350")
root.title("Calculator")
root.configure(bg="black")
scvalue = StringVar()
scvalue.set("")
screen = Entry(root,textvar = scvalue, font="lucida 15 bold")
screen.pack(fill=X,ipadx=8,padx=10,pady=10)

F1 = Frame(root,bg="black")
B = Button(F1,text = "C",padx=10,pady=6, font="lucida 15 bold",bg="blue")
B.bind("<Button-1>",click)
B.pack(side = LEFT,padx = 3,pady = 3)

B = Button(F1,text = "/",padx=13,pady=7, font="lucida 14 bold",bg="grey")
B.bind("<Button-1>",click)
B.pack(side = LEFT,padx = 3,pady = 3)

B = Button(F1,text = "%",padx=3,pady=7, font="lucida 14 bold",bg="grey")
B.bind("<Button-1>",click)
B.pack(side = LEFT,padx = 5,pady = 3)
B = Button(F1,text = "*",padx=12,pady=7, font="lucida 15 bold",bg="grey")
B.bind("<Button-1>",click)
F1.pack()

F1 = Frame(root,bg="black")
B.pack(side = LEFT,padx = 8,pady = 5)
B = Button(F1,text = "7",padx=10,pady=6, font="lucida 15 bold", bg="grey")
B.bind("<Button-1>",click)
B.pack(side = LEFT,padx = 3,pady = 3)
B = Button(F1,text = "8",padx=10,pady=6, font="lucida 15 bold",bg="grey")
B.bind("<Button-1>",click)
B.pack(side = LEFT,padx = 3,pady = 3)
B = Button(F1,text = "9",padx=10,pady=6, font="lucida 15 bold",bg="grey")
B.bind("<Button-1>",click)
B.pack(side = LEFT,padx = 3,pady = 3)
B = Button(F1,text = "-",padx=10,pady=6, font="lucida 16 bold",bg="grey")

B.bind("<Button-1>",click)
F1.pack()

F1 = Frame(root,bg="black")
B.pack(side = LEFT,padx = 8,pady = 5)
B = Button(F1,text = "4",padx=10,pady=6, font="lucida 15 bold",bg="grey")
B.bind("<Button-1>",click)
B.pack(side = LEFT,padx = 3,pady = 3)
B = Button(F1,text = "5",padx=10,pady=6, font="lucida 15 bold",bg="grey")
B.bind("<Button-1>",click)
B.pack(side = LEFT,padx = 3,pady = 3)
B = Button(F1,text = "6",padx=10,pady=6, font="lucida 15 bold",bg="grey")
B.bind("<Button-1>",click)
B.pack(side = LEFT,padx = 3,pady = 3)
B = Button(F1,text = ".",padx=10,pady=6, font="lucida 16 bold",bg="grey")
B.bind("<Button-1>",click)
F1.pack()

F1 = Frame(root,bg="black")
B.pack(side = LEFT,padx = 3,pady = 3)
B = Button(F1,text = "1",padx=10,pady=6, font="lucida 15 bold",bg="grey")
B.bind("<Button-1>",click)
B.pack(side = LEFT,padx = 3,pady = 3)

B = Button(F1,text = "2",padx=10,pady=6, font="lucida 15 bold",bg="grey")
B.bind("<Button-1>",click)
B.pack(side = LEFT,padx = 3,pady = 3)

B = Button(F1,text = "3",padx=10,pady=6, font="lucida 15 bold",bg="grey")
B.bind("<Button-1>",click)
B.pack(side = LEFT,padx = 3,pady = 3)
B = Button(F1,text = "0",padx=10,pady=6, font="lucida 15 bold",bg="grey")
B.bind("<Button-1>",click)
B.pack(side = LEFT,padx = 3,pady = 3)
F1.pack()

F1 = Frame(root,bg="black")
B.pack(side = LEFT,padx = 3,pady = 3)
B = Button(F1,text = "=",padx=45,pady=6, font="lucida 15 bold",bg= "Orange")
B.bind("<Button-1>",click)
B.pack(side = LEFT,padx = 3,pady = 3)

B = Button(F1,text = "+",padx=30,pady=6, font="lucida 15 bold",bg="grey")
B.bind("<Button-1>",click)
B.pack(side = LEFT,padx = 3,pady = 3)
#B.pack(side = LEFT,padx = 10,pady = 7)
F1.pack()

root.mainloop()

