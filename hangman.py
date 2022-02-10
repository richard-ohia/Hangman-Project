from random import randrange
from tkinter.font import ITALIC
import words
from tkinter import *
import pygame
class Hangman:
    def __init__(self):
        self.window = Tk()
        pygame.mixer.init()
        self.word_list = list()
        self.ingame_word = list()
        self.checkSpace()
        self.buttons = []
        self.lives = 6 #This is for each body part of the hangman
        self.musicOn = False
        self.photo_image = PhotoImage()
        self.music_button = Button()
        self.canvas = Canvas()
        self.label1 = Label()
        self.label2 = Label()
        self.button = Button()
        self.button2 = Button()
        self.button3 = Button()
        self.button4 = Button()
        
        self.window.title("Hangman")
        self.window.geometry("900x700") #widthxheight
        self.window.config(bg="#323231")
        header = Label(self.window, text="H_NGM_N", bg="#323231", fg="#C1436D", font=("Helvetica",70,ITALIC))
        header.place(relx=.48,rely=.1,anchor=CENTER)
        

    def checkSpace(self):
        index = 0
        for i in self.word_list:
            if i == " ":
                self.ingame_word[index] = " "
            elif i == "'":
                self.ingame_word[index] = "'"
            index += 1


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

        self.gameWindow()

        try:
            self.display(self.lives)
            self.music_button = Button(self.window, text = "Play Music", fg="Black", highlightbackground="#323231", highlightthickness=0, width=5, height=1, command= lambda : self.playMusic())
            self.music_button.place(relx=.2,rely=.5,anchor=S)

            self.canvas = Canvas(self.window, bg="#323231", highlightthickness=0)
            self.canvas.place(relx=.42,rely=.97,anchor=S)
            for i in range(65,91):
                n = chr(i)
                n_button = Button(self.canvas, text=n, fg="Black", highlightbackground="#323231", width=4, height=1, command= lambda i=i, n=n: self.play(i - 65, n))
                if i < 72:
                    n_button.grid(padx=2,pady=2,row=i//9, column=i%9 - 1,)  
                elif i == 90:
                    n_button.grid(padx=2,pady=2,row=i//9, column=4)
                else:
                    n_button.grid(padx=2,pady=2,row=i//9, column=i%9)
                self.buttons.append(n_button)
        except:
            pass


    def play(self,index, user_input):
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


    def disable(self,index):
        self.buttons[index].config(state="disabled")


    def trueAnswer(self):
        self.label1 = Label(self.window, text=" ".join(self.word_list), bg="#323231",fg="#C1436D",font=("Arial",20))
        self.label1.place(relx=.65,rely=.5,x=900/2 - 250,anchor=CENTER)


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


    def restart(self):
        if self.musicOn == True:
            self.stopMusic()
        self.window.destroy()
        game = Hangman()
        game.main()


    def endGame(self):
        if self.musicOn == True:
            self.stopMusic()
        self.window.destroy()


    def playMusic(self):
        songs = ["chillday.mp3", "betterdays.mp3", "blushes.mp3" ,"dream.mp3"]
        rand = randrange(4)
        self.music_button.destroy()
        pygame.mixer.music.load(songs[rand])
        pygame.mixer.music.play()
        self.musicOn = True

        self.music_button = Button(self.window, text = "Stop Music", fg="Black", highlightbackground="#323231", highlightthickness=0, width=5, height=1, command= lambda : self.stopMusic())
        self.music_button.place(relx=.2,rely=.5,anchor=S)


    def stopMusic(self):
        self.music_button.destroy()
        pygame.mixer.music.stop()
        self.musicOn = False

        self.music_button = Button(self.window, text = "Play Music", fg="Black", highlightbackground="#323231", highlightthickness=0, width=5, height=1, command= lambda : self.playMusic())
        self.music_button.place(relx=.2,rely=.5,anchor=S)


    def display(self,lives):
        stages = ["hangman6.png", "hangman5.png", "hangman4.png", "hangman3.png",
        "hangman2.png", "hangman1.png", "hangman0.png"]
        
        self.label1.destroy()
        self.label1 = Label(self.window, text=" ".join(self.ingame_word), bg="#323231",fg="#C1436D",font=("Arial",20))
        self.label1.place(relx=.65,rely=.5,x=900/2 - 250,anchor=CENTER)
        
        self.photo_image = PhotoImage(file=stages[lives]).zoom(2, 2)
        self.label2 = Label(self.window, bg="#323231",image=self.photo_image)
        self.label2.place(relx=.5,rely=.78,anchor=S)


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
            n_button = Button(self.canvas, text=n, fg="Black", highlightbackground="#323231", width=4, height=1, command= lambda i=i, n=n: self.play(i - 65, n))
            if i < 72:
                n_button.grid(padx=2,pady=2,row=i//9, column=i%9 - 1,)  
            elif i == 90:
                n_button.grid(padx=2,pady=2,row=i//9, column=4)
            else:
                n_button.grid(padx=2,pady=2,row=i//9, column=i%9)
            self.buttons.append(n_button)
        self.window.mainloop()


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


    def main(self): 
        self.gameChoice()
        self.window.mainloop()


game = Hangman()
game.main()