
def compute_num_interaction_protein(a,n):
    num_interaction_protein = {}
    
    for i in range(1,n):
        num_interaction_protein[i] = sum(a[i:])   #all elements in i row
        
    return num_interaction_protein