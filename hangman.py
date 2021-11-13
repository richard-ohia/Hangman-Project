import words
from tkinter import *

window = Tk()
word_list = list(words.game_word())
finished = False #Keeps track of when game is completed
ingame_word = list("_" * len(word_list))
guessed_letters = set()
buttons = []

def play(index, user_input):
    lives = 6 #This is for each body part of the hangman Please choose a letter:
    disable(index - 65, user_input) 
    print(word_list)
    print(ingame_word)
    if(user_input in guessed_letters):
        print("\nYou guessed this letter already. Try again!")
        label1 = Label(window, text=" ".join(ingame_word), fg="#371BB1",font=("Arial",20))
        label1.place(relx=.6,rely=.5,x=900/2 - 250,anchor=CENTER)
    elif(user_input in word_list and len(user_input) == 1):
        print("\nNice " + '"' + user_input + '"' + " is part of the word.")
        guessed_letters.add(user_input)
        indices = [i for i, value in enumerate(word_list) if value == user_input] ## Wtf is this
        for index in indices:
            ingame_word[index] = user_input
        if("_" not in ingame_word):
            finished = True
            print("\nYou Won! The word was " + "".join(ingame_word) + ".")
        else:
            print(display(lives))
            label1 = Label(window, text=" ".join(ingame_word), fg="#371BB1",font=("Arial",20))
            label1.place(relx=.6,rely=.5,x=900/2 - 250,anchor=CENTER)
    elif(user_input not in word_list and len(user_input) == 1):
        print('\n"' + user_input + '"' + " is not part of the word.")
        guessed_letters.add(user_input)
        lives -= 1
        print(display(lives))
        label1 = Label(window, text=" ".join(ingame_word), fg="#371BB1",font=("Arial",20))
        label1.place(relx=.6,rely=.5,x=900/2 - 250,anchor=CENTER)
        print("\nYou have " + str(lives) + " lives.")
    else:
        print("\nPlease input one letter. Try again!")

def disable(index, n):
    print(n)
    buttons[index].config(state="disabled")


def display(lives):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |    
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |    
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |    
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |    
                   -
                """
    ]
    return stages[lives]

def main():
    window.title("Hangman")
    window.geometry("900x700") #widthxheight
    header = Label(window, text="Hangman", fg="#371BB1",font=("Arial",20))
    header.place(relx=.6,rely=.1,anchor=CENTER)
    
    photo_image = PhotoImage(file="hangman0.png")
    larger_image = photo_image.zoom(2, 2)
    label2 = Label(window, image=larger_image)
    label2.place(relx=.5,rely=.8,anchor=S)
   
    canvas = Canvas(window)
    canvas.place(relx=.42,rely=.97,anchor=S)
    for i in range(65,91):
        n = chr(i)
        if i < 72:
            n_button = Button(canvas, fg="Black", text=n, width = 4, height = 1,command= lambda i=i, n=n: play(i, n))
            n_button.grid(padx=2,pady=2,row=i//9, column=i%9 - 1)  
        elif i == 90:
            n_button = Button(canvas, fg="Black", text=n, width = 4, height = 1,command= lambda i=i, n=n: play(i, n))
            n_button.grid(padx=2,pady=2,row=i//9, column=4)
        else:
            n_button = Button(canvas, fg="Black", text=n, width = 4, height = 1,command= lambda i=i, n=n: play(i, n))
            n_button.grid(padx=2,pady=2,row=i//9, column=i%9)
        buttons.append(n_button)
   

    label1 = Label(window, text=" ".join(ingame_word), fg="#371BB1",font=("Arial",20))
    label1.place(relx=.6,rely=.5,x=900/2 - 250,anchor=CENTER)
    window.mainloop()


main()