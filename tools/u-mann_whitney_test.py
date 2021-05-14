import numpy as np
import pandas as pd
from scipy.io.arff import loadarff 

raw_data = loadarff('C:\\Users\\micha\\OneDrive\\Documents\\Programowanie\\Python\\Sleep_Disorders_Assessment\\project_resources\\prezentacja 2\\sda_db_double_quotes.arff')
df_data = pd.DataFrame(raw_data[0])

df.head()