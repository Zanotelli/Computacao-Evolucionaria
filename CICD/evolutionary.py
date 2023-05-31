import random as rd
import numpy as np
import matplotlib.pyplot as plt

crossover_rate = 1
mutation_rate = 0.8
base_population = 20
pop_sample = 5
fitness_history = []


# UTIL

def argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)

def verify_condition(pupulation):
    return 0 in pupulation

def get_best_solution(population_fit):
    count = 0
    aux = 100
    for i in range(len(population_fit)):
        if population_fit[i] < aux:
            aux = population_fit[i]
            count = i
    return i

def draw_pop(pop):
    for i in range(len(pop)):
        line = ''.format((8-i), ' ')
        for j in range(len(pop)):
            if pop[j] == i:
                line = line + "X "
            else:
                line = line + "- "
        print(line)


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

def select_parents(pupulation, pop_sample):

    sample_pop = rd.sample(pupulation, pop_sample)

    sample_pop_fit = [0] * pop_sample
    for i in range(len(sample_pop_fit)):
        sample_pop_fit[i] = fitness_nq(sample_pop[i])

    parents_id = np.argsort(sample_pop_fit)[:2]
    parents = [sample_pop[parents_id[0]],
               sample_pop[parents_id[1]]]
    return parents

def cut_and_crossfill(N, parents):
    cross_point = rd.randint(1, N-1)

    p1 = [parents[0][:cross_point] , parents[0][cross_point:]]
    p2 = [parents[1][:cross_point] , parents[1][cross_point:]]

    f1 = p1[0]
    f2 = p2[0]
    for i in range(len(parents[1])):
        if not f1.__contains__(i):
            f1.append(i)
        if not f2.__contains__(i):
            f2.append(i)

    return [f1, f2]

def mutate_offspring(offspring, mutation_rate, N):
    for of in offspring:
        if rd.random() < mutation_rate:
            id1 = rd.randint(0, N-1)
            id2 = rd.randint(0, N-1)
            aux = of[id1]
            of[id1] = of[id2]
            of[id2] = aux
    return offspring

def draw_graph(datax, datay):
    plt.plot(range(datax+1), datay[0], "-g", label="Medium")
    plt.plot(range(datax+1), datay[1], "-r", label="Best")
    plt.legend(loc="upper right")
    plt.xlabel('Generation')
    plt.ylabel('Fittness')
    plt.show()
