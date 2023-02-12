import tkinter
import turtle as t

window=tkinter.Tk()
window.title("Hello GUI")
window.minsize(width=600,height=600)


label1=tkinter.Label(text="First Label", font=("Arial",24,"bold"),bg="navy",fg="yellow")
label1.pack(side="right") #geometry-management mechanism

micky=t.Turtle()
micky.penup()
micky.setpos(-300,0)
micky.write("I shall give her what she deserves.",font=("Courier",25,"bold"),align="left")

window.mainloop()