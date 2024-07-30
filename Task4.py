import tkinter as tk
from tkinter import ttk
import random

# Initialize counters for wins
user_wins = 0
computer_wins = 0
total_games = 0

def play_game(user_choice):
    global user_wins, computer_wins, total_games
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    user_choice_label.config(text=f"Your Choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's Choice: {computer_choice}")
    
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You Win!"
        user_wins += 1
    else:
        result = "You Lose!"
        computer_wins += 1
        
    total_games += 1
    result_label.config(text=result)
    user_wins_label.config(text=f"Your Wins: {user_wins}")
    computer_wins_label.config(text=f"Computer's Wins: {computer_wins}")
    
    if total_games == 10:
        if user_wins > computer_wins:
            final_result = "You are the overall winner!"
        elif computer_wins > user_wins:
            final_result = "The computer is the overall winner!"
        else:
            final_result = "It's an overall tie!"
        final_result_label.config(text=final_result)

def reset_game():
    global user_wins, computer_wins, total_games
    user_wins = 0
    computer_wins = 0
    total_games = 0
    user_choice_label.config(text="Your Choice: ")
    computer_choice_label.config(text="Computer's Choice: ")
    result_label.config(text="")
    user_wins_label.config(text="Your Wins: 0")
    computer_wins_label.config(text="Computer's Wins: 0")
    final_result_label.config(text="")

# Initialize the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x400")

# Optional: Using ttk for better styling
style = ttk.Style(root)
style.configure('TButton', font=('Helvetica', 12))
style.configure('TLabel', font=('Helvetica', 12))

# Title label
title_label = ttk.Label(root, text="Rock-Paper-Scissors", font=('Helvetica', 16))
title_label.pack(pady=10)

# Label to display choices
user_choice_label = ttk.Label(root, text="Your Choice: ", font=('Helvetica', 14))
user_choice_label.pack(pady=5)

computer_choice_label = ttk.Label(root, text="Computer's Choice: ", font=('Helvetica', 14))
computer_choice_label.pack(pady=5)

# Label to display result
result_label = ttk.Label(root, text="", font=('Helvetica', 14))
result_label.pack(pady=20)

# Label to display win counts
user_wins_label = ttk.Label(root, text="Your Wins: 0", font=('Helvetica', 14))
user_wins_label.pack(pady=5)

computer_wins_label = ttk.Label(root, text="Computer's Wins: 0", font=('Helvetica', 14))
computer_wins_label.pack(pady=5)

# Label to display final result
final_result_label = ttk.Label(root, text="", font=('Helvetica', 14))
final_result_label.pack(pady=10)

# Frame to hold buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Buttons for Rock, Paper, Scissors
rock_button = ttk.Button(button_frame, text="Rock", command=lambda: play_game('Rock'))
rock_button.grid(row=0, column=0, padx=5, pady=5)

paper_button = ttk.Button(button_frame, text="Paper", command=lambda: play_game('Paper'))
paper_button.grid(row=0, column=1, padx=5, pady=5)

scissors_button = ttk.Button(button_frame, text="Scissors", command=lambda: play_game('Scissors'))
scissors_button.grid(row=0, column=2, padx=5, pady=5)

# Reset button
reset_button = ttk.Button(root, text="Reset Game", command=reset_game)
reset_button.pack(pady=10)

# Customize colors (optional)
root.configure(bg='lightblue')
title_label.configure(background='lightblue', foreground='darkblue')
user_choice_label.configure(background='lightblue', foreground='darkblue')
computer_choice_label.configure(background='lightblue', foreground='darkblue')
result_label.configure(background='lightblue', foreground='darkblue')
user_wins_label.configure(background='lightblue', foreground='darkblue')
computer_wins_label.configure(background='lightblue', foreground='darkblue')
final_result_label.configure(background='lightblue', foreground='darkblue')
button_frame.configure(background='lightblue')

# Pack and display the main window
root.mainloop()
