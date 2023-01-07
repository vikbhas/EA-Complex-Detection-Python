def compute_adjancy_matrix(protein_label_pairs):
    rows_and_columns = len(protein_label_pairs)
    A = {}
    for row_num in range(1,rows_and_columns):
        i = protein_label_pairs[row_num][1]
        j = protein_label_pairs[row_num][2]
        
        A[i][j] = 1
        A[j][i] = 1
        A[i][i] = 0
        
    return A