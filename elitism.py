def elitism(population, population_size, child):
    
    elitist_percentage = 0.1
    elitist_size = int(population_size * elitist_percentage)
    temp_population = {}
    temp_child = {}
    
    for individual_counter in range(1,population_size+1):
        temp_population[individual_counter] = population[individual_counter]['Q']
        
    temp_population_sorted = dict(sorted(temp_population.items(), key=lambda item: item[1],reverse=True))
    index_population = list(temp_population_sorted)
        
    for individual_counter in range(1,population_size+1):
        temp_child[individual_counter] = child[individual_counter]['Q']
        
    temp_child_sorted = dict(sorted(temp_child.items(), key=lambda item: item[1],reverse=True))
    index_child = list(temp_child_sorted)

    
    for elitist_counter in range(1,elitist_size):
        child[index_child[elitist_counter]] = population[index_population[elitist_counter]]
    return child