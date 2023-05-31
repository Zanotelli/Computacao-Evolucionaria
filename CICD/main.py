import random as rd
import numpy as np
import matplotlib.pyplot as plt

import evolutionary as ev

crossover_rate = 1
mutation_rate = 0.8
base_population = 20
pop_sample = 5
fitness_history = []



N = 0
try:
    N = int(input())
except:
    raise ValueError('ERROR: o valor digitado não é valido!')

max_generation = 10 * N
print("Número de rainhas do problema: ", N)
print("Máximo de gerações: ", max_generation)
print()

pupulation = ev.init_population(base_population, N)
population_fitt = [0] * base_population

for i in range(base_population):
    population_fitt[i] = ev.fitness_nq(pupulation[i])
print("Fittness da população inicial:")
print(population_fitt)

count_gen = 0
datay = [[], []]
for i in range(max_generation):
    parents = ev.select_parents(pupulation, pop_sample)

    offspring = ev.cut_and_crossfill(N, parents)

    ev.mutate_offspring(offspring, mutation_rate, N)

    pupulation = select_new_generation(pupulation, offspring)

    for j in range(base_population):
        population_fitt[j] = ev.fitness_nq(pupulation[j])

    datay[0].append(sum(population_fitt) / len(population_fitt))
    datay[1].append(min(population_fitt))

    count_gen = i
    if verify_condition(population_fitt):
        break

print()
print("Geração final: ", (count_gen+1))
print()
print("Fittness da população final:")
print(population_fitt)
print()
print("Melhor indivíduo:")
best_pop = pupulation[get_best_solution(population_fitt)]
print(best_pop)
print()
ev.draw_pop(best_pop)
ev.draw_graph(count_gen, datay)