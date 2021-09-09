from tkinter import *
root = Tk()

def checkError():
    # if any of the entry field is empty show an error message and clear
    if (birth_day.get() == "" or birth_month.get() == ""
            or birth_year.get() == "" or given_day.get() == ""
            or given_month.get() == "" or given_year.get() == ""):
        # error message
        messagebox.showerror("Input Error")
        clearAll()
        return -1

def click_clear_button():
    # clears all inputs and outputs
    day_of_birth.delete(0, END)
    month_of_birth.delete(0, END)
    year_of_birth.delete(0, END)
    given_day.delete(0, END)
    given_month.delete(0, END)
    given_year.delete(0, END)
    result_year.delete(0, END)
    result_day.delete(0, END)
    result_month.delete(0, END)

    print("Your form has been cleared")

clear_button = Button(root,command = click_clear_button)
clear_button.place(x = 440,y = 370)
clear_button["text"] = "Clear"


def CalculateAge():
    value = checkError()
    if value == -1:
        return
    else:
        birth_day = int(day_of_birth_entrytext.get())
        birth_month = int(month_of_birth_entrytext.get())
        birth_year = int(year_of_birth_entrytext.get())

        given_day = int(given_day_entrytext.get())
        given_month = int(month_of_birth_entrytext.get())
        given_year = int(year_of_birth_entrytext.get())

        month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if (birth_day > given_day):
            given_month = given_month - 1
            given_day = given_day + month[birth_month - 1]

        if (birth_month > given_month):
            given_year = given_year - 1
            given_month = given_month + 12

        calculated_day = given_day - birth_day
        calculated_month = given_month - birth_month
        calculated_year = given_year - birth_year

    result_day_entrytext.insert(0,str(calculated_day))
    result_month_entrytext.insert(0,str(calculated_month))
    result_year_entrytext.insert(0,str(calculated_year))


root.title("Age Calculator")

root.geometry("800x800")
root.maxsize(10000,10000)

root["bg"] = "white"

age_calculator = Label(root)
age_calculator.pack()

age_calculator["text"] = "AGE CALCULATOR"
age_calculator["font"] = ("Al Tarikh",30,"bold","underline")

date_of_birth = Label(root,text = "Date of Birth")
date_of_birth.place(x = 70,y = 70)

day_of_birth = Label(root,text = "Day :")
day_of_birth.place(x = 50,y = 100)
day_of_birth_entrytext = Entry(root,bg = "#9096e6",fg ="white",borderwidth = 3)
day_of_birth_entrytext.place(x = 100,y=100)

month_of_birth = Label(root,text = "Month :")
month_of_birth.place(x = 36,y = 130 )
month_of_birth_entrytext = Entry(root,bg = "#9096e6",fg ="white",borderwidth = 3)
month_of_birth_entrytext.place(x = 100,y=130)

year_of_birth = Label(root,text = "Year :")
year_of_birth.place(x = 48,y = 160)
year_of_birth_entrytext = Entry(root,bg = "#9096e6",fg ="white",borderwidth = 3)
year_of_birth_entrytext.place(x = 100,y=160)

given_date = Label(root,text = "Given Date")
given_date.place(x = 530,y = 70)

given_day = Label(root,text = "Given Day :")
given_day.place(x = 500,y = 100 )
given_day_entrytext = Entry(root,bg = "#9096e6",fg ="white",borderwidth = 3)
given_day_entrytext.place(x = 580,y=100)

given_month = Label(root,text = "Given Month :")
given_month.place(x = 485 ,y = 130 )
given_month_entrytext = Entry(root,bg = "#9096e6",fg ="white",borderwidth = 3)
given_month_entrytext.place(x = 580,y=130)

given_year = Label(root,text = "Given Year :")
given_year.place(x = 495 ,y = 160)
given_year_entrytext = Entry(root,bg = "#9096e6",fg ="white",borderwidth = 3)
given_year_entrytext.place(x = 580,y = 160)

Result = Button(root,command = CalculateAge ,text = "Resultant Age")
Result.place(x = 350  ,y = 240 )

result_year = Label(root,text = "Year :")
result_year.place(x = 315 ,y = 270)
result_year_entrytext = Entry(root,bg = "#9096e6",fg ="white",borderwidth = 3)
result_year_entrytext.place(x = 370,y=270)

result_day = Label(root,text = "Day :")
result_day.place(x = 320 ,y = 300)
result_day_entrytext = Entry(root,bg = "#9096e6",fg ="white",borderwidth = 3)
result_day_entrytext.place(x = 370,y=300)

result_month = Label(root,text = "Month :")
result_month.place(x = 305,y = 330 )
result_month_entrytext = Entry(root,bg = "#9096e6",fg ="white",borderwidth = 3)
result_month_entrytext.place(x = 370,y=330)

root.mainloop()