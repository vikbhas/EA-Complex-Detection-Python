import random

def crossover(parent_1, parent_2, parameter_dimension, child=None):
    pc = 0.5
    
    rand = random.uniform(0, 1)
    
    for i in range(1, parameter_dimension):
        if rand <= pc:
            child['chromosome'][i] = parent_1['chromosome'][i]
        else:
            child['chromosome'][i] = parent_2['chromosome'][i]
            
    return child

    