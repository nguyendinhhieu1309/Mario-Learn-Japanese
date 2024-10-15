import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import sys

def launch_game1():
    subprocess.Popen([sys.executable, "alphabet.py"])
    root.destroy()

def launch_game2():
    subprocess.Popen([sys.executable, "vocarb.py"])
    root.destroy()

root = tk.Tk()
root.title("Mario Learn Japanese")
root.geometry("500x400")

# Load the background image
background_image = Image.open("assets/background_1.png")
background_photo = ImageTk.PhotoImage(background_image)

# Create a canvas and set the background image
canvas = tk.Canvas(root, width=500, height=400)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_photo, anchor="nw")

# Create widgets
label = tk.Label(root, text="Select a game to play:", font=("Arial", 14), bg="white")
game1_button = tk.Button(root, text="Alphabet", command=launch_game1, width=20, height=2)
game2_button = tk.Button(root, text="Vocarb", command=launch_game2, width=20, height=2)

# Add widgets to the canvas
canvas.create_window(250, 50, window=label)
canvas.create_window(250, 150, window=game1_button)
canvas.create_window(250, 200, window=game2_button)

root.mainloop()
