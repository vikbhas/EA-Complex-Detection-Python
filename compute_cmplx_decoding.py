def compute_cmplx_decoding(individual, n, num_interaction_protein):
    current_cmplx_id = 0
    next_individual_gene_locus = 0
    
    while (sum(individual['CmplxFlag'].values())) != n:
        current_cmplx_id += 1
        next_individual_gene_locus += 1
        
        while individual['CmplxFlag'][next_individual_gene_locus] == 1: 
            next_individual_gene_locus+= 1

        if individual['chromosome'][next_individual_gene_locus] == 0:
            individual['CmplxFlag'][next_individual_gene_locus] = 1
            next_individual_gene_locus += 1
        else:
            individual['CmplxID'][next_individual_gene_locus] = current_cmplx_id
            individual['CmplxID'][individual['chromosome'][next_individual_gene_locus]] = current_cmplx_id
            individual['CmplxFlag'][next_individual_gene_locus] = 1
            individual['CmplxFlag'][individual['chromosome'][next_individual_gene_locus]] = 1
        
        for i in range(next_individual_gene_locus+1, n+1):
            if individual['chromosome'][i] == 0:
                individual['CmplxFlag'][i] = 1
                next_individual_gene_locus += 1
            elif (individual['chromosome'][i] == next_individual_gene_locus) \
                or (individual['chromosome'][i] == individual['chromosome'][next_individual_gene_locus]):
                    
                individual['CmplxID'][i] = current_cmplx_id
                individual['CmplxFlag'][i] = 1
                individual['CmplxID'][individual['chromosome'][i]] = current_cmplx_id
                individual['CmplxFlag'][individual['chromosome'][i]] = 1
                
        more_interaction_in_this_cmplx = 1
        
        while (sum(individual['CmplxFlag'].values())!=n) and (more_interaction_in_this_cmplx == 1):
            flag = 0
            for i in range(next_individual_gene_locus+1, n):
                if num_interaction_protein[i] != 0 :
                    if (individual['CmplxID'][i] == 0) and (individual['CmplxID'][individual['chromosome'][i]]== current_cmplx_id) \
                        or ((individual['CmplxID'][individual['chromosome'][i]])==0) and (individual['CmplxID'][i] == current_cmplx_id):
                            flag = 1
                            individual['CmplxID'][i] = current_cmplx_id
                            individual['CmplxFlag'][i] = 1
                            individual['CmplxID'][individual['chromosome'][i]] = current_cmplx_id
                            individual['CmplxFlag'][individual['chromosome'][i]] = 1
     
            if (flag == 0):
                more_interaction_in_this_cmplx = 0
        
        next_individual_gene_locus = 0    
    return individual


