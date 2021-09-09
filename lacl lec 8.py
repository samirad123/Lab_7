from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("Login System")


def help_func():
    print("This is help menu")


menu_example = Menu(root)

# Top Level Menu
# menu_example.add_command(label="File")
# menu_example.add_command(label="Edit")
# menu_example.add_command(label="Selection")
# menu_example.add_command(label="Find")
# menu_example.add_command(label="View")
# menu_example.add_command(label="Goto")
# menu_example.add_command(label="Help",command=help_func)

# Menu + Submenu
file_menu = Menu(menu_example)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Open Recent")
file_menu.add_command(label="Save")
file_menu.add_command(label="Save As")
file_menu.add_command(label="Exit", command=root.destroy)

menu_example.add_cascade(label="File", menu=file_menu)


def edit_copy():
    print("This has been copied")


edit_menu = Menu(menu_example)
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Copy", command=edit_copy)

menu_example.add_cascade(label="Edit", menu=edit_menu)

root.config(menu=menu_example)

login_label = Label(root, text="Login System", font=('Calibri', 30))
login_label.pack()

# Spinbox
spinbox_months = Spinbox(root, from_=1, to=12)
spinbox_months.pack()

spinbox_year = Spinbox(root, from_=1990, to=2022)
spinbox_year.pack()

# OptionMenu
list_of_programming_languages = ["Java", "Swift", "Kotlin", "Python", "Go", "C"]
temp = StringVar()
option_menu_pl = OptionMenu(root, temp, *list_of_programming_languages)
option_menu_pl.pack()
temp.set("Select a coding langauage")

# ListBox
listbox_languages = Listbox(root, height=5, width=10)
listbox_languages.pack()

listbox_languages.insert(1, "Java")
listbox_languages.insert(2, "Swift")
listbox_languages.insert(3, "Kotlin")
listbox_languages.insert(4, "Python")
listbox_languages.insert(5, "Go")
listbox_languages.insert(6, "C")

frame1 = Frame(root, bg="#bfeff8")
frame1.pack()

label_username = Label(frame1, text="Username")
label_username.grid(row=0, column=0, padx=10, pady=10)
username_entrytext = Entry(frame1)
username_entrytext.grid(row=0, column=1, padx=10, pady=10)

label_password = Label(frame1, text="Password")
label_password.grid(row=1, column=0, padx=10, pady=10)
password_entrytext = Entry(frame1, show='*')
password_entrytext.grid(row=1, column=1, padx=10, pady=10)

frame2 = Frame(root, bg="#0080ff")
frame2.pack()


def login_function():
    print("You have successfully logged in")


button_login = Button(frame2, text="Login", command=login_function)
button_login.grid(row=0, column=0, padx=10, pady=10)

button_reset = Button(frame2, text="Reset")
button_reset.grid(row=0, column=1, padx=10, pady=10)

button_exit = Button(frame2, text="Exit Window", command=root.destroy)
button_exit.grid(row=0, column=2, padx=10, pady=10)

frame3 = Frame(root, bg="#f9ce71")
frame3.pack()


def info_button():
    messagebox.showinfo("Login Status", "Login is Successful")


info_button = Button(frame3, text="Info button", command=info_button)
info_button.grid(row=0, column=0, padx=10, pady=10)


def warning_button():
    messagebox.showwarning("Beware", "You are trying to use a website which is not secure")


warning_button = Button(frame3, text="Warning button", command=warning_button)
warning_button.grid(row=0, column=1, padx=10, pady=10)


def error_button():
    messagebox.showerror("DividebyZero", "You cannot divide by zero")


error_button = Button(frame3, text="Error button", command=error_button)
error_button.grid(row=0, column=2, padx=10, pady=10)


def askquestion_button():
    messagebox.askquestion("Feedback", "Do you like Python?")


askquestion_button = Button(frame3, text="Ask Question button", command=askquestion_button)
askquestion_button.grid(row=1, column=0, padx=10, pady=10)


def askokcancel_button():
    messagebox.askokcancel("Accept T&C", "Do you agree with terms and conditions?")


askokcancel_button = Button(frame3, text="Ask OK Cancel button", command=askokcancel_button)
askokcancel_button.grid(row=1, column=1, padx=10, pady=10)


def askyesno_button():
    messagebox.askyesno("Proceed", "Do you want to proceed?")


askyesno_button = Button(frame3, text="Ask Yes No button", command=askyesno_button)
askyesno_button.grid(row=1, column=2, padx=10, pady=10)


def retry_button():
    messagebox.askretrycancel("Retry", "Page loading failed. Do you want to retry?")


retry_button = Button(frame3, text="Retry button", command=retry_button)
retry_button.grid(row=2, column=1, padx=10, pady=10)

# Image
cal_image_path = PhotoImage(file="/Users/samiradeepak/Downloads/rock paper scissors.png")
calendar_img = Label(root, image=cal_image_path)
calendar_img.pack()


# If you want to open a new window on click of a button

def openNewWindow():
    # new_window = Toplevel(root)
    # new_window.title("Second Window")
    me = Tk()
    me.geometry("354x460")
    me.title("CALCULATOR")
    melabel = Label(me, text="CALCULATOR", bg='dark gray', font=("Times", 30, 'bold'))
    melabel.pack(side=TOP)
    me.config(background='Dark gray')

    textin = StringVar()
    operator = ""

    def clickbut(number):  # lambda:clickbut(1)
        global operator
        operator = operator + str(number)
        textin.set(operator)

    def equlbut():
        global operator
        add = str(eval(operator))
        textin.set(add)
        operator = ''

    def equlbut():
        global operator
        sub = str(eval(operator))
        textin.set(sub)
        operator = ''

    def equlbut():
        global operator
        mul = str(eval(operator))
        textin.set(mul)
        operator = ''

    def equlbut():
        global operator
        div = str(eval(operator))
        textin.set(div)
        operator = ''

    def clrbut():
        textin.set('')

    metext = Entry(me, font=("Courier New", 12, 'bold'), textvar=textin, width=25, bd=5, bg='powder blue')
    metext.pack()

    but1 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(1), text="1",
                  font=("Courier New", 16, 'bold'))
    but1.place(x=10, y=100)

    but2 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(2), text="2",
                  font=("Courier New", 16, 'bold'))
    but2.place(x=10, y=170)

    but3 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(3), text="3",
                  font=("Courier New", 16, 'bold'))
    but3.place(x=10, y=240)

    but4 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(4), text="4",
                  font=("Courier New", 16, 'bold'))
    but4.place(x=75, y=100)

    but5 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(5), text="5",
                  font=("Courier New", 16, 'bold'))
    but5.place(x=75, y=170)

    but6 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(6), text="6",
                  font=("Courier New", 16, 'bold'))
    but6.place(x=75, y=240)

    but7 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(7), text="7",
                  font=("Courier New", 16, 'bold'))
    but7.place(x=140, y=100)

    but8 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(8), text="8",
                  font=("Courier New", 16, 'bold'))
    but8.place(x=140, y=170)

    but9 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(9), text="9",
                  font=("Courier New", 16, 'bold'))
    but9.place(x=140, y=240)

    but0 = Button(me, padx=14, pady=14, bd=4, bg='white', command=lambda: clickbut(0), text="0",
                  font=("Courier New", 16, 'bold'))
    but0.place(x=10, y=310)

    butdot = Button(me, padx=47, pady=14, bd=4, bg='white', command=lambda: clickbut("."), text=".",
                    font=("Courier New", 16, 'bold'))
    butdot.place(x=75, y=310)

    butpl = Button(me, padx=14, pady=14, bd=4, bg='white', text="+", command=lambda: clickbut("+"),
                   font=("Courier New", 16, 'bold'))
    butpl.place(x=205, y=100)

    butsub = Button(me, padx=14, pady=14, bd=4, bg='white', text="-", command=lambda: clickbut("-"),
                    font=("Courier New", 16, 'bold'))
    butsub.place(x=205, y=170)

    butml = Button(me, padx=14, pady=14, bd=4, bg='white', text="*", command=lambda: clickbut("*"),
                   font=("Courier New", 16, 'bold'))
    butml.place(x=205, y=240)

    butdiv = Button(me, padx=14, pady=14, bd=4, bg='white', text="/", command=lambda: clickbut("/"),
                    font=("Courier New", 16, 'bold'))
    butdiv.place(x=205, y=310)

    butclear = Button(me, padx=14, pady=119, bd=4, bg='white', text="CE", command=clrbut,
                      font=("Courier New", 16, 'bold'))
    butclear.place(x=270, y=100)

    butequal = Button(me, padx=151, pady=14, bd=4, bg='white', command=equlbut, text="=",
                      font=("Courier New", 16, 'bold'))
    butequal.place(x=10, y=380)
    me.mainloop()


button_new_window = Button(root, text="Open a new Window", command=openNewWindow)
button_new_window.pack()

root.mainloop()