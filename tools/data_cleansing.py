#3-->gender, 9-->sleep_quality
#for this data chance is higher than 0.05 so we have to dissmiss assumption that 

import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu
from scipy.stats import norm

def show_gender_sleep_quality_columns(df):
    print(df["3"][:])
    print("\n\n")
    print(df["9"][:])

def encode_text_sleep_quality(df):
    replace_dict = {"'bardzo zła'": 1, "'znacznie niesatysfakcjonująca'": 2, "'niezacznie niesatysfakcjonująca'": 3, "'satysfakcjonująca'": 4}
    df["9"] = df["9"].map(replace_dict)
    return df

def delete_rows_with_gender_equals_other(df):
    df["3"].replace("'inna'", np.nan, inplace=True)
    return df

def drop_nan_data(df):
    new_df.dropna(inplace=True)
    return df

def create_list(df):
    return list(df)

if __name__ == "__main__":
    df = pd.read_csv("C:\\Users\\micha\\OneDrive\\Documents\\Programowanie\\Python\\Sleep_Disorders_Assessment\\project_resources\\prezentacja 2\\votes_weka_newest.csv", error_bad_lines=False)
    new_df = encode_text_sleep_quality(df)
    new_df = delete_rows_with_gender_equals_other(new_df)
    new_df = drop_nan_data(new_df)
    sleep_quality_df = new_df["9"]
    male = new_df["3"]=="'mężczyzna'"
    female = new_df["3"]=="'kobieta'"

    male_list = create_list(sleep_quality_df[male][:])
    female_list = create_list(sleep_quality_df[female][:])

    print(mannwhitneyu(male_list, female_list, use_continuity=False, alternative = 'two-sided'))
    U, pval = mannwhitneyu(male_list, female_list, use_continuity=False, alternative = 'two-sided')
    print("Z value: " + norm.ppf(pval/2))
