from compute_cmplx_decoding import compute_cmplx_decoding
def individual_to_cmplx_decoding(n,num_interaction_protein, population, population_size):
    for individual_counter in range(1,population_size+1):
        population[individual_counter]['CmplxFlag'] = {}
        population[individual_counter]['CmplxID'] = {}
        for protein_counter in range(0,n):
            if (num_interaction_protein[protein_counter]) != 0:
                population[individual_counter]['CmplxFlag'][protein_counter+1] = 0
                population[individual_counter]['CmplxID'][protein_counter+1] = 0
            else:
                population[individual_counter]['CmplxFlag'][protein_counter+1] = 1
                population[individual_counter]['CmplxID'][protein_counter+1] = 0
                
    for individual_counter in range(1,population_size+1):
        population[individual_counter] = compute_cmplx_decoding(population[individual_counter], n, num_interaction_protein)
    return population
