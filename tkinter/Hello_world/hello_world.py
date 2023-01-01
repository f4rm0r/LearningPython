import tkinter as tk

root = tk.Tk()

# Changing window size and location to be in the middle.
window_width = 300
window_height = 200

# Get screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# Set the position of the window to the center of the screen.
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Set title on root window.
root.title("Tkinter test")

# Getting title on window.
title = root.title()

# Place a label on the root window.
message = tk.Label(root, text=f"{title}")
message.pack()

# Trying to load dpi awareness dll file on windows.
try:
    from ctypes import windll

    #windll.shcore.SetProcessDpiAwareness(1)
finally:
# Keep the window open and visible.
    root.mainloop()