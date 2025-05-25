import tkinter as tk
from tkinter import ttk

def HandleBtnClick (ClickedBtnTxt):
    CurrentText = ResultVar.get()

    if ClickedBtnTxt == "=":
        try:
            #replace custom python symbols
            expression = CurrentText.replace("÷","/").replace ("x","*")
            result = eval(expression)

            #check if result is Whole
            if isinstance(result, float) and result.is_integer():
                result = int(result)

            ResultVar.set(result)
        except Exception as e: 
            print(f"Error occurred: {e}")
            ResultVar.set("error")

    #Clear when error is present and next button is clicked
    elif ResultVar.get() == "error":
            ResultVar.set(ClickedBtnTxt)
    #clear
    elif ClickedBtnTxt == "C":
            ResultVar.set("")

    #Convert to decimal
    elif ClickedBtnTxt == "%":
         try:
              CurrentNum = float (CurrentText)
              ResultVar.set (CurrentNum / 100)
         except ValueError:
              ResultVar.set("Error")

    #convert to negative
    elif ClickedBtnTxt == ("±"):
         try:
              CurrentNum = float(CurrentText)
              ResultVar.set (-CurrentNum)
         except ValueError:
              ResultVar.set("error")
    else:
            ResultVar.set(CurrentText+ClickedBtnTxt)

#Main Window
root = tk.Tk()
root.title("Calculator")

#output
ResultVar = tk.StringVar()
root.title("Calculator")
ResultVar = tk.StringVar()
ResultEntry = ttk.Entry(root, textvariable=ResultVar,
font= ("Helvetica",24), justify="right")
ResultEntry.grid(row=0,column=0, columnspan=4,
sticky="nsew")
#Button layout
Buttons = [
        ("C", 1, 0), ("±", 1, 1), ("%", 1, 2), ("÷", 1, 3),
        ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("x", 2, 3),
        ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
        ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
        ("0", 5, 0, 2), (".", 5, 2), ("=", 5, 3)
]
#configure style
style = ttk.Style()
style.theme_use('default')
style.configure("Tbutton", font = ("Helvetica", 16), width = 10, heighth=4)

#Create buttons
for BtnInfo in Buttons:
    BtnTxt,row,col = BtnInfo[:3]
    colspan =  BtnInfo[3] if len(BtnInfo) > 3 else 1
    Button = ttk.Button(root, text = BtnTxt, 
                        command = lambda text = BtnTxt: HandleBtnClick(text),
                        style="TButton")
    Button.grid(row=row, column=col, columnspan=colspan,
                sticky="nsew", ipadx=10, ipady=4, padx=5, pady=5)
#grid weight
for i in range(6):
    root.grid_rowconfigure(i,weight=1)

for i in range(4):
    root.grid_columnconfigure(i, weight =1)

#window size
width = 500
height=700
root.geometry(f"{width}x{height}")

#window resizeable?
root.resizable(True, True)

#keyboard controls
root.bind("<Return>", lambda _: HandleBtnClick("="))
root.bind("<BackSpace>", lambda _: HandleBtnClick("C"))

#Run
root.mainloop()
