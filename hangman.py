"""
Author: Richard Ohia
Hangman Project - game interface
This program implements a Hangman game using the python programming language, Tkinter and Pygame
"""
from random import randrange
from tkinter.font import BOLD, ITALIC
import words
from tkinter import *
import pygame
class Hangman:
    def __init__(self):
        #Initializes variables that will be updated throughout the program 
        self.window = Tk()
        pygame.mixer.init()
        self.word_list = list()
        self.ingame_word = list()
        self.buttons = []
        self.lives = 6 #This is for each body part of the hangman
        self.musicOn = False
        self.photo_image = PhotoImage()
        self.music_button = Button()
        self.canvas = Canvas()
        self.label1 = Label()
        self.label2 = Label()
        
        #These buttons are for the pick a theme interface of the program
        self.button = Button()
        self.button2 = Button()
        self.button3 = Button()
        self.button4 = Button()
        
        #Header and Title
        self.window.title("Hangman")
        self.window.geometry("900x700") #widthxheight
        self.window.config(bg="#323231")
        header = Label(self.window, text="H_NGM_N", bg="#323231", fg="#C1436D", font=("Helvetica",70,ITALIC,BOLD))
        header.place(relx=.48,rely=.1,anchor=CENTER)
        
    """
    This method checks if the word chosen by the program has a space or an apostrophe on it.
    If it does, we add the space or apostrophe to the position that it is supposed to appear on the puzzle.
    """
    def checkSpace(self):
        index = 0
        for i in self.word_list:
            if i == " ":
                self.ingame_word[index] = " "
            elif i == "'":
                self.ingame_word[index] = "'"
            index += 1

    """
    After the user chooses their theme, we call on words program which returns us a word.
    Sets the game word, calls the checkSpace and gameWindow methods
    """
    def gameWord(self, choice):
        if choice == "Random Words":
            self.word_list = list(words.game_word("words.txt"))
        elif choice == "US Largest Cities":
            self.word_list = list(words.game_word("cities.txt"))
        elif choice == "Countries":
            self.word_list = list(words.game_word("countries.txt"))
        elif choice == "US States":
            self.word_list = list(words.game_word("states.txt"))
        self.ingame_word = list("_" * len(self.word_list))
        self.checkSpace()
        self.gameWindow()

    """
    This method checks the user input against the actual word.
    Also calls on the disable, display and gameWon methods, 
    updates the game word and the hangman lives, and checks if the game is over.
    """
    def checkWord(self,index, user_input):
        self.disable(index)
        if(user_input in self.word_list and len(user_input) == 1):
            count = 0
            for i in self.word_list:
                if i == user_input:
                    self.ingame_word[count] = user_input
                count += 1
            if("_" not in self.ingame_word):
                self.display(self.lives)
                self.gameWon(True)
            else:
                self.display(self.lives)
        elif(user_input not in self.word_list and len(user_input) == 1):
            self.lives -= 1
            self.display(self.lives)
        if self.lives <= 0:
            self.gameWon(False)

    """
    Disables the button last clicked on by the user.
    """
    def disable(self,index):
        self.buttons[index].config(state="disabled")

    """
    Displays the word chosen by our program.
    """
    def trueAnswer(self):
        self.label1 = Label(self.window, text=" ".join(self.word_list), bg="#323231",fg="#C1436D",font=("Arial",20))
        self.label1.place(relx=.65,rely=.5,x=900/2 - 250,anchor=CENTER)

    """
    This method controls what the user sees after they are done playing a game.
    """
    def gameWon(self, gameFinished):
        self.canvas.destroy()
        self.label2.destroy()
        self.label1.destroy()
        self.trueAnswer()
        canvas = Canvas(self.window, bg="#323231", highlightthickness=0)
        canvas.place(relx=.5,rely=.6,anchor=S)
        if gameFinished == True:
            label = Label(canvas, text="🥳", bg="#323231",fg="#C1436D",font=("Arial",200))
        else:
            label = Label(canvas, text="🥲", bg="#323231",fg="#C1436D",font=("Arial",200))
        label.pack()
        button = Button(canvas, text = "Play Again", fg="Black", highlightbackground="#323231", highlightthickness=0, width=10, height=2, command= lambda : self.restart())
        button2 = Button(canvas, text = "End Game", fg="Black", highlightbackground="#323231", highlightthickness=0, width=10, height=2, command= lambda : self.endGame())
        button.pack()
        button2.pack()

    """
    Closes the current window and starts a new one.
    """
    def restart(self):
        if self.musicOn == True: #Checking to see if the user was playing music
            self.stopMusic()
        self.window.destroy()
        game = Hangman()
        game.main()

    """
    Closes the current window
    """
    def endGame(self):
        if self.musicOn == True: #Checking to see if the user was playing music
            self.stopMusic()
        self.window.destroy()

    """
    When the user clicks play music, this method chooses a random song from the four choices.
    Deletes the play music button and replaces it with the stop music button.
    """
    def playMusic(self):
        songs = ["chillday.mp3", "betterdays.mp3", "blushes.mp3" ,"dream.mp3"]
        rand = randrange(4)
        self.music_button.destroy()
        pygame.mixer.music.load(songs[rand])
        pygame.mixer.music.play()
        self.musicOn = True

        self.music_button = Button(self.window, text = "Stop Music", fg="Black", highlightbackground="#323231", highlightthickness=0, width=5, height=1, command= lambda : self.stopMusic())
        self.music_button.place(relx=.2,rely=.5,anchor=S)

    """
    When the user clicks stop music, or the program is asked to restart 
    or stop the game while music was playing, this method stops the music.
    Deletes the stop music button and replaces it with the play music button.
    """
    def stopMusic(self):
        self.music_button.destroy()
        pygame.mixer.music.stop()
        self.musicOn = False

        self.music_button = Button(self.window, text = "Play Music", fg="Black", highlightbackground="#323231", highlightthickness=0, width=5, height=1, command= lambda : self.playMusic())
        self.music_button.place(relx=.2,rely=.5,anchor=S)

    """
    Updates the image of the hangman and its current life status.
    """
    def display(self,lives):
        stages = ["hangman6.png", "hangman5.png", "hangman4.png", "hangman3.png",
        "hangman2.png", "hangman1.png", "hangman0.png"]
        
        self.label1.destroy()
        self.label1 = Label(self.window, text=" ".join(self.ingame_word), bg="#323231",fg="#C1436D",font=("Arial",20))
        self.label1.place(relx=.65,rely=.5,x=900/2 - 250,anchor=CENTER)
        
        self.photo_image = PhotoImage(file=stages[lives]).zoom(2, 2)
        self.label2 = Label(self.window, bg="#323231",image=self.photo_image)
        self.label2.place(relx=.5,rely=.78,anchor=S)


    """
    After the word is choosen and set, this method changes what the user sees,
    from pick a theme, the user now sees the hangman image and the letter buttons.
    """
    def gameWindow(self):
        self.canvas.destroy()
        self.label2.destroy()
        self.button.destroy()
        self.button2.destroy()
        self.button3.destroy()
        self.button4.destroy()
        self.display(self.lives)

        self.canvas = Canvas(self.window, bg="#323231", highlightthickness=0)
        self.canvas.place(relx=.42,rely=.97,anchor=S)
        for i in range(65,91):
            n = chr(i)
            n_button = Button(self.canvas, text=n, fg="Black", highlightbackground="#323231", width=4, height=1, command= lambda i=i, n=n: self.checkWord(i - 65, n))
            if i < 72:
                n_button.grid(padx=2,pady=2,row=i//9, column=i%9 - 1,)  
            elif i == 90:
                n_button.grid(padx=2,pady=2,row=i//9, column=4)
            else:
                n_button.grid(padx=2,pady=2,row=i//9, column=i%9)
            self.buttons.append(n_button)
        self.window.mainloop()

    """
    This method controls the face interace the user sees. 
    Which looks to see which theme, the user wants.
    """
    def gameChoice(self):
        self.music_button = Button(self.window, text = "Play Music", fg="Black", highlightbackground="#323231", highlightthickness=0, width=5, height=1, command= lambda : self.playMusic())
        self.music_button.place(relx=.2,rely=.5,anchor=S)
        
        self.canvas = Canvas(self.window, bg="#323231", highlightthickness=0)
        self.canvas.place(relx=.45,rely=.6,anchor=S)
        
        self.label2 = Label(self.canvas, text="Pick a theme", bg="#323231",fg="#C1436D",font=("Arial",35))
        self.label2.place(relx=.2,rely=.2)

        self.button = Button(self.canvas, text = "Random Words", fg="Black", highlightbackground="#323231", highlightthickness=0, width=10, height=2, command= lambda : self.gameWord("Random Words"))
        self.button.place(relx=.58,rely=.5)
        self.button2 = Button(self.canvas, text = "US States", fg="Black", highlightbackground="#323231", highlightthickness=0, width=10, height=2, command= lambda : self.gameWord("US States"))
        self.button2.place(relx=.58,rely=.7)
        self.button4 = Button(self.canvas, text = "US Largest Cities", fg="Black", highlightbackground="#323231", highlightthickness=0, width=10, height=2, command= lambda : self.gameWord("US Largest Cities"))
        self.button4.place(relx=.1,rely=.5)
        self.button3 = Button(self.canvas, text = "Countries", fg="Black", highlightbackground="#323231", highlightthickness=0, width=10, height=2, command= lambda : self.gameWord("Countries"))
        self.button3.place(relx=.1,rely=.7)

    """
    This is the beautiful main method. 
    Starts the general interface of the game.
    """
    def main(self): 
        self.gameChoice()
        self.window.mainloop()


game = Hangman() #Hangman object
game.main()