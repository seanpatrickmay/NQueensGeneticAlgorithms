# Genetic algorithm for finding solution to N-Queens problem
# Assumption that population size >= 3, and all population members are of equal size.
# Heuristics will be so that higher values are worse.
import random
import sys

# Produces next generation by crossing then mutating members chosen based on fitness.
def getNextGeneration(population, fitnessFunction):
    P = len(population)
    # Simple list works, no need to get fancy
    newGen = []
    # Keeps same population size
    for _ in range(P):
        # Assuming population >= 3
        currentChoices = random.sample(population, 3) 

        # Sort the 3 chosen, and take the 2 most fit of them.
        # This is a fairly relaxed implementation of fitness selection. (I think)
        currentChoices.sort(key=fitnessFunction)
        Dad = currentChoices[1]
        Mom = currentChoices[0] # Mom's are better?

        # Cross and mutate
        Baby = crossTwoMembers(Mom, Dad)
        mutateMember(Baby)

        newGen.append(Baby)
    return newGen

# Crosses two members to create a child
def crossTwoMembers(Mom, Dad):
    # Choose crossover point, not letting it be either extreme.
    crossPoint = random.randint(1, len(Mom) - 2)
    return Dad[:crossPoint] + Mom[crossPoint:]

# Mutates each index to randint in range with chance 1/n.
# Changes original member, doesn't return.
def mutateMember(Member):
    memberSize = len(Member) #haha
    # For each part of dna strand
    for index in range(memberSize):
        # With chance 1/length
        if random.randint(1, memberSize) == 1:
            Member[index] = random.randint(1, memberSize)

# Find fitness based on # of collisions. Higher is worse.
def NQueensCollisionFitness(queens):
    fitness = 0
    n = len(queens)
    for index in range(n):
        # Convert coordinate to integer
        currentQueenPos = (queens[index] - 1) * n + index
        # Only get conflicts once by sweeping rightwards as we check
        for otherIndex in range(index + 1, n):
            otherQueenPos = (queens[otherIndex] - 1) * n + otherIndex
            # Check for columns and rows 
            #(technically columns not needed due to our representation as 1 in each column)
            if otherQueenPos % n == currentQueenPos % n:
                fitness += 1
            elif otherQueenPos // n == currentQueenPos // n:
                fitness += 1
            # Check for diagonals
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

# Prints a population member as a pretty string
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

# Function to generate first generation of size P, with bound N
def getFirstGen(P, N):
    firstGen = []
    for _ in range(P):
        firstGen.append(random.choices(range(1, N + 1), k=N))
    return firstGen

if __name__ == '__main__':
    # Handling sys input
    if len(sys.argv) == 3:
        P = int(sys.argv[1])
        N = int(sys.argv[2])
    elif len(sys.argv) == 2:
        # 200 is reasonable standard population size
        P = 200
        N = int(sys.argv[1])
    else:
        print("Please enter N, the number of queens to solve for.")
        sys.exit()

    # Create first gen, and iterate on it
    exampleFirstGen = getFirstGen(P, N)
    #print(f"First generation is: {exampleFirstGen}")
    nextGen = exampleFirstGen
    fitnessFunction = NQueensCollisionFitness
    for iteration in range(200000):
        nextGen = getNextGeneration(nextGen, fitnessFunction)
        for member in nextGen:
            if fitnessFunction(member) <= 0:
                print(f"Found a solution during iteration {iteration}:")
                printNQueens(member)
                break
        # For else 😎
        else:
            continue
        break
