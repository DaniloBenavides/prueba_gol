from tkinter import *

x=0
y=110
tk = Tk()
canvas = Canvas(tk, width=600, height=600)
canvas.pack()
img = PhotoImage(file="pelota.gif")
canvas.create_image(0,240,anchor=NW,image=img)
img2 = PhotoImage(file="arco.gif")
canvas.create_image(400,200,anchor=NW,image=img2)
def mover(event):
    global x
    global y
    if event.keysym == 'Left':
        canvas.move(1, -5, 0)
        x=x-5
        print(x)
    else:
        canvas.move(1, 5, 0)
        x=x+5
        print(x)
        if(x==380):
            print("GOLLLLLLLLLLL.......")
            exit()
    
##widget=Label(text="gool")  
##widget.grid(row=0,column=1)

canvas.bind_all('<KeyPress-Left>', mover)
canvas.bind_all('<KeyPress-Right>', mover)


##widget.mainloop()
tk.mainloop()
