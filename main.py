from tkinter import *
from tkinter import messagebox
import pandas as pd
import secrets

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

# creates a function to make the first letter in each word in capital letters randomly
def random_cap_first_letter(word):
    if not word:
        return word
    first_char = secrets.choice([word[0].upper(),word[0].lower()])
    return first_char + word[1:].lower()

def get_random_specials():
    special_chars_list = ['!', '@', '#', '$', '%', '&', '*', '-', '_']
    # Randomly choose to include a special character, a number, both, or none
    specials = ""
    if secrets.choice([True, False]):
        specials += secrets.choice(special_chars_list)  # Add a special character
    if secrets.choice([True, False]):
        specials += str(secrets.randbelow(10))  # Add a number
    return specials


def update_list():
    global language_selected
    language_selected = [lang for lang, var in language_vars.items() if var.get() == 1]
    # uncomment the following for debugging purpose
    # print("Languages selected:", language_selected)  # For debugging

def generate_password():
    # print(language_selected)
    if language_selected:
        password_entry.delete(0, "end")

        # check if the dataframes have data
        if not animals_df.empty and not adjectives_df.empty and not places_df.empty:
            # Randomly select a language from the selected languages
          # Sample one row from each DataFrame
            random_row_adj = adjectives_df.sample().iloc[0]
            random_row_animal = animals_df.sample().iloc[0]
            random_row_place = places_df.sample().iloc[0]
            
            # For easy mode, use one language for all words; for hard mode, potentially use different languages for each word
            if difficulty.get() == 1:
                chosen_language = secrets.choice(language_selected)
                lang_adj = lang_animal = lang_place = chosen_language
            else:
                lang_adj, lang_animal, lang_place = [secrets.choice(language_selected) for _ in range(3)]
            
            # Select words based on the chosen languages
            random_word_adj = random_row_adj[lang_adj]
            random_word_animal = random_row_animal[lang_animal]
            random_word_place = random_row_place[lang_place]
            password = (
                f"{random_cap_first_letter(random_word_adj)}"
                f"{get_random_specials()}"
                f"{random_cap_first_letter(random_word_animal)}"
                f"{get_random_specials()}"
                f"{random_cap_first_letter(random_word_place)}"
                f"{get_random_specials()}"
            )
            # password_entry.insert(0, f"{random_cap_first_letter(random_word_adj)}{get_random_specials()}{random_cap_first_letter(random_word_animal)}{get_random_specials()}{random_cap_first_letter(random_word_place)}{get_random_specials()}")
            password_entry.insert(0,password)
        else:
            print("No animals found in the DataFrame.")
    else:
        messagebox.showinfo(title="Language Selection Issue:", message="Please select at least one language.")


# function to copy the password in the Entry by clicking 
def copy_password(event):
    password_entry.select_range(0,"end")
    password_entry.clipboard_clear()
    password_entry.clipboard_append(password_entry.get())


canvas = Canvas(window,width=218,height=230)
salsa_img = PhotoImage(file="image_assets/salsa bowl.png")
canvas.create_image(109,115,image=salsa_img)
canvas.grid(row=1,column=1,rowspan=6,columnspan=1)

password_entry = Entry(window,width=35)
password_entry.grid(row=0,column=1)
# the binding of copying the password with a left click of the mouse
password_entry.bind("<Button-1>",copy_password)

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

easy_img = PhotoImage(file="image_assets/jalapeno.png")
easy_mode_button = Radiobutton(window,text="easy",image=easy_img,compound="left",variable=difficulty,value=1)
easy_mode_button.grid(row=7,column=0)
hard_img = PhotoImage(file="image_assets/red_pepper.png")
hard_mode_button = Radiobutton(window,text="hard",image=hard_img,compound="left",variable=difficulty,value=2)
hard_mode_button.grid(row=7,column=2)


generate_button = Button(text="Generate Password",command=generate_password)
generate_button.grid(row=7,column=1)

update_list()

window.mainloop()