# Regression problem
# y = a*x + b --> Linear Regression
# non-linear regression eg) y = a*x^2 + b*x + c
import random
import math
data_points = [(0,1),(1,3)]
c1 = 1
c2 = 2

# in case of quadratic regression y = a*x*x + b*x + c
# data_points =[(0,3),(1,2),(2,3),(3,6)]
# print(score([1,-2,3])) --> 0

def score(coefficients): # eg) a,b = [1,2]
    # return total error from data points to the line y=a*x+b
    a, b = coefficients
    total_error = 0
    for x,y in data_points:
        y2 = a * x + b
        e = abs(y2-y)
        total_error += e
    return total_error

class Particle:
    def __init__(self):
        self.pos = [random.uniform(-10,10), random.uniform(-10,10)]
        self.velocity = [random.uniform(-1,1), random.uniform(-1,1)]
        self.score = score(self.pos)
        self.best_score = self.score
        self.best_pos = self.pos[:]

    def update(self):
        # velocity update
        for i in range(2):
            my_gap = self.best_pos[i] - self.pos[i]
            g_gap = global_best_pos[i] - self.pos[i]
            self.velocity[i] += c1*random.random() * my_gap + c2*random.random()*g_gap
        # position update based on velocity
        for i in range(2):
            self.pos[i] += self.velocity[i]
        self.score = score(self.pos)
        if self.score < self.best_score:
            self.best_score = self.score
            self.best_pos = self.pos[:]

population = []
global_best_score = math.inf
for i in range(50):
    p = Particle()
    population.append(p)
    if p.score < global_best_score:
        global_best_score = p.score
        global_best_pos = p.pos[:]
    #print(p.pos, p.velocity, p.score)
print(global_best_score, global_best_pos)

for i in range(100):
    for p in population:
        p.update()
        if p.best_score < global_best_score:
            global_best_score = p.best_score
            global_best_pos = p.best_pos[:]
    print(global_best_score, global_best_pos)        

for p in population:
    print(p.score, p.pos, p.velocity)
##print(score([2,1]))
##print(score([2,5]))
##print(score([1,3]))
