from Ball import Ball
from Brain import brain
import random

#should create a popilation of given size
def createPop(canvas,x,y, size):
    balls = []
    #create balls and add them to array
    for i in range(size):
        ball = Ball(canvas,"black", x, y)
        balls.append(ball)
    return balls

#finds the highest fitness ball of a generation
def findGenChamp(balls, fx,fy):
        genChamp = None
        for curr in balls:
            if genChamp == None:
                genChamp = curr
            if(curr.findFitness(fx,fy) > genChamp.fitness):
                genChamp = curr
        
        #makes it easier to find best dot
        print(genChamp.fitness, "id: ", genChamp.id, " Steps taken", genChamp.moveNum) 
        return genChamp

#converts all fitness scores into an array and randomly selects a parent for new generation
def findParent(balls, champ):
    parentGroup = []

    #check if any have gotten to end and if they have only accept that
    if champ.fitness > 1:
        for i in balls:
            if i.fitness > 1:
                #fill in the spots of the array
                spots = int((i.fitness -1)*1000)
                for j in range(spots):
                    parentGroup.append(i)
    else:
        for i in balls:
            spots = int(i.fitness*1000)
            for j in range(spots):
                parentGroup.append(i)

    #pick a random parent from the list
    randy = random.randint(0, len(parentGroup)-1)

    return parentGroup[randy]
            
            
#makes a new generation of babies from selected parent then randomly mutates thier brain
def makeBabies( champ, balls, canvas, x, y):
    newBalls = []

    #keep the champion from last in new generation
    #makes sure a generation never gets worse
    newBrain = brain(champ.brain.size)
    newBrain.copy(champ.brain.moves)
    champcpy = Ball(canvas,"blue", x, y)  
    champcpy.brain = newBrain 
   

    #deletes previous generation
    for i in balls:
            canvas.delete(i.id)

    for i in range(99):
        parent = findParent(balls, champ)
        newBrain = brain(champ.brain.size)
        #makes copy of parents brain
        newBrain.copy(parent.brain.moves)
        #randomly mutates the brain
        newBrain.mutate()
        ball = Ball(canvas,"black", x, y)
        ball.brain = newBrain

        newBalls.append(ball)
    #puts champion in 
    newBalls.append(champcpy)
    canvas.tag_raise(champcpy.id)

    #return new generation
    return newBalls