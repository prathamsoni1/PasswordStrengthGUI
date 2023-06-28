import re
import tkinter as tk
import hashlib

BG_COLOR = "#222222"
FG_COLOR = "#a38e4d"
BUTTON_COLOR = "#FF0000"

def score_password(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 2
    if re.search(r"[a-z]", password):
        score += 2
    if re.search(r"\d", password):
        score += 2
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 3
    if not re.search(r"(.)\1{2,}", password):
        score += 1
    return score

def evaluate_password():
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    score = score_password(password)
    feedback = []

    if len(password) < 8:
        feedback.append("Password should be at least 8 characters long.")
    if not re.search(r"[A-Z]", password):
        feedback.append("Password should contain uppercase letters.")
    if not re.search(r"[a-z]", password):
        feedback.append("Password should contain lowercase letters.")
    if not re.search(r"\d", password):
        feedback.append("Password should contain digits.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        feedback.append("Password should contain special characters.")
    if re.search(r"(.)\1{2,}", password):
        feedback.append("Password should not have consecutive characters.")

    strength_text.configure(state="normal")
    strength_text.delete("1.0", tk.END)

    if password != confirm_password:
        strength_text.insert(tk.END, "Passwords do not match. Please retype the password.")
    elif feedback:
        strength_text.insert(tk.END, "Password is weak. Please consider the following:\n\n")
        for item in feedback:
            strength_text.insert(tk.END, "- " + item + "\n")
    else:
        strength_text.insert(tk.END, "Password is strong. Good job!")
        hash_value = hashlib.sha256(password.encode()).hexdigest()
        strength_text.insert(tk.END, "\nSHA-256 Hash: " + "\n" + hash_value)

    strength_text.configure(state="disabled")
    password_entry.delete(0, tk.END)
    confirm_password_entry.delete(0, tk.END)

# Create the GUI window
window = tk.Tk()
window.title("Password Strength Evaluator")
window.geometry("800x400")
window.config(bg=BG_COLOR)

password_label = tk.Label(window, text="Enter a password:", bg=BG_COLOR, fg=FG_COLOR, font=("Arial", 22))
password_label.pack()
password_entry = tk.Entry(window, show="*", bg=BG_COLOR, fg=FG_COLOR, font=("Arial", 16))
password_entry.pack()
tk.Label(window, text="", bg=BG_COLOR).pack()

confirm_password_label = tk.Label(window, text="Confirm password:", bg=BG_COLOR, fg=FG_COLOR, font=("Arial", 22))
confirm_password_label.pack()
confirm_password_entry = tk.Entry(window, show="*", bg=BG_COLOR, fg=FG_COLOR, font=("Arial", 16))
confirm_password_entry.pack()
tk.Label(window, text="", bg=BG_COLOR).pack()

evaluate_button = tk.Button(window, text="Evaluate", command=evaluate_password, bg=BG_COLOR, fg=FG_COLOR)
evaluate_button.pack()

strength_text = tk.Text(window, height=10, width=64, bg=BG_COLOR, fg=FG_COLOR)
strength_text.pack()

window.mainloop()
