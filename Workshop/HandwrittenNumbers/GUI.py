import tkinter as tk
from PIL import ImageTk,Image,ImageDraw
import numpy as np
import cv2
import joblib
count=0
model=joblib.load("/Users/mac/Desktop/Simple DSP/Workshop/HandwrittenNumbers/KNN_model.sav")

def eventFunction(event):
   x=event.x
   y=event.y
   fat=25

   x1=x-fat
   y1=y-fat
   x2=x+fat
   y2=y+fat

   canvas.create_oval((x1,y1,x2,y2),fill="black")
   imgDraw.ellipse((x1,y1,x2,y2),fill="white")

def save():
   global count

   imgArray=np.array(img)
   imgArray=cv2.resize(imgArray,(8,8))
   print(imgArray)
   if not cv2.imwrite("/Users/mac/Desktop/Simple DSP/Workshop/HandwrittenNumbers/data/"+str(count)+".jpg",imgArray):
      raise Exception("Error Writing Image")
   count+=1

def clear():
   global img,imgDraw

   canvas.delete("all")
   img=Image.new("RGB",(w,h),(0,0,0))
   imgDraw=ImageDraw.Draw(img)

def predict():
   global img
   print(img)
   imgArray=np.array(img)
   # print(imgArray)
   imgArray=cv2.cvtColor(imgArray,cv2.COLOR_RGB2GRAY)
   imgArray=cv2.resize(imgArray,(8,8))
   imgArray=np.reshape(imgArray,(1,64))
   print(imgArray)
   imgArray=(imgArray/255)*16
   # print(imgArray)
   result=model.predict(imgArray)
   labelStatus.config(text="PREDICTED DIGIT"+str(result))
   

#Main Window
win=tk.Tk()
w,h=300,300
f="Helvetica 20 bold"
f_label="Helvetica 24 bold"

canvas=tk.Canvas(win,width=w,height=h,bg="White")
canvas.grid(row=0,column=0,columnspan=4)

buttonSave=tk.Button(win,text="SAVE",bg="pink",fg="white",font=f,command=save)
buttonSave.grid(row=1,column=0)

buttonSave=tk.Button(win,text="PREDICT",bg="blue",fg="White",font=f,command=predict)
buttonSave.grid(row=1,column=1)

buttonSave=tk.Button(win,text="CLEAR",bg="gold",fg="White",font=f,command=clear)
buttonSave.grid(row=1,column=2)

buttonSave=tk.Button(win,text="EXIT",bg="red",fg="White",font=f)
buttonSave.grid(row=1,column=3)

labelStatus=tk.Label(win,text="PREDICTED DIGIT: NONE",bg="white",fg="black",font=f_label)
labelStatus.grid(row=2,column=0,columnspan=4)

canvas.bind("<B1-Motion>",eventFunction)
img=Image.new("RGB",(w,h),(0,0,0))
imgDraw=ImageDraw.Draw(img)

win.mainloop()
