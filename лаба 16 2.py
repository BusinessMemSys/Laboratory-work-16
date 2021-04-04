from tkinter import *
 


 
canvas = Canvas()
canvas.create_oval(10, 10, 200, 200, outline="#05f",fill="#05f", width=2)
canvas.create_rectangle(30, 50, 180, 160, outline="#fb0", fill="#fb0")
 
 
canvas.pack(fill=BOTH, expand=1)
 
 
def main():
    root = Tk()
    root.geometry("400x250")
    root.mainloop()
 
 
if __name__ == '__main__':
    main()