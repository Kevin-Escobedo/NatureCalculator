#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com
import vc_natures
import tkinter
import sys
import os

class Interface:
    def __init__(self):
        self.root_window = tkinter.Tk()
        self.root_window.geometry("300x100")
        self.root_window.iconbitmap(self.resource_path("pokeball.ico"))
        self.root_window.resizable(False, False)
        self.root_window.title("VC Nature Calculator")
        self.EXP = tkinter.Entry(self.root_window, width = 39)
        self.result = tkinter.StringVar()
        self.nature_result = ""

    def resource_path(self, relative_path):
        '''Get absolute path to resource, works for dev and for PyInstaller'''
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def get_exp(self):
        try:
            exp = int(self.EXP.get())
            if exp < 0:
                raise ValueError
            return exp
        except ValueError:
            self.result.set("Invalid EXP")


    def calculate_nature(self):
        try:
            experience = self.get_exp()
            self.nature_result = vc_natures.calculate_nature(experience)
            self.result.set("{} Nature".format(self.nature_result))
        except TypeError:
            pass

    def key(self, event):
        '''Handles key input'''
        if event.keysym == "Return":
            self.calculate_nature()

    def run(self):
        '''Runs the GUI'''
        tkinter.Label(self.root_window, text = "Enter EXP").grid(row=0, column=0)
        self.EXP.grid(row=0, column=1)

        calculate_button = tkinter.Button(self.root_window, text = "Calculate", command = self.calculate_nature)
        calculate_button.grid(row = 1, column = 1)

        
        tkinter.Label(self.root_window, textvariable = self.result).grid(row = 2, column = 1)
        self.result.set("{}".format(self.nature_result))

        self.root_window.bind("<KeyPress>", self.key)

        self.root_window.mainloop()

if __name__ == "__main__":
    Interface().run()
