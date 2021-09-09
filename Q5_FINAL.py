from tkinter import *
import random

#dict
RPS_dict = {"rock":{"rock":1, "paper":0, "scissor":2}, "paper":{"rock":2, "paper":1, "scissor":0}, "scissor":{"rock":0, "paper":2, "scissor":1}}
c_score = 0
p_score = 0

#outcome functions
def outcome_handler(user_choice):
    global c_score
    global p_score
    choices = ["rock","paper","scissor"]
    random_num = random.randint(0,2)
    computer_choice = choices[random_num]
    result= RPS_dict[user_choice][computer_choice]

    player_choice.config(fg = "red",text = "Player Choice: "+str(user_choice))
    comp_choice.config(fg = "green",text = "Computer Choice: "+str(computer_choice))

    if  result == 2:
        p_score = p_score + 2
        player_score.config(text = "Player: "+str(p_score))
        outcome.config(fg="blue",text = "Outcome : Player won ")
    elif result == 1:
        p_score = p_score + 1
        c_score = c_score + 1
        player_score.config(text = "Player: "+str(p_score))
        comp_score.config(text="Computer: " + str(c_score))
        outcome.config(fg="blue",text = "Outcome : Draw")
    elif result == 0:
        c_score = c_score + 2
        comp_score.config(text="Computer: " + str(c_score))
        outcome.config(fg="blue", text="Outcome : Computer won")


#main window
root = Tk()
root.title("Rock Paper Scissors")
root.geometry("700x400")

#title
Rock_paper_scissor = Label(root,text = "ROCK PAPER SCISSORS",foreground = "#af0000")
Rock_paper_scissor["font"] = ("Century Gothic",30,"bold","underline")
Rock_paper_scissor.pack()

#start game
start_game = Label(root,text = "Lets Start the Game....",foreground = "green")
start_game["font"] = ("Al Bayan",15,"bold italic")
start_game.pack()

#your options
options = Label(root,text = "Your options : ",foreground = "#8b0a50")
options["font"] = ("Al Bayan",15,"underline")
options.place(x = 70,y = 100)

#player score
player_score = Label(root,text = "Player = 0",fg = "red")
player_score["font"] = ("Al Bayan",15)
player_score.place(x= 420,y =260)

#computer score
comp_score = Label(root,text = "Computer = 0",fg = "green")
comp_score["font"] = ("Al Bayan",15)
comp_score.place(x = 420 ,y = 310)

#player choice
player_choice = Label(root,text = "Player Choice: ",fg = "green")
player_choice["font"] = ("Al Bayan",15)
player_choice.place(x = 190 , y = 260)

#computer choice
comp_choice = Label(root,text = "Computer Choice: ",fg = "red")
comp_choice["font"] = ("Al Bayan",15)
comp_choice.place(x =190 , y = 310)

#outcome
outcome = Label(root)
outcome["font"] = ("Al Bayan",15)
outcome.place(x= 300 ,y = 350)

Button(root,text = "Rock",height = 5, width = 15,highlightbackground ="#bcceac",command=lambda:outcome_handler("rock")).place(x = 150 ,y = 150 )
Button(root,text = "Paper",height = 5, width = 15,highlightbackground ="#8acae7",command=lambda:outcome_handler("paper")).place(x = 310 ,y = 150 )
Button(root,text = "Scissor",height = 5, width = 15,highlightbackground ="#e5d7db",command=lambda:outcome_handler("scissor")).place(x = 470 ,y = 150 )

root.mainloop()