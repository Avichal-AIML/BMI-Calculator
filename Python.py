from tkinter import *
from tkinter import messagebox

def calculate_bmi():
    try:
        height = float(height_entry.get()) / 100
        weight = float(weight_entry.get())
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            category = "Underweight 😟"
            tip = "You might need to gain some weight. Consider a nutrition-rich diet!"
        elif 18.5 <= bmi < 24.9:
            category = "Normal 😊"
            tip = "You're doing great! Keep maintaining a balanced lifestyle."
        elif 25 <= bmi < 29.9:
            category = "Overweight 😐"
            tip = "Consider light exercise and a healthy diet."
        else:
            category = "Obese 😟"
            tip = "Consult a doctor and work on a weight management plan."

        result_label.config(
            text=f"Your BMI: {bmi}\nCategory: {category}\n\n💡 Tip: {tip}",
            fg="#1b5e20"
        )

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for height and weight.")

# GUI Setup
bmi_app = Tk()
bmi_app.title("💪 BMI Calculator")
bmi_app.geometry("400x400")
bmi_app.configure(bg="#e8f5e9")

Label(bmi_app, text="BMI Calculator", font=("Helvetica", 18, "bold"), bg="#e8f5e9", fg="#2e7d32").pack(pady=10)

frame = Frame(bmi_app, bg="#c8e6c9", padx=20, pady=20)
frame.pack(pady=20)

Label(frame, text="Height (cm):", font=("Arial", 12), bg="#c8e6c9").grid(row=0, column=0, sticky=W, pady=5)
height_entry = Entry(frame, font=("Arial", 12))
height_entry.grid(row=0, column=1, pady=5)

Label(frame, text="Weight (kg):", font=("Arial", 12), bg="#c8e6c9").grid(row=1, column=0, sticky=W, pady=5)
weight_entry = Entry(frame, font=("Arial", 12))
weight_entry.grid(row=1, column=1, pady=5)

Button(bmi_app, text="Calculate BMI", font=("Arial", 12, "bold"), bg="#66bb6a", fg="white", command=calculate_bmi).pack(pady=10)

result_label = Label(bmi_app, text="", font=("Arial", 12), bg="#e8f5e9", wraplength=350, justify=LEFT)
result_label.pack(pady=10)

bmi_app.mainloop()
