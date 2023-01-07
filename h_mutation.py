import random
from turtle import pen
def top_mutataion(a, child, indices_interaction_protein, num_interaction_protein, pm):
    n = len(a)
    print(n)
    rand = random.uniform(0, 1)
    for node_i in range(1,n+1):
        if (num_interaction_protein[node_i -1] > 0) and (rand <= pm):
            k_node_i_in = 0
            k_node_i_out = 0
            
            for node_j in range(1, n+1):
                if (node_i!= node_j) and (child['CmplxID'][node_j] == child['CmplxID'][node_i]):
                    k_node_i_in = k_node_i_in + a[node_i -1][node_j -1]
                
                if (node_i!= node_j) and (child['CmplxID'][node_j] != child['CmplxID'][node_i]):
                    k_node_i_out = k_node_i_out + a[node_i -1 ][node_j -1 ]
            
            if (k_node_i_in <= k_node_i_out):
                old_cluster = child['CmplxID'][node_i]
                new_cluster = child['CmplxID'][node_i]
                new_diff = k_node_i_in - k_node_i_out
                
                k = max(child['CmplxID'])    
                
                for i in range(1,k+1):
                    if (i!= old_cluster):
                        k_node_i_in = 0
                        k_node_i_out = 0
                        
                        for node_j in range(1,n+1):
                            if (node_i != node_j) and (child['CmplxID'][node_j] == i):
                                k_node_i_in = k_node_i_in + a[node_i -1][node_j-1]
                            if (node_i != node_j) and (child['CmplxID'][node_j] != i):
                                k_node_i_out = k_node_i_out + a[node_i-1][node_j-1]

                        if new_diff < (k_node_i_in - k_node_i_out):
                            new_diff = k_node_i_in - k_node_i_out
                            new_cluster = i
                        else:
                            if (new_diff == (k_node_i_in - k_node_i_out)):
                                rand_temp_num = random.uniform(0, 1)
                                if (rand_temp_num > 0.5):
                                    new_cluster = i
                                    
                child['CmplxID'][node_i] = new_cluster
                connected_node = child['chromosome'][node_i]
                
                for connected_node_counter in range(1,num_interaction_protein[node_i-1]+1):
                    if indices_interaction_protein[node_i-1][connected_node_counter-1] == 0:
                        val = 1
                    else:
                        val = indices_interaction_protein[node_i-1][connected_node_counter-1]
                        
                    if (child['CmplxID'][val] == new_cluster):
                        connected_node = indices_interaction_protein[node_i-1][connected_node_counter-1]
                
                child['chromosome'][node_i] = connected_node
    return child