from tkinter import *
from PIL import Image,ImageTk
import random
root = Tk()

# pictures
rock_img = (Image.open("/Users/samiradeepak/Downloads/rock1.png"))
paper_img = (Image.open("/Users/samiradeepak/Downloads/paper1.png"))
scissor_img = (Image.open("/Users/samiradeepak/Downloads/scissor1.png"))
rock_img_comp = (Image.open("/Users/samiradeepak/Downloads/rock1.png"))
paper_img_comp = (Image.open("/Users/samiradeepak/Downloads/paper1.png"))
scissor_img_comp = (Image.open("/Users/samiradeepak/Downloads/scissor1.png"))


# messages
msg = Label(root)
msg.place(x = 330, y = 460)

#update message
def updateMessage(x):
    msg['text'] = x

# update user score
def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)


# update computer score
def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)


# check winner
def checkWin(player, computer):
    if player == computer:
        updateMessage("Its a tie!!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()

    else:
        pass



#update choices
choices = ["rock", "paper", "scissor"]
#define function for user input
def updateChoice(x):
    # for computer
    compChoice = choices[random.randint(0, 2)]
    if compChoice == "rock":
        insert_comp.configure(image=rock_img_comp)
    elif compChoice == "paper":
        insert_comp.configure(image=paper_img_comp)
    else:
        insert_comp.configure(image=scissor_img_comp)
#for user
    if x == "rock":
        user_s.configure(image=rock_img)
    elif x == "paper":
        user_s.configure(image=paper_img)
    else:
        user_s.configure(image=scissor_img)
    return checkWin(x,compChoice)

#window size
root.title("Rock Paper Scissors")
root.geometry("900x500")

#title
Rock_paper_scissor = Label(root,text = "ROCK PAPER SCISSORS",foreground = "#af0000")
Rock_paper_scissor["font"] = ("Century Gothic",30,"bold","underline")
Rock_paper_scissor.pack()


#picture
canvas = Canvas(root, width = 600, height = 400)
canvas.place(x = 390 ,y = 70)
#Load an image in the script
img = (Image.open("/Users/samiradeepak/Downloads/rock paper scissors.png"))
#Resize the Image using resize method
resized_image = img.resize((100,100), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)
#Add image to the Canvas Items
canvas.create_image(10,10, anchor=NW, image=new_image)


#start game
start_game = Label(root,text = "Lets Start the Game....",foreground = "green")
start_game["font"] = ("Al Bayan",15,"bold italic")
start_game.pack()

#your options
options = Label(root,text = "Your options : ")
options.place(x = 150,y = 200)

#rock
rock = Button(root, text = "Rock", width = 10, height = 5, highlightbackground ="#bcceac",command=lambda: updateChoice("rock"))
rock.place(x = 250 ,y = 200 )

#paper
paper = Button(root,text = "Paper",width = 10,height = 5,highlightbackground = "#8acae7",
               command=lambda: updateChoice("paper"))
paper.place(x = 350 ,y =200 )

#scissors
scissors = Button(root,text = "Scissors",width = 10,height = 5,highlightbackground = "#e5d7db",
                  command=lambda: updateChoice("scissor"))
scissors.place(x = 450,y = 200)

#your selection
your_selection = Label(root,text = "Your selection : ")
your_selection.place(x = 230 ,y = 330)


#user entry
user_s = Label(root)
user_s.place(x = 490 ,y = 330 )

#your score
your_score = Label(root,text = "Your score : ")
your_score.place(x = 450 ,y = 330)
#insert score of user
playerScore = Label(root,text = 0)
playerScore.place(x=530,y=330)


#computer selection
computer_selection = Label(root,text = "Computer Selection : ")
computer_selection.place(x = 450 ,y = 360)
#insert selection of comp
insert_comp = Label(root)
insert_comp.place(x = 520,y = 360 )


#computer score
computer_score = Label(root,text = "Computer score : ")
computer_score.place(x = 230 ,y =360 )
#insert score of computer
computerScore = Label(root,text = 0)
computerScore.place(x= 340 ,y = 360)


root.mainloop()