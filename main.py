import tkinter as tk

# window
window = tk.Tk()
window.title("BMI Calculator")
window.minsize(288, 240)
window.config(padx=15, pady=15)

# final label
final_label = tk.Label()

# weight
weight_label = tk.Label()
weight_label.config(text="Enter Your Weight (kg)", font=("Bahnschrift", 10, "bold"))
weight_label.pack()
weight_entry = tk.Entry()
weight_entry.pack()

# height
height_label = tk.Label()
height_label.config(text="Enter Your Height (cm)", font=("Bahnschrift", 10, "bold"))
height_label.pack()
height_entry = tk.Entry()
height_entry.pack()


def bmi_query():
    user_height = height_entry.get()
    user_weight = weight_entry.get()
    if user_height == "" or user_weight == "":
        final_label.config(text="Fill in the blanks !", font=("Bahnschrift", 15, "bold"))
    else:
        try:
            user_weight = float(user_weight)
            user_height = float(user_height)
            user_bmi = user_weight / (user_height / 100) ** 2
            if user_bmi <= 0:
                final_label.config(text="Enter a valid value !", font=("Bahnschrift", 15, "bold"))
            elif 0 < user_bmi <= 16:
                final_label.config(text=f"Your BMI is {round(user_bmi, 2)}\nYou are severely thin!",
                                   font=("Bahnschrift", 13, "bold"))
            elif 16 < user_bmi <= 17:
                final_label.config(text=f"Your BMI is {round(user_bmi, 2)}\nYou are mild thin!",
                                   font=("Bahnschrift", 13, "bold"))
            elif 17 < user_bmi <= 18.5:
                final_label.config(text=f"Your BMI is {round(user_bmi, 2)}\nYou are normal weight",
                                   font=("Bahnschrift", 13, "bold"))
            elif 25 < user_bmi <= 30:
                final_label.config(text=f"Your BMI is {round(user_bmi, 2)}\nYou are overweight",
                                   font=("Bahnschrift", 13, "bold"))
            elif 30 < user_bmi <= 35:
                final_label.config(text=f"Your BMI is {round(user_bmi, 2)}\nYou are obese class 2",
                                   font=("Bahnschrift", 13, "bold"))
            elif 35 < user_bmi <= 40:
                final_label.config(text=f"Your BMI is {round(user_bmi, 2)}\nYou are obese class 3",
                                   font=("Bahnschrift", 13, "bold"))

        except:
            final_label.config(text="Enter a valid value !", font=("Bahnschrift", 15, "bold"))


# calculate button
calc_button = tk.Button(text="Calculate BMI", command=bmi_query)
calc_button.pack(pady=15)

final_label.pack(pady=10)

tk.mainloop()
