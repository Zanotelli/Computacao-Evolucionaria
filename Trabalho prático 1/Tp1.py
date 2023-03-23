import random as rd
import numpy as np

crossover_rate = 1
mutation_rate = 0.8

def init_population(_mu:int = 20, n:int = 8):
    population = []
    for i in range (_mu):
        population.append(rd.sample(range(n), n))
    return population

def fitness_nq(solution):
    xeques = 0
    for i in range(0,len(solution)):
        for j in range(0,len(solution)):
            if i!=j:
                if i-solution[i] == j-solution[j] or i+solution[i] == j+solution[j]:
                    xeques+=1
    return xeques


pop = init_population(20, 8)
print(pop)

fitness_nq(pop)

pop_fitness = [fitness_nq(each_solution) for each_solution in pop]
print(pop_fitness)