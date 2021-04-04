from tkinter import *
root=Tk()
canv=Canvas(root,width=1000,height=1000,bg="lightblue",cursor="pencil")

canv.create_rectangle(20,150,400,300,fill="blue",outline="black")
canv.create_rectangle(250,20,400,150,fill="blue",outline="black")
canv.create_rectangle(40,40,80,150,fill="blue",outline="black")
canv.create_oval(50,250,150,350,fill="black",outline="black")
canv.create_oval(170,250,270,350,fill="black",outline="black")
canv.create_oval(290,225,400,350,fill="black",outline="black")
canv.create_rectangle(240,15,410,30,fill="black",outline="black")
canv.pack()

root.mainloop()