import random
def create_population(n,num_interaction_protein,indices_interaction_protein,population_size):
    print("Create Population")
    population = {}
    for individual_counter in range(1,population_size+1):
        population[individual_counter] = {}
        population[individual_counter]['chromosome'] = {}
        for protein_counter in range(1,n+1):
            if num_interaction_protein[protein_counter - 1] > 0 :
                random_num = (random.randint(0, num_interaction_protein[protein_counter - 1]-1))
                population[individual_counter]['chromosome'][protein_counter] = indices_interaction_protein[protein_counter -1][random_num]
            else:
                population[individual_counter]['chromosome'][protein_counter] = 0
    return population    
            