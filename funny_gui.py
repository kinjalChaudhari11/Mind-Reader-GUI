import tkinter as tk
from tkinter import messagebox
import time

def start_mind_reading():
    user_input = entry.get()
    
    try:
        number = float(user_input)  #float so we can also do decimals 
        if not (1 <= number <= 10):  
            raise ValueError  #make sure we only do numbers and that too 1-10
    except ValueError:
        messagebox.showerror("Your input can only be a number from 1-10")
        return
    
    #progress messages
    progress_messages = [
        "🧠Scanning brainwaves...",
        "🔍 Reading memories...",
        "📊 Calculating probabilities...",
        "🔢 Cross-referencing data..."
    ]
    
    
    button.config(state=tk.DISABLED) #button is disabled while processing 
    
    for msg in progress_messages:
        label.config(text=msg)
        root.update()
        #dramatic pauses
        time.sleep(1.5)  
    
    #tada 
    label.config(text=f"u chose {number:.2f}")

    
    button.config(state=tk.NORMAL) #button re enabled so we can play again




#application window 
root = tk.Tk()
root.title("wowowowooowowowwwwww Mind Reader")
root.geometry("400x250")


label = tk.Label(root, text="Think of a number from 1-10 and enter it below", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12), justify="center")
entry.pack(pady=5)

button = tk.Button(root, text="Read My Mind!", font=("Arial", 12), command=start_mind_reading)
button.pack(pady=10)

# Run the application
root.mainloop()
