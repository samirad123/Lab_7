from tkinter import *
from PIL import Image,ImageTk
import calendar
root = Tk()

#function
def text():
    month_int = int(month.get())
    year_int = int(year.get())
    cal = calendar.month(year_int, month_int)
    textbox.delete(0.0, END)
    textbox.insert(INSERT, cal)


#window size
root.title("Calendar")
root.maxsize(1000,800)
root.geometry("800x500")
Title_label = Label(root,text="CALENDAR",font = ("Heiti SC",30,"bold"))
Title_label.place(x = 300,y = 20)



#Create a canvas
cal_photo = PhotoImage(file = "/Users/samiradeepak/Downloads/calendar_icon.png")
cal_label = Label(root,image = cal_photo)
cal_label.pack()
canvas = Canvas(root, width= 600, height= 400)
canvas.place(x = 320 ,y = 70)
#Load an image in the script
img = (Image.open("/Users/samiradeepak/Downloads/calendar_icon.png"))
#Resize the Image using resize method
resized_image= img.resize((100,100), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
#Add image to the Canvas Items
canvas.create_image(10,10, anchor=NW, image=new_image)


#Month label
month = Label(root,text = "Month :")
month.place(x = 200 ,y = 200 )
list_of_months = [1,2,3,4,5,6,7,8,9,10,11,12]
#optionmenu or dropdown for months
temp1 = StringVar()
months_optionmenu = OptionMenu(root,temp1,*list_of_months)
months_optionmenu.place(x = 259,y = 200)
temp1.set("Select the month")


#Year label
year = Label(root,text = "Year :")
year.place(x = 430 ,y = 200)
#optionmenu or dropdown for years
list_of_years = [2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030]
temp2 = StringVar()
years_optionmenu = OptionMenu(root,temp2,*list_of_years)
years_optionmenu.place(x = 479,y = 200)
temp2.set("Select the year")

#show label
show = Button(root,text = "Show",command = text)
show.place(x = 320 ,y = 400)

#text/font of the calendar
textbox = Text(root, width=25, height=10, foreground ="red")
textbox.place(x=350, y=500)



























root.mainloop()

















































