from Humber_TkinterApp import TkinterApp
import tkinter as tk
from tkinter import messagebox

"""
Developer Name: Team4 developers
Edited on: 14-April-2024
Method Name: main()
Method Description: main() method is the starting point of this application and will call Humber_TkinterApp.
Creates and configures the main Tkinter window, initializes the application, and starts the event loop.
"""
def main():
    root = tk.Tk()
    
    # Set initial window size
    root.geometry("830x550")

    # set minimum window size value
    root.minsize(830, 550)
 
    # set maximum window size value
    root.maxsize(830, 550)
    
    # Initialize the application
    app = TkinterApp(root)

     # Start the event loop
    root.mainloop()

if __name__ == "__main__":
    main()
