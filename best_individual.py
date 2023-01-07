def best_individual(child, population_size, generation_counter):
    results = {}
    best_index = 1
    
    for child_counter in range(2,population_size):
        if child[child_counter]['Q'] > child[best_index]['Q']:
            best_index = child_counter

    results[generation_counter] = {}
    results[generation_counter]['chromosome'] = child[best_index]['chromosome']
    results[generation_counter]['CmplxID'] = child[best_index]['CmplxID']
    results[generation_counter]['Q'] = child[best_index]['Q']
    
    return results