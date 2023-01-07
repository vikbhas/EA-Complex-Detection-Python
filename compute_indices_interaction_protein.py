def compute_indices_interaction_protein(a,n,indices_interaction_protein):
    
    for i in range(1,n):
        j = 1
        k = 1
        
        while (j <=n ):
            if (a[i][j]) == 1:
                indices_interaction_protein[i][k] = j
                k = k + 1;
            j=j+1
            
    return indices_interaction_protein
                