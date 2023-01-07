import scipy.io
import pandas as pd
mat = scipy.io.loadmat('/Users/vigneshwaraa/Desktop/DigEng/2nd Sem/Evaluation Algorithm Project/EA Complex Detection Python/DataSets/Protein/1-Protein-Yeast-D1-Files.mat') 
mat = {k:v for k, v in mat.items() if k[0] != '_'}
data = pd.DataFrame({k: pd.Series(v[0]) for k, v in mat.items()})
data.to_csv("Protein.csv")