import numpy as np


def compute_fitness(a, n,indices_interaction_protein, num_interaction_protein,
                                    population, population_size):
    m = sum(sum(a))
    
    for individual_counter in range(1,population_size+1):
        CmplxID = population[individual_counter]['CmplxID']
        k = max(CmplxID.values())
        cluster_k_volume = [0]*k;
        cluster_k_cardinality = [0]*k;
        cluster_k_degree = [0]*k;
        cluster_k_Q = [0]*k;

        for node_i in range(1,n+1):
            if (num_interaction_protein[node_i -1] != 0):
                cluster_k_cardinality[CmplxID[node_i]-1] = cluster_k_cardinality[CmplxID[node_i]-1] + 1
                cluster_k_degree[CmplxID[node_i] - 1] = cluster_k_degree[CmplxID[node_i] -1 ] + np.sum(a[node_i-1:])  #check here
                
            for node_j in range(0, num_interaction_protein[node_i - 1]):
                if (CmplxID[node_i] == CmplxID[indices_interaction_protein[node_i - 1][node_j]]):
                    cluster_k_volume[CmplxID[node_i]-1] = cluster_k_volume[CmplxID[node_i]-1] + a[node_i -1][indices_interaction_protein[node_i - 1][node_j] -1]

        
        for val in range(len(cluster_k_Q)):
            q_temp_1 = cluster_k_volume[val]/m
            q_temp_2 = ((cluster_k_degree[val]/(2*m))**2)
            cluster_k_Q[val] = (q_temp_1 - q_temp_2)
        q = sum(cluster_k_Q)
        population[individual_counter]['Q'] = q
    return population
