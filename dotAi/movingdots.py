from tkinter import *
import math
import keyboard
from Ball import Ball
from population import *
import random

#function to check if all the balls of a generation are dead
def allDead(b):
    for i in b:
        if (i.isDead == False):
            return False
    return True

def main():
    #change the starting postion of the dots
    x = 500
    y = 550

    #change where the finsih is
    fx = 500
    fy = 90
    
    master = Tk()

    #current generation counter
    gen = IntVar(value = 0)

    #creates canvas
    w = Canvas(master, width = 1000, height = 600)
    master.title("Ball AI")

    #puts keyboard focus on canvas
    w.bind("<1>", lambda event: w.focus_set())

    # creates finish ball
    w.create_oval(fx -10,fy- 10, fx+10 ,fy+10, fill = "red")
    w.create_line(400,300, 600, 300)
    
    #creates the initial population
    balls = createPop(w,x,y, 100)

    #creates generation label
    label1 = Label(master, text = "generation: ")
    label1.place(x=10, y=10, anchor='nw')

    label = Label(master, textvariable = gen)
    label.place(x=80, y=10, anchor='nw')

    w.pack()


    while 1:
        #check if all beds are dead
        if (allDead(balls) == False):
            for i in balls:
                #move all the balls
                i.update(fx,fy)
            master.update()

        #what runs when they all die
        else:
            #prints out fitness of current champion
            print("")
            print("Fitness of Champion in Gen ", gen.get())

            # gets the best of the geration
            genChamp = findGenChamp(balls,fx,fy)

            #create next generation
            balls = makeBabies(genChamp, balls, w, x, y)

            #updates the gen value
            gen.set(value = gen.get()+1)

            
    w.mainloop()


#runs the program
main()