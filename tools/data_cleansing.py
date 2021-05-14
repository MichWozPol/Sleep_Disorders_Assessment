import pandas as pd

db = pd.read_csv("C:\\Users\\micha\\OneDrive\\Documents\\Programowanie\\Python\\Sleep_Disorders_Assessment\\project_resources\\prezentacja 2\\votes_weka_newest.csv",error_bad_lines=False)

print(db["3"][:])
print(db["9"][:].head())