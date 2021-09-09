from tkinter import *
from PIL import Image,ImageTk
import calendar

root = Tk()
root["bg"] = "#d6d2d2"
#window size
root.title("Calendar")
root.maxsize(1000,800)
root.geometry("800x500")
Title_label = Label(root,text="CALENDAR",bg = "#d6d2d2",font = ("Heiti SC",30,"bold"))
Title_label.place(x = 325,y = 20)

# Function
def text():
    month_int = int(month.get())
    year_int = int(year.get())
    cal = calendar.month(year_int, month_int)
    textfield.delete(0.0, END)
    textfield.insert(INSERT, cal)

#picture
cal_photo = PhotoImage(file = "/Users/samiradeepak/Downloads/calendar_new1.png")
cal_label = Label(root,image = cal_photo)
cal_label.place(x = 355 , y = 70)


# Creating Labels
m = Label(root, text="Month:",bg = "#d6d2d2")
m["font"] = ("Al Bayan",14)
m["foreground"] = "#df283a"
m.place(x = 200, y = 200)

y = Label(root, text="Year:",bg = "#d6d2d2")
y["font"] = ("Al Bayan",14)
y["foreground"] = "#df283a"
y.place(x = 430 , y = 200)

# Creating spinbox
month = Spinbox(root, from_=1, to=12, width=8)
month["font"] = ("Al Bayan",14)
month["bg"] = "#d6d2d2"
month["highlightbackground"] = "#913cc1"
month.place(x = 259 ,y = 200)

year = Spinbox(root, from_=2000, to=2100, width=10)
year["font"] = ("Al Bayan",14)
year["bg"] = "#d6d2d2"
year["highlightbackground"] = "#913cc1"
year.place(x = 479,y = 200 )

# Creating Button
show = Button(root, text="Show", command=text)
show["font"] = ("Al Bayan",14)
show["highlightbackground"] = "#649cff"
show["width"] = 20
show.place(x = 335 ,y = 400 )


# Creating Textfield
textfield = Text(root, width=30, height=10, fg="black",bg = "#d6d2d2")
textfield.place(x= 325  ,y = 250)


root.mainloop()