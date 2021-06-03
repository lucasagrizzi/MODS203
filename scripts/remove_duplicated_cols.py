#------------------------------#
#--- FUNCTIONALITY ------------#
#------------------------------#

# This script is supposed to delete duplicated columns in each dataset from the repository.


import os
import pandas as pd 

datasets = [os.path.join(path, name) for path, subdirs, files in os.walk(".\..\datasets") for name in files if name.endswith('.csv.zip')]
for idx, dataset in enumerate(datasets):
    df = pd.read_csv(dataset)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df.to_csv(dataset)
    print(f"\r{idx+1}/{len(datasets)}: {dataset}", end="")