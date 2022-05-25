
import tkinter as tk

frame = tk.Tk()
frame.title("Text counter")
frame.geometry('400x200')

  
def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "Words "+str(len(inp.split())))

def letterInput():
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "Characters "+str(len(inp)))
  

inputtxt = tk.Text(frame, height = 5, width = 20)
  
inputtxt.pack()
  

printButton = tk.Button(frame,text = "Check how many words are there:", command = printInput)
printButton.pack()
letterButton = tk.Button(frame,text ="check how many letters are there:",command = letterInput)
letterButton.pack()

lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()
