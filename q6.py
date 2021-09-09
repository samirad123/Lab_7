from tkinter import *

root=Tk()
root.title('Calculator')
root.configure(background="#d6d2d2")
root.geometry('500x500')
result = " "
equation = StringVar()

def press(num):
    global result
    result= result + str(num)
    equation.set(result)



def equal():
    global result

    total = str(eval(result))
    equation.set(total)
    result= " "

def clear():
    calculate.delete(first=0, last=200)


lb1 = Label(root,width=20,text='CALCULATOR',fg ='#649cff',bg="#d6d2d2",font=('Al Bayan',20,'bold'))
lb1.place(x=100,y=50)

calculate = Entry(root, width=30, text=equation, fg ="#df283a",borderwidth = 3, font=('Al Bayan', 17, 'bold'))
calculate.place(x=60, y=100)

b_1= Button(root, width=5, command=lambda: press('1'), text='1', font=('Al Bayan', 18, 'bold'))
b_1.place(x=100, y=150)

b_2= Button(root, width=5, text='2', command=lambda: press('2'), font=('Al Bayan', 18, 'bold'))
b_2.place(x=175, y=150)

b_3= Button(root, width=5, text='3', command=lambda: press('3'), font=('Al Bayan', 18, 'bold'))
b_3.place(x=250, y=150)

b_4= Button(root, width=5, text='4', command=lambda: press('4'), font=('Al Bayan', 18, 'bold'))
b_4.place(x=100, y=200)

b_5= Button(root, width=5, text='5', command=lambda: press('5'), font=('Al Bayan', 18, 'bold'))
b_5.place(x=175, y=200)

b_6= Button(root, width=5, text='6', command=lambda: press('6'), font=('Al Bayan', 18, 'bold'))
b_6.place(x=250, y=200)

b_7= Button(root, width=5, text='7', command=lambda: press('7'), font=('Al Bayan', 18, 'bold'))
b_7.place(x=100, y=250)

b_8= Button(root, width=5, text='8', command=lambda: press('8'), font=('Al Bayan', 18, 'bold'))
b_8.place(x=175, y=250)

b_9= Button(root, width=5, text='9', command=lambda: press('9'), font=('Al Bayan', 18, 'bold'))
b_9.place(x=250, y=250)

b_0= Button(root, width=5, text='0', command=lambda: press('0'), font=('Al Bayan', 18, 'bold'))
b_0.place(x=175, y=300)

b_clear= Button(root, width=5, text='c', command=clear, font=('Al Bayan', 18, 'bold'))
b_clear.place(x=100, y=300)

b_equal= Button(root, width=5, text='=', command=equal, font=('Al Bayan', 18, 'bold'))
b_equal.place(x=250, y=300)

b_add= Button(root, width=5, text='+', command=lambda: press('+'), font=('Al Bayan', 18, 'bold'))
b_add.place(x=325, y=150)

b_minus= Button(root, width=5, text='-', command=lambda: press('-'), font=('Al Bayan', 18, 'bold'))
b_minus.place(x=325, y=200)

b_multipy= Button(root, width=5, text='*', command=lambda: press('*'), font=('Al Bayan', 18, 'bold'))
b_multipy.place(x=325, y=300)

b_divide= Button(root, width=5, text='/', command=lambda: press('/'), font=('Al Bayan', 18, 'bold'))
b_divide.place(x=325, y=250)

root.mainloop()
