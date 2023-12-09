import tkinter as tk
import tkinter.ttk as ttk
import sys
import os
import tkinter.font as tkFont


def close():
    root.quit()


def run_project1():
    os.system("python project1.py")


def run_project2():
    os.system("python project2.py")


def run_project6():
    os.system("python project6.py")


class NewprojectApp:
    def __init__(self, master=None):
        # build ui
        frame1 = ttk.Frame(master)
        frame1.configure(height=200, padding=150, width=200)

        self.welcome = ttk.Label(frame1)
        self.welcome.configure(
            cursor="arrow",
            font="{@Microsoft YaHei UI} 15 {bold}",
            takefocus=True,
            text="Welcome to LASSP. Pick a project: ",
            foreground="RED",
        )
        self.welcome.grid(column=0, row=0)

        style = ttk.Style()
        bold_font = tkFont.Font(family="Helvetica", size=13, weight="bold")
        style.configure(
            "Green.TButton", foreground="Green", background="White", font=bold_font
        )
        self.project1 = ttk.Button(frame1, text="Project 1", style="Green.TButton")
        self.project1.grid(column=0, row=1)
        self.project1.configure(command=run_project1)

        self.project2 = ttk.Button(frame1, text="Project 2", style="Green.TButton")
        self.project2.configure(text="Project 2")
        self.project2.grid(column=0, row=2)
        self.project2.configure(command=run_project2)

        self.project3 = ttk.Button(frame1, text="Project 3", style="Green.TButton")
        self.project3.configure(text="Project 3")
        self.project3.grid(column=0, row=3)

        self.project4 = ttk.Button(frame1, text="Project 4", style="Green.TButton")
        self.project4.configure(text="Project 4")
        self.project4.grid(column=0, row=4)

        self.project5 = ttk.Button(frame1, text="Project 5", style="Green.TButton")
        self.project5.configure(text="Project 5")
        self.project5.grid(column=0, row=5)

        self.project6 = ttk.Button(frame1, text="Project 6", style="Green.TButton")
        self.project6.configure(text="Project 6")
        self.project6.grid(column=0, row=6)
        self.project6.configure(command=run_project6)

        button7 = ttk.Button(frame1, text="Quit", style="Green.TButton")
        button7.configure(text="Quit")
        button7.grid(column=0, row=7)
        button7.configure(command=close)

        frame1.pack(side="top")
        frame1.bind("<Button>", self.callback, add="")

        # Main widget
        self.mainwindow = frame1

    def run(self):
        self.mainwindow.mainloop()

    def callback(self, event=None):
        pass

    def close(self):
        self.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = NewprojectApp(root)
    app.run()
