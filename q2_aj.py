from tkinter import *
import math as m


#create app root
root=Tk()

#window title
root.title("AGE OF CALCULATOR")

#window geomtery width x height
root.geometry("1000x1000")

#window background
root["bg"]="grey"

#age  calculator label
age_calculator_label= Label(root)
age_calculator_label.place(x=365,y=10)
age_calculator_label["bg"]="grey"

#dictionary attributes
age_calculator_label["text"]="Age Calculator"
age_calculator_label["font"]=("Arial",30)

#steps for any widget creation
#1. write name of widget class
#2. pass root as parameter to class
#3. save it in a variable
#4. pack, place, grid

#date of birth label
date_of_birth_label=Label(root)
date_of_birth_label.place(x=180,y=60)


#given date label
given_date_label=Label(root)
given_date_label.place(x=580,y=60)


#dictionary attributes
date_of_birth_label["text"]="Date of Birth:"
date_of_birth_label["font"]=("Calibri",30)

#dictionary atributes
given_date_label["text"]="Given Date:"
given_date_label["font"]=("Calibri",30)

#day label
Day_label=Label(root , text="Day: ")
Day_label.place(x=180,y=135)
Day_label["font"]=("Calibri",20)

#textbox for day label
Day_label_entrytext = Entry(root)
Day_label_entrytext.place(x=250,y=135)

#given day
Given_day_label=Label(root, text="Given Day: ")
Given_day_label.place(x=580,y=135)
Given_day_label["font"]=("Calibri",20)

#textbox for given day label
Given_day_label_entrytext = Entry(root)
Given_day_label_entrytext.place(x=705,y=135)

#month label
month_label =Label(root,text="Month:")
month_label.place(x=180,y=195)
month_label["font"]=("Calibri",20)


#textbox for the mothn label
month_label_entrytext = Entry(root)
month_label_entrytext.place(x=260,y=195)

#given month label
given_month_label= Label(root,text="Given Month:")
given_month_label.place(x=570,y=200)
given_month_label['font']=("Calibri",20)

#textbox for given month label
given_month_label_entrytext=Entry(root)
given_month_label_entrytext.place(x=710,y=200)

#year label
year_label = Label(root, text = "Year:")
year_label.place(x=180,y=250)
year_label["font"]=("Calibri",20)

#text box for year label
year_label_entrytext = Entry(root)
year_label_entrytext.place(x=250,y=250)

# given year label
given_year_label= Label(root,text ="Given Year:")
given_year_label.place(x=580,y=260)
given_year_label["font"]=("Calibri",20)

#textbox for given label
given_year_label_entrytext= Entry(root)
given_year_label_entrytext.place(x=700,y=260)

#resultant data
resultant_date_button= Button(root,text="Resultant Date")
resultant_date_button.place(x=390,y=350)
resultant_date_button["font"]=("Arial",30)

#year resultant label
year_resultant_label= Label(root , text="Year")
year_resultant_label.place(x=450,y=420)
year_resultant_label["font"]=("Calibri",20)

#month resultant label
month_resultant_label = Label(root,text ="Month")
month_resultant_label.place(x=450,y=520)
month_resultant_label["font"]=("Calibri",20)

#textybox for year resultant label
year_resultant_label_entrytext = Entry(root)
year_resultant_label_entrytext.place(x=390,y=470)

#textbox for moth label
month_resultant_entrytext = Entry(root)
month_resultant_entrytext.place(x=390,y=570)

#day resultant label
day_resultant_label= Label(root, text="Day")
day_resultant_label.place(x=450,y=630)
day_resultant_label["font"]=("Calibri",20)

#textbox for day resultant label
day_resultant_entrytext= Entry(root)
day_resultant_entrytext.place(x=390,y=680)

def clear():
    year_resultant_label_entrytext.delete(0,END)
    day_resultant_entrytext.delete(0,END)
    month_resultant_entrytext.delete(0,END)
    Day_label_entrytext.delete(0,END)
    month_label_entrytext.delete(0,END)
    year_label_entrytext.delete(0,END)
    Given_day_label_entrytext.delete(0,END)
    given_month_label_entrytext.delete(0,END)
    given_year_label_entrytext.delete(0,END)


#clear button
button_clear = Button(root,text = "Clear",command = clear)
button_clear.place(x=390,y=730)
button_clear["font"]=("Calibri",20)


#start or run the window
root.mainloop()