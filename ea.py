from operator import ge
import random
from best_individual import best_individual
from elitism import elitism
from crossover import crossover
from mutation import mutation
from h_mutation import top_mutataion
from individual_to_cmplx_decoding import individual_to_cmplx_decoding
from compute_fitness import compute_fitness
import datetime

def ea(a,n,mutation_type,indices_interaction_protein, num_interaction_protein,
                                    population, population_size,pm):
    result_list = []
    child = population
    generations = 100
    for generation_counter in range(1,generations+1):
        ct = datetime.datetime.now()
        print("GENERATION COUNTER")
        print(generation_counter)
        print("TIME : ",ct)
        population = child
        selected_parents = {}
        parent_1 = []
        parent_2 = []
        
        for problem_counter in range (1,population_size+1):
            rand_int_temp_1 = random.uniform(0, 1)
            rand_int_temp_2 = random.uniform(0, 1)
            
            rand_num_1 = int(rand_int_temp_1*(population_size -1)+1)
            rand_num_2 = int(rand_int_temp_2*(population_size -1)+1)
            
            candidate_1_parent_1 = population[rand_num_1]
            candidate_2_parent_1 = population[rand_num_2]
            
            if candidate_1_parent_1['Q'] > candidate_2_parent_1['Q']:
                parent_1 = candidate_1_parent_1
                p1 = rand_num_1
            else:
                parent_1 = candidate_2_parent_1;
                p1 = rand_num_2
                
            rand_int_temp_3 = random.uniform(0, 1)
            rand_int_temp_4 = random.uniform(0, 1)
            
            rand_num_3 = int(rand_int_temp_3*(population_size -1)+1)
            rand_num_4 = int(rand_int_temp_4*(population_size -1)+1)
            
            candidate_1_parent_2 = population[rand_num_3]
            candidate_2_parent_2 = population[rand_num_4]
            
            
            if candidate_1_parent_2['Q'] > candidate_2_parent_2['Q']:  #inform musthafa
                parent_2 = candidate_1_parent_2
                p2 = rand_num_4
            else:
                parent_2 = candidate_2_parent_2;
                p2 = rand_num_3
                
            index = 2 * (problem_counter -1) +1
            selected_parents[index] = p1
            selected_parents[index +1] = p2

            child_problem_counter = crossover(parent_1,parent_2, n, child[problem_counter])
            
            child[problem_counter] = child_problem_counter
        
        for problem_counter in range (1,population_size+1):
            if mutation_type == 1:
                child_problem_counter = mutation(child[problem_counter], indices_interaction_protein, num_interaction_protein, pm)
            elif mutation_type == 2:
                child_problem_counter = top_mutataion(a, child[problem_counter], indices_interaction_protein, num_interaction_protein, pm)
            
            child[problem_counter] = child_problem_counter
        
        child = individual_to_cmplx_decoding(n,num_interaction_protein, child, population_size)
        child = compute_fitness(a, n,indices_interaction_protein, num_interaction_protein,
                                    child, population_size)
        child = elitism(population, population_size, child)
        results = best_individual(child, population_size,generation_counter)
        result_list.append(results)
    print("END")
            
            
    return results