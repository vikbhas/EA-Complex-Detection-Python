import pandas as pd
from scipy.io import loadmat 
from create_population import create_population
from individual_to_cmplx_decoding import individual_to_cmplx_decoding
from compute_fitness import compute_fitness
from ea import ea
import datetime

protein_mat_file = loadmat('/Users/vigneshwaraa/Desktop/DigEng/2nd Sem/Evaluation Algorithm Project/EA_Complex_Detection_Python/DataSets/Protein/1-Protein-Yeast-D1-Files.mat') 
complex_mat_file = loadmat('/Users/vigneshwaraa/Desktop/DigEng/2nd Sem/Evaluation Algorithm Project/EA_Complex_Detection_Python/DataSets/Complex/1-Complex-D1-Files.mat')

complex_protein_label = complex_mat_file['ComplexProteinLabel']
number_of_known_proteins_in_complex = complex_mat_file['NumberOfKnownProteinsInComplexes']
number_of_protein_in_complexes = complex_mat_file['NumberOfProteinsInComplexes']
overlap_complex_flag = complex_mat_file['OverlapComplexesFlag']

a = protein_mat_file['A']
indices_interaction_protein = protein_mat_file['IndicesInteractionProtein']
known_proteiens = protein_mat_file['KnownProteins']
max_num_interaction_protein = protein_mat_file['MaxNumInteractionProtein']
n = protein_mat_file['N'][0][0]
num_interaction_protein = protein_mat_file['NumInteractionProtein'][0]
protein_label = protein_mat_file['ProteinLabel']
protein_label_pairs = protein_mat_file['ProteinLabelPairs']
max_runs = int(input('Enter the maximum number of run \n MaxRun: '))
mutation_type = int(input('\n Enter type of mutation: \n 1: Canonical Mutation \n 2: Topological Mutation \n Mutation-Type: '))

if (mutation_type == 1):
    pm = 0.2
elif (mutation_type == 2):
    pm = float(input('Enter the Pm value:'))

population_size = 100
for run_number in range(0, max_runs):
    results_group = []
    population = []
    ct_1 = datetime.datetime.now()
    print("Create Population time:-", ct_1)
    population = create_population(n,num_interaction_protein,indices_interaction_protein,population_size)
    ct_2 = datetime.datetime.now()
    print("individual_to_cmplx_decoding time:-", ct_2)
    population = individual_to_cmplx_decoding(n,num_interaction_protein, population, population_size) 
    ct_3 = datetime.datetime.now()
    print("Compute Fitness time:-", ct_3) 
    population = compute_fitness(a, n,indices_interaction_protein, num_interaction_protein,
                                    population, population_size)
    ct_4 = datetime.datetime.now()
    print("EA time:-", ct_4)
    results = ea(a,n,mutation_type,indices_interaction_protein, num_interaction_protein,
                                    population, population_size,pm)
    
    print(results)