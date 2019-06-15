import random

N = 50
POPULATION_SIZE = 1000
  
def num_of_attack(state):
    attack_cnt = 0
    for i in range(len(state)-1):
        for j in range(i+1,len(state)):
            if state[i] == state[j] or i+state[i]==j+state[j] or i-state[i]==j-state[j]: 
                attack_cnt += 1
    return attack_cnt

class Queen:
    def __init__(self, state=None):
        self.state = state
        self.score = num_of_attack(state)
    def __str__(self):
        return "state={} score={}".format(self.state,self.score)
    
#print(num_of_attack([6,4,2,0,5,7,1,3]))
##q1 = Queen([6,4,2,0,5,7,1,3])
##q2 = Queen([1,1,1,1,1,1,1,1])
##print(q1)
##print(q2)
def tournament_selection(population):
    winner = random.choice(population)
    for i in range(5):
        contender = random.choice(population)
        if winner.score > contender.score:
            winner = contender
    
    return winner

def cross_over(p1,p2,pos):
    c1 = p1[:pos] + p2[pos:]
    c2 = p2[:pos] + p1[pos:]
    return c1, c2

def mutate(state):
    # change duplicated values into some values not used yet
    # eg) mutate([1,3,0,3,1]) -> [1,3,0,2,4] or [1,3,0,4,2]
    all_rows = set(range(N))
    rows = set(state)
    remaining = all_rows - rows
    rows_so_far = set()
    new_state = []
    for r in state:
        if r not in rows_so_far:
            rows_so_far.add(r)
            new_state.append(r)
        else:
            new_state.append(remaining.pop())
    return new_state

#print(mutate([1,3,0,3,1]))

population = []
for i in range(POPULATION_SIZE):
    s = list(range(N))
    random.shuffle(s)
    q = Queen(s)
    if q.score == 0:
        print("Lucky!!. Randomly generated solution", q)
        break
    population.append(q)
print(sum([q.score for q in population])/POPULATION_SIZE)

solved = False
for i in range(200):
    new_population = []
    visited_state = set()
    while len(new_population) < POPULATION_SIZE:
        parent1 = tournament_selection(population)
        parent2 = tournament_selection(population)
        c1state, c2state = cross_over(parent1.state,parent2.state,random.randint(1,N-1))
        child1, child2 = Queen(mutate(c1state)), Queen(mutate(c2state))
        if child1.score == 0:
            print("Found a solution", child1)
            solved = True
            break
        if child2.score == 0:
            print("Found a solution", child2)
            solved = True
            break

        if tuple(child1.state) not in visited_state:
            new_population.append(child1)
            visited_state.add(tuple(child1.state))
        if tuple(child2.state) not in visited_state:    
            new_population.append(child2)
            visited_state.add(tuple(child2.state))
    if solved:
        break
        
    print(sum([q.score for q in new_population])/POPULATION_SIZE)
    population = new_population

if not solved:
    for q in population:
        print(q)


