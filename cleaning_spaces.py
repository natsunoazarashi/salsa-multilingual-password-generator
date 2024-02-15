import pandas as pd

df = pd.read_csv("word_list.csv")

# Specify the columns you want to modify
columns_to_modify = ["english", "french_translit", "japanese_romaji",
                     "korean_RR", "spanish_translit", "german_translit"]

# Replace spaces with "_" in the specified columns
for column in columns_to_modify:
    df[column] = df[column].astype(str).replace(" ", "_", regex=True)

# Save the modified DataFrame back to a CSV file, if needed
df.to_csv("modified_word_list.csv", index=False)