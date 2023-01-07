import random
def mutation(child, indices_interaction_protein, num_interaction_protein, pm):
    rand = random.uniform(0, 1)
    for i in range(1, len(child)+1):
        if (num_interaction_protein[i -1] > 0) and (rand <= pm):
            random_num = round((rand * (num_interaction_protein[i] - 1) + 1))
            child['chromosome'][i] = indices_interaction_protein[i][random_num]
    
    return child
                           