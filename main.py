import tkinter as tk
from Distance_Converter import MilesToKM

PAD_AMOUNT = 35

FONT=("Times New Roman",14)

# Initialise Window
window = tk.Tk()
strTitle = "Mile to KM Converter"
window.title(strTitle)
window.minsize(width=300, height=100)
window.config(padx=PAD_AMOUNT, pady=PAD_AMOUNT)

# Miles Input
miles_input = tk.Entry(width=15, font=FONT, justify="left")
miles_input.grid(row=0, column=1)


def create_label(text_label):
    return tk.Label(text=text_label, font=FONT, justify="left")


# Miles Input Supporting Units
miles_units_label = create_label(text_label="Miles")
miles_units_label.grid(row=0, column=2)

# KM equality condition label
equal_condition_label = create_label(text_label="is equal to")
equal_condition_label.grid(row=1, column=0)

# KM Supporting Units
km_units_label = create_label(text_label="Km")
km_units_label.grid(row=1, column=2)


def calculate_distance(*arg):
    """outputs the distance specified into the km output label"""
    km_output_label["text"] = str(MilesToKM(float(miles_input.get())))


# KM Output
km_output_label = create_label(text_label="0")
km_output_label.grid(row=1, column=1)

window.bind("<Return>", calculate_distance)

calculate_button = tk.Button(text="Calculate", command=calculate_distance, font=FONT)
calculate_button.grid(row=2, column=1)

miles_input.focus()

window.mainloop()