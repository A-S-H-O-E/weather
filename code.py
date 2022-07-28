from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk,Image
import requests
import os
os.system('cls')
root = Tk()
root.title('Weather App')
root.geometry('500x300')
root.configure(background = 'lightblue')
def findwther():
    city =  citytxt.get()
    link = 'https://fcc-weather-api.glitch.me/api/current?lat=35&lon=139'
    response = requests.get(link)
    data = response.json()
    tmperture['text'] = '{} °C'.format(data['main']['temp'])
    tmperture.place(x = 205, y = 240)
title = Label(root,text = 'Weather App',font = ('bold',15))
title.place(x = 181, y = 30)
cityl = Label(root,text = 'Enter City Name',font = ('bold',15))
cityl.place(x = 175, y = 100)
citytxt = StringVar()
citye = Entry(root,textvariable = citytxt)
citye.place(x=185, y = 140)
gobttn = Button(root,text = 'Search',width=12,command = findwther)
gobttn.place(x = 205, y = 175)
tmperture = Label(root,text = '',font = ('bold',15))
root.mainloop()
