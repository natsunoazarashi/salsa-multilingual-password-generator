from tkinter import *
import pandas as pd
import random

# re module for regex

language_selected = []

window = Tk()
window.title("Salsa Multilingual Password Generator")
window.config(padx=20,pady=20)

df = pd.read_csv("word_list.csv")

animals_df = df[df["category"] == "animals"]
places_df = df[df["category"] == "places"]
concepts_df = df[df["category"] == "concepts"]
adjectives_df = df[df["category"] == "adjectives"]

def update_list():
    global language_selected
    language_selected = [lang for lang, var in language_vars.items() if var.get() == 1]
    print("Languages selected:", language_selected)  # For debugging

def generate_password():
    # print(language_selected)
    if language_selected:
        password_entry.delete(0, "end")

        # check if the dataframes have data
        if not animals_df.empty and not adjectives_df.empty and not places_df.empty:
            # Sample one row for each dataframe
            random_row_adj = adjectives_df.sample().iloc[0]
            random_row = animals_df.sample().iloc[0]
            random_row_places = places_df.sample().iloc[0]


            # Randomly select a language from the selected languages
            random_language_1 = random.choice(language_selected)
            random_language_2 = random.choice(language_selected)
            random_language_3 = random.choice(language_selected)
            # Get the word from the selected language column
            # we select one language if the mode is easy, otherwise we mix the languages
            if difficulty.get() == 1:
                random_word_adj = random_row_adj[random_language_1]
                random_word = random_row[random_language_1]
                random_word_places = random_row_places[random_language_1]
            else:
                random_word_adj = random_row_adj[random_language_1]
                random_word = random_row[random_language_2]
                random_word_places = random_row_places[random_language_3]
            password_entry.insert(0, f"{random_word_adj}{random_word}{random_word_places}")
        else:
            print("No animals found in the DataFrame.")
    else:
        print("No language selected.")





canvas = Canvas(window,width=218,height=230)
salsa_img = PhotoImage(file="image_assets/salsa bowl.png")
canvas.create_image(109,115,image=salsa_img)
canvas.grid(row=1,column=1,rowspan=6,columnspan=1)

password_entry = Entry(window,width=35)
password_entry.grid(row=0,column=1)

# Dictionary to hold language checkbutton variables
language_vars = {
    "english": IntVar(value=1),
    "spanish_translit": IntVar(value=0),
    "french_translit": IntVar(value=0),
    "german_translit": IntVar(value=0),
    "japanese_romaji": IntVar(value=0),
    "korean_RR": IntVar(value=0)
}

# Function to create a language checkbutton
def create_language_checkbutton(language_label,language, row, column, image_file):
    flag_img = PhotoImage(file=image_file)
    checkbutton = Checkbutton(window, text=language_label.title(), image=flag_img, variable=language_vars[language], compound="left", command=update_list)
    checkbutton.image = flag_img  # Keep a reference!
    checkbutton.grid(row=row, column=column)
    # Label(window, text=language_label.title()).grid(row=row+1, column=column)

create_language_checkbutton("english","english", 1, 0, "image_assets/british flag.png")
create_language_checkbutton("spanish","spanish_translit", 3, 0, "image_assets/spanish flag.png")
create_language_checkbutton("french","french_translit", 5, 0, "image_assets/french flag.png")
create_language_checkbutton("german","german_translit", 1, 2, "image_assets/german_flag.png")
create_language_checkbutton("japanese","japanese_romaji", 3, 2, "image_assets/japanese_flag.png")
create_language_checkbutton("korean","korean_RR", 5, 2, "image_assets/south korean flag.png")

# Shared IntVar for both Radiobuttons
difficulty = IntVar(value=1)  # 1 for easy mode, 2 for hard mode

easy_mode_button = Radiobutton(window,text="easy",variable=difficulty,value=1)
easy_mode_button.grid(row=7,column=0)
hard_mode_button = Radiobutton(window,text="hard",variable=difficulty,value=2)
hard_mode_button.grid(row=7,column=2)


generate_button = Button(text="Generate Password",command=generate_password)
generate_button.grid(row=7,column=1)

update_list()

window.mainloop()