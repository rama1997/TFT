import tkinter as tk
from tkinter import ttk

class GUI:
    def __init__(self,text_queue):
        self.text_queue = text_queue

        # Main GUI Window
        self.root = tk.Tk()
        self.root.title('TFT HELPER GUI Demo')
        self.root.geometry('1920x1080')
        self.root.resizable(False, False)
        self.root.config(bg='#000000')
        # Makes main gui window fullscreen, stays on top of all windows, and transparent outside of widgets
        self.root.attributes("-fullscreen", 1,'-transparentcolor', '#000000', '-topmost', 1)
        # Makes GUI uncloseable using "regular" means
        self.root.overrideredirect(True) 

        # Console widget
        self.console = tk.Text(width=100, height=40,state= "disabled", bg = "grey",)
        self.console.pack()
        self.consoleState = 1

        # Activate Button, toggles console on and off
        self.activate = tk.Button(text="TFT", width=15, height=3, bg="white", fg="black", command =  lambda:self.toogleConsole())
        self.activate.place(x=20, y=25)

        # Exit button to close gui
        self.exit = tk.Button(text="Exit", width=15, height=5, bg="white", fg="black",command = self.root.destroy)
        self.exit.pack()
        
    # Print to console if there is text in the queue to print
    def updateConsole(self):
        if self.text_queue.empty() is False:
            text = self.text_queue.get()

            # Gets number of lines
            numlines = int(self.console.index('end - 1 line').split('.')[0])

            # Have to enable state in order to make changes
            self.console.config(state= "normal")

            # Deletes top line if there are too many lines
            if numlines==40: 
                self.console.delete(1.0, 2.0)
        
            # Add new line character if line is not empty
            if self.console.index('end-1c')!='1.0': 
                self.console.insert('end', '\n')
            
            # Add new text to console
            self.console.insert('end', text)

            # Disable to avoid making more changes
            self.console.config(state= "disabled")

        # Continous runs itself to update console every second
        self.root.after(ms=1, func=self.updateConsole)

    # Toogle GUI on and off
    def toogleConsole(self):
        if self.consoleState == 0:
            self.console.pack()
            self.consoleState = 1
        else:
            self.console.pack_forget()
            self.consoleState = 0

    def startGUI(self):
        self.updateConsole()
        self.root.mainloop()


