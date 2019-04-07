import random


#the brains of the balls
class brain:
    def __init__(self,size):
        self.size = size
        self.moves = []
        self.randomize(self.moves)

    #creates a random brain
    def randomize(self, moves):
        for i in range(self.size):
            rand = random.randint(1,4)
            moves.append(rand)

    #mutates brain
    def mutate(self):
        #the % to mutate the brainn
        mutationRate = 5
        for i in range(len(self.moves)):
            randy = random.randint(0,101)
            if randy < mutationRate:
                newMove = random.randint(1,4)
                self.moves[i] = newMove

    #copies the brain given
    def copy(self, oldmoves):
        self.moves = oldmoves.copy()
       
