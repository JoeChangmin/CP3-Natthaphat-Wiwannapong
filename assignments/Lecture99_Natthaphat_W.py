from tkinter import *
import math

def leftClickButton(event):
    print(float(textBoxWeight.get())/(math.pow(float(textBoxHight.get())/100,2)))
    result = float(textBoxWeight.get())/(math.pow(float(textBoxHight.get())/100,2))
    textResult = ""
    if result > 30:
        textResult = "อ้วนมาก"
    elif result >= 25:
        textResult = "อ้วน"
    elif result >= 23:
        textResult = "น้ำหนักเกิน"
    elif result >= 18.6:
        textResult = "น้ำหนักปรกติ เหมาะสม"
    elif result < 18.5:
        textResult = "ผมเกินไป"

    lableResult.config(text=textResult)
    lableBMI.config(text=result)

MainWindow = Tk()
lableHight = Label(MainWindow, text="ส่วนสูง (cm.)")
lableHight.grid(row=0,column=0)

textBoxHight = Entry(MainWindow)
print("textBoxHeight =",textBoxHight.get())
textBoxHight.grid(row=0,column=1)

lableWeight = Label(MainWindow, text="น้ำหนัก (Kg.)")
lableWeight.grid(row=1,column=0)

textBoxWeight = Entry(MainWindow)
print("textBoxWeight = ",textBoxWeight.get())
textBoxWeight.grid(row=1,column=1)

button = Button(MainWindow,text = "คำนวณ")
button.bind('<Button-1>',leftClickButton)
button.grid(row=2,column=0)

lableResult = Label(MainWindow, text="ผลลัพธ์")
lableResult.grid(row=2,column=1)

lableBMI = Label(MainWindow, text="BMI")
lableBMI.grid(row=3,column=1)

MainWindow.mainloop()
