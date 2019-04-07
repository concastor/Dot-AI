from tkinter import *
from Brain import brain
import math

#the balls that will be modified
class Ball:
    def __init__(self, canvas, colour, x, y):
        self.brain = brain(1000)
        self.x = x
        self.y = y
        self.moveNum = 0
        self.moves = 0
        self.finishedIndex = self.brain.size
        self.isDead = False
        self.finished = False
        self.canvas = canvas
        self.id = canvas.create_oval(x-5, y-5, x+5, y+5, fill=colour)
        self.fitness = 0.0

    #updates all the stats related to the ball
    def update(self, fx, fy):
        #check if its dead before doing anything
        if (self.isDead == False):
            #moves balls
            self.isDead = self.move()
            #check if its dead after it moved
            if self.isDead == False:
                #check if ball is within bounds
                if (self.x < 5 or self.x > 995 or self.y < 5 or self.y > 595):
                    self.isDead = True
                else:
                    self.isDead = self.finish(fx,fy)
            
            #increase number of moves taken
            self.moves += 1

    #finds distance to the finish
    def distance(self, fx, fy):
        #first time ive had a use for pythagorem theorem
        a = self.x - fx
        b = self.y - fy
        c = (a*a) + (b*b)
        c = math.sqrt(c)
        return c

    #check if it collides with 
    def finish(self, fx, fy):
        d = self.distance(fx,fy)
        if d <= 15:
            self.finished = True
            self.finishedIndex = self.moveNum
            return True
        else:
            return False

    #moves the dot depending on the brain
    def move(self):
        if self.y == 300:
            if self.x < 600 and self.x > 400:
                self.isDead = True
                return True


        #check if dot is out of moves
        if (self.moveNum >= self.brain.size):
            self.isDead == True
            return True

        #move left
        if(self.brain.moves[self.moveNum] == 1):
            self.canvas.move(self.id, -5, 0)
            self.x -= 5
        #move up
        elif(self.brain.moves[self.moveNum] == 2):
            self.canvas.move(self.id, 0, -5)
            self.y -= 5
        #move right
        elif(self.brain.moves[self.moveNum]== 3):
            self.canvas.move(self.id, 5, 0)
            self.x += 5
        #move down
        elif(self.brain.moves[self.moveNum] == 4):
              self.canvas.move(self.id, 0, 5)
              self.y += 5

        self.moveNum += 1
        return False

    #finds the fitness of the balls to determine what the next generation will look like
    def findFitness(self, fx,fy):
        self.fitness = 0.0
        #score if dot finished
        if (self.finished):
            self.fitness += 1
            self.fitness += 1.0/self.moves
        else:
            #score if dot doesent finish 
            d = self.distance(fx,fy)
            self.fitness = (1.0/((self.distance(fx,fy)*2)))

        return self.fitness

        
        
        