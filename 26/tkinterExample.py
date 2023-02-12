import tkinter
import turtle as t

window=tkinter.Tk()
window.title("Hello GUI")
window.minsize(width=600,height=600)


label1=tkinter.Label(text="First Label", font=("Arial",24,"bold"),bg="navy",fg="yellow")
#label1.pack(side="right") #geometry-management mechanism
label1.pack()

label1["text"]="New First Label"
label1.config(text="Passport Please")



def button1_clicked():
    label1["text"]=input.get()

button1=tkinter.Button(text="Click Me",command=button1_clicked)
button1.pack()


input= tkinter.Entry(width=30)
input.pack()
#label1.config(text=input.get())
#label1["text"]=input.get()

micky=t.Turtle()
micky.penup()
micky.setpos(-300,0)
micky.write("I shall give her what she deserves.",font=("Courier",25,"bold"),align="left")

window.mainloop()