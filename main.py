from tkinter import *
import pandas as pd
import random

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
    print(language_selected)
    if language_selected:
        password_entry.delete(0, "end")
        # Filter DataFrame for 'animals' category
        animals_df = df[df['category'] == 'animals']
        if not animals_df.empty:
            # Randomly select a row from the animals DataFrame
            random_row = animals_df.sample().iloc[0]
            # Randomly select a language from the selected languages
            random_language = random.choice(language_selected)
            # Get the word from the selected language column
            random_word = random_row[random_language]
            password_entry.insert(0, random_word)
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

british_flag_img = PhotoImage(file="image_assets/british flag.png")
# create a variable to check if the button is checked, the value is put to 1 as a default starter
# english_checked = IntVar(value=1)
english_checked = IntVar()
english_checkbutton = Checkbutton(text="English",image=british_flag_img,variable=language_vars["english"],command=update_list)
english_checkbutton.grid(row=1,column=0)
english_label = Label(window,text="English")
english_label.grid(row=2,column=0)

spanish_flag_img = PhotoImage(file="image_assets/spanish flag.png")
# spanish_checked = IntVar(value=0)
spanish_checkbutton = Checkbutton(text="Spanish",image=spanish_flag_img,variable=language_vars["spanish_translit"],command=update_list)
spanish_checkbutton.grid(row=3,column=0)
spanish_label = Label(window,text="Spanish")
spanish_label.grid(row=4,column=0)


french_flag_img = PhotoImage(file="image_assets/french flag.png")
french_checked = IntVar(value=0)
french_checkbutton = Checkbutton(text="French",image=french_flag_img,variable=language_vars["french_translit"],command=update_list)
french_checkbutton.grid(row=5,column=0)
french_label = Label(window,text="French")
french_label.grid(row=6,column=0)


german_flag_img = PhotoImage(file="image_assets/german_flag.png")
german_checked = IntVar(value=0)
german_checkbutton = Checkbutton(text="German",image=german_flag_img,variable=language_vars["german_translit"],command=update_list)
german_checkbutton.grid(row=1,column=2)
german_label = Label(window,text="German")
german_label.grid(row=2,column=2)


japanese_flag_img = PhotoImage(file="image_assets/japanese_flag.png")
japanese_checkbutton = Checkbutton(text="Japanese",image=japanese_flag_img,variable=language_vars["japanese_romaji"],command=update_list)
japanese_checkbutton.grid(row=3,column=2)
japanese_label = Label(window,text="Japanese")
japanese_label.grid(row=4,column=2)


korean_flag_img = PhotoImage(file="image_assets/south korean flag.png")
korean_checked = IntVar(value=0)
korean_checkbutton = Checkbutton(text="Korean",image=korean_flag_img,variable=language_vars["korean_RR"],command=update_list)
korean_checkbutton.grid(row=5,column=2)
korean_label = Label(window,text="Korean")
korean_label.grid(row=6,column=2)

generate_button = Button(text="Generate Password",command=generate_password)
generate_button.grid(row=7,column=1)

update_list()

window.mainloop()