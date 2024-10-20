
from tkinter import Tk, Button
count = 0 # Records the number of button presses
counter = 0 # Records the number of button presses for the 2nd button


# Updates the count label within the graphical button
def update():
    global count, b
    count += 1
    b.config(text="Click Count = " + str(count))
    print("Updating")


# Updates the count label within the graphical button
def updating():
    global counter, c
    counter += 5
    c.config(text="2nd Click Count = " + str(counter))
    print("Updated")
    
root = Tk()
b = Button(root)
c = Button(root)
b.configure(background="yellow", text="Click Count = 0", command=update)
c.configure(background="red", text="2nd Click Count = 0", command=updating)
b.pack()
c.pack()
root.mainloop()

