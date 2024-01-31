# This script is kept to show how the transliteration was done for the european languages

import pandas as pd
import unicodedata



def remove_accents(input_string):
    # Normalize the input string using NFKD normalization, which separates characters 
    # into their base characters and combining marks (e.g., accents). The list comprehension 
    # then filters out these marks, leaving only the base characters. This effectively 
    # removes accents from the input string.
    return "".join([c for c in unicodedata.normalize("NFKD",input_string) if not unicodedata.combining(c)])

df = pd.read_csv("word_list.csv")

euro_lang_list = ["french","spanish","german"]

for language in euro_lang_list:
    translit_column = f"{language}_translit"
    df[translit_column] = df[language].apply(remove_accents)

df.to_csv("new_word_list.csv",index=False)
