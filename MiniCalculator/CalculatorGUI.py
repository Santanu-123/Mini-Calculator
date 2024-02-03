# It is a mini calculator. So, do only one operation at a time ( if addition, so only addition and so on ... )

import time
import tkinter as tk
import re

font = "Times new Roman", 13, "bold"
root = tk.Tk()
root.title("Mini Calculator")
root.geometry("+500+200")
root.minsize(300, 300)
root.resizable(False, False)
root.config(bg="grey33")


def clickedNumber(number):
    currNum = outputLabel["text"]
    outputLabel.config(text=currNum + str(number))


def clearMethod():
    outputLabel.config(text="")


def backspaceMethod():
    currNum = outputLabel["text"]
    outputLabel.config(text=currNum[:-1])


def equalsMethod():
    string1 = outputLabel["text"]
    splitters = ["+", "-", "*", "/"]
    pattern = "|".join(map(re.escape, splitters))
    result = re.split(pattern, string1)
    result = [item.strip() for item in result if item.strip()]

    if splitters[0] in string1:
        newResult = 0
        for res in range(len(result)):
            newResult += int(result[res])
        outputLabel.config(text=newResult)
        root.update()
        time.sleep(2)
        clearMethod()

    if splitters[1] in string1:
        newResult = 0
        for res in range(len(result)):
            newResult = int(result[0])
            newResult -= int(result[res])
        outputLabel.config(text=newResult)
        root.update()
        time.sleep(2)
        clearMethod()

    if splitters[2] in string1:
        newResult = 0
        for res in range(len(result)):
            newResult = int(result[0])
            newResult *= int(result[res])
        outputLabel.config(text=newResult)
        root.update()
        time.sleep(2)
        clearMethod()

    if splitters[3] in string1:
        newResult = 0
        for res in range(len(result)):
            newResult = int(result[0])
            newResult /= int(result[res])
        outputLabel.config(text=newResult)
        root.update()
        time.sleep(2)
        clearMethod()


def close():
    root.destroy()


# Output screen
outputLabel = tk.Label(root, highlightthickness=1, highlightbackground="black", bg="white")
outputLabel.place(relx=0.01, rely=0.02, relheight=0.15, relwidth=0.98)
outputLabel.config(font=font)

# All buttons for calculator
num1 = tk.Button(root, text=1, highlightthickness=1, highlightbackground="black",
                 bg="white", font=font, command=lambda: clickedNumber(num1["text"]))
num1.place(relx=0.01, rely=0.19, relheight=0.142, relwidth=0.16)
num2 = tk.Button(root, text=2, highlightthickness=1, highlightbackground="black",
                 bg="white", font=font, command=lambda: clickedNumber(num2["text"]))
num2.place(relx=0.18, rely=0.19, relheight=0.142, relwidth=0.16)
num3 = tk.Button(root, text=3, highlightthickness=1, highlightbackground="black",
                 bg="white", font=font, command=lambda: clickedNumber(num3["text"]))
num3.place(relx=0.35, rely=0.19, relheight=0.142, relwidth=0.16)
plus = tk.Button(root, text="+", highlightthickness=1, highlightbackground="black",
                 bg="burlywood2", font=font, command=lambda: clickedNumber(plus["text"]))
plus.place(relx=0.66, rely=0.19, relheight=0.142, relwidth=0.16)
minus = tk.Button(root, text="-", highlightthickness=1, highlightbackground="black",
                  bg="burlywood2", font=font, command=lambda: clickedNumber(minus["text"]))
minus.place(relx=0.83, rely=0.19, relheight=0.142, relwidth=0.16)

num4 = tk.Button(root, text=4, highlightthickness=1, highlightbackground="black",
                 bg="white", font=font, command=lambda: clickedNumber(num4["text"]))
num4.place(relx=0.01, rely=0.342, relheight=0.142, relwidth=0.16)
num5 = tk.Button(root, text=5, highlightthickness=1, highlightbackground="black",
                 bg="white", font=font, command=lambda: clickedNumber(num5["text"]))
num5.place(relx=0.18, rely=0.342, relheight=0.142, relwidth=0.16)
num6 = tk.Button(root, text=6, highlightthickness=1, highlightbackground="black",
                 bg="white", font=font, command=lambda: clickedNumber(num6["text"]))
num6.place(relx=0.35, rely=0.342, relheight=0.142, relwidth=0.16)
multi = tk.Button(root, text="*", highlightthickness=1, highlightbackground="black",
                  bg="burlywood2", font=font, command=lambda: clickedNumber(multi["text"]))
multi.place(relx=0.66, rely=0.342, relheight=0.142, relwidth=0.16)
div = tk.Button(root, text="/", highlightthickness=1, highlightbackground="black",
                bg="burlywood2", font=font, command=lambda: clickedNumber(div["text"]))
div.place(relx=0.83, rely=0.342, relheight=0.142, relwidth=0.16)

num7 = tk.Button(root, text=7, highlightthickness=1, highlightbackground="black",
                 bg="white", font=font, command=lambda: clickedNumber(num7["text"]))
num7.place(relx=0.01, rely=0.494, relheight=0.142, relwidth=0.16)
num8 = tk.Button(root, text=8, highlightthickness=1, highlightbackground="black",
                 bg="white", font=font, command=lambda: clickedNumber(num8["text"]))
num8.place(relx=0.18, rely=0.494, relheight=0.142, relwidth=0.16)
num9 = tk.Button(root, text=9, highlightthickness=1, highlightbackground="black",
                 bg="white", font=font, command=lambda: clickedNumber(num9["text"]))
num9.place(relx=0.35, rely=0.494, relheight=0.142, relwidth=0.16)

num = tk.Button(root, text=0, highlightthickness=1, highlightbackground="black",
                bg="white", font=font, command=lambda: clickedNumber(num["text"]))
num.place(relx=0.18, rely=0.647, relheight=0.142, relwidth=0.16)
doubleZero = tk.Button(root, text="00", highlightthickness=1, highlightbackground="black",
                       bg="white", font=font, command=lambda: clickedNumber(doubleZero["text"]))
doubleZero.place(relx=0.35, rely=0.647, relheight=0.142, relwidth=0.16, )

clear = tk.Button(root, text="AC", highlightthickness=1, highlightbackground="black",
                  bg="burlywood2", font=font, command=clearMethod)
clear.place(relx=0.01, rely=0.647, relheight=0.142, relwidth=0.16)
backspace = tk.Button(root, text="←", highlightthickness=1, highlightbackground="black",
                      bg="burlywood2", font=font, command=backspaceMethod)
backspace.place(relx=0.66, rely=0.494, relheight=0.142, relwidth=0.326)
dot = tk.Button(root, text="=", highlightthickness=1, highlightbackground="black",
                bg="burlywood2", font=font, command=equalsMethod)
dot.place(relx=0.66, rely=0.647, relheight=0.142, relwidth=0.326)

# close button
closeButton = tk.Button(root, text="Close", highlightthickness=1, fg="white",
                        highlightbackground="black", bg="Green", command=close, font=font)
closeButton.place(relx=0.01, rely=0.84, relheight=0.14, relwidth=0.98)

if __name__ == "__main__":
    root.mainloop()
