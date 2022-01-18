# tkinter module for GUI
from tkinter import*
import calendar

# initialize the window screen
root = Tk()

# naming window
root.title("Calendar Finder...")

# giving height x width + position from left + position from top
root.geometry('600x600+380+20')

# function that perform task on clicking the button...
def calendarShow():
    year = entry1.get()
    month = entry2.get()
    result = calendar.month(year, month)
    l3 = Label(root, text = result)
    l3.place(x = 220, y = 400)

# variable for accepting the values given by the user ...
entry1 = IntVar()
entry2 = IntVar()

# label l1 and entry e1
l1 = Label(root, text = "Enter the year please.", font = 16)
l1.place(x = 220, y = 100)
e1 = Entry(root, width = 25, textvariable = entry1)
e1.place(x = 220,  y = 130)

# label l2 and Entry e2
l2 = Label(root, text = "Enter month please.", font = 16)
l2.place(x = 220 , y = 200)
e2 = Entry(root, width = 25, textvariable = entry2)
e2.place(x = 220, y = 230)

btn1 = Button(root, text = "show calendar", command = calendarShow)
btn1.place(x = 245, y = 300)

# stop the window in a loop
root.mainloop()