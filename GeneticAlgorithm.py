#Genetic algorithm for finding solution to N-Queens problem
import random

#Assuming population >= 3
def getNextGeneration(population, fitnessFunction):
    P = len(population)
    newGen = []
    for _ in range(P):
        currentChoices = random.sample(population, 3)
        currentChoices.sort(key=fitnessFunction)
        Dad = currentChoices[1]
        Mom = currentChoices[0] #hmm
        MomSize = len(Mom)
        crossoverLoc = random.randint(1, MomSize - 2)
        Baby = Dad[:crossoverLoc] + Mom[crossoverLoc:]
        for index in range(MomSize):
            if random.randint(1, MomSize) == 1:
                Baby[index] = random.randint(1, MomSize)
        newGen.append(Baby)
    return newGen

def NQueensFitness(queens):
    fitness = 0
    n = len(queens)
    for index in range(len(queens)):
        currentQueenPos = (queens[index] - 1) * n + index
        for otherIndex in range(index + 1, len(queens)):
            otherQueenPos = (queens[otherIndex] - 1) * n + otherIndex
            if otherQueenPos % n == currentQueenPos % n:
                fitness += 1
            elif otherQueenPos // n == currentQueenPos // n:
                fitness += 1
            elif otherQueenPos % (n + 1) == currentQueenPos % (n + 1):
                if otherQueenPos < currentQueenPos and otherIndex > index:
                    continue
                elif currentQueenPos < otherQueenPos and index > otherIndex:
                    continue
                fitness += 1
            elif otherQueenPos % (n - 1) == currentQueenPos % (n - 1):
                if otherQueenPos < currentQueenPos and otherIndex < index:
                    continue
                elif currentQueenPos < otherQueenPos and index < otherIndex:
                    continue
                fitness += 1
    return fitness

def printNQueens(queens):
    outPutString = ''
    columns = len(queens)
    totalSquares = columns**2
    queenPosis = set()
    for index in range(len(queens)):
        queenPosis.add((queens[index] - 1) * columns + index)
    for num in range(totalSquares):
        if num in queenPosis:
            outPutString += 'Q|'
        else:
            outPutString += '_|'
        if (num + 1) % columns == 0:
            outPutString += '\n'
    print(outPutString)

def getFirstGen(P, n):
    firstGen = []
    for _ in range(P):
        firstGen.append(random.choices(range(1, n + 1), k=n))
    return firstGen

if __name__ == '__main__':
    exampleFirstGen = getFirstGen(10, 8)
    #print(exampleFirstGen)
    nextGen = exampleFirstGen
    sols = []
    for iteration in range(200000):
        nextGen = getNextGeneration(nextGen, NQueensFitness)
        for gen in nextGen:
            if NQueensFitness(gen) <= 0:
                sols.append(gen)
        if len(sols) != 0:
            print(iteration)
            break
        
    EightQueensSol = [5, 3, 1, 7, 2, 8, 6, 4]
    nextGen.sort(key=NQueensFitness)
    print([NQueensFitness(queens) for queens in nextGen])
    printNQueens(nextGen[0])
