from tkinter import*

def click(event):
    global scvalue
    text=event.widget.cget("text")
    #print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value= int(scvalue.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                print(e)
                value="Error"
                screen.update()
        scvalue.set(value)
        screen.update()
    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root=Tk()


root.geometry("900x800")
root.title("DIVYANSHU CALCULATOR")

scvalue= StringVar()
scvalue.set("")
my_label=Label(root,text="DIVYANSHU CALCULATOR WELCOMES YOU!",font="lucida 20 bold ").pack()

screen=Entry(root,textvar=scvalue,font="lucida 40 bold")
screen.pack(fill=X)
f=Frame(root,bg="gray")
f.pack()
b=Button(f,text="9",padx=12,pady=10,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=12,pady=8)
b=Button(f,text="8",padx=12,pady=10,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=12,pady=8)
b=Button(f,text="7",padx=12,pady=10,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=12,pady=8)


f=Frame(root,bg="gray")
f.pack()

b=Button(f,text="6",padx=12,pady=10,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=12,pady=8)

b=Button(f,text="5",padx=12,pady=10,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=12,pady=8)
b=Button(f,text="4",padx=12,pady=10,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=12,pady=8)
f=Frame(root,bg="gray")
f.pack()
b=Button(f,text="3",padx=12,pady=10,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=12,pady=8)

b=Button(f,text="2",padx=12,pady=10,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=12,pady=8)

b=Button(f,text="1",padx=12,pady=10,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=12,pady=8)
b=Button(f,text="0",padx=12,pady=10,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=10,pady=8)
f=Frame(root,bg="gray")
f.pack()
b=Button(f,text="-",padx=12,pady=10,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=12,pady=8)
b=Button(f,text="+",padx=12,pady=10,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=12,pady=8)

b=Button(f,text="*",padx=12,pady=10,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=10,pady=8)

b=Button(f,text="%",padx=8,pady=10,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=RIGHT,padx=10,pady=8)
f=Frame(root,bg="gray")
f.pack()
b=Button(f,text="/",padx=12,pady=10,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=12,pady=8)
b=Button(f,text="=",padx=12,pady=10,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=12,pady=8)

b=Button(f,text="C",padx=8,pady=8,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=8,pady=8)
b=Button(f,text=".",padx=12,pady=10,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=12,pady=10)
f=Frame(root,bg="gray")
f.pack()

root.mainloop()