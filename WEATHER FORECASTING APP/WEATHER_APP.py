from tkinter import *
from tkinter import ttk
import requests

def data_get():
      city = city_name.get()
      data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=8c1b11c3df3e0320e7e39ee8ff91d844").json()
      w_label1.config(text=data["weather"][0]["main"])
      wb_label1.config(text=data["weather"][0]["description"])
      temp_label1.config(text=str(data["main"]["temp"]-273.15))
      per_label1.config(text=data["main"]["pressure"])
      
win = Tk()
win.title("WEATHER FORECASTING")
win.config(bg="lightseagreen")
win.geometry("550x550")

name_label = Label(win,text="WEATHER APP",font=("Algerian",35,"bold"))
name_label.place(x=30,y=40,height=50,width=450)

city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","Delhi","Puducherry"]
com = ttk.Combobox(win,text="WEATHER APP",values=list_name,font=("Castellar",15,"bold"),textvariable=city_name)
com.place(x=30,y=120,height=50,width=450)

w_label = Label(win,text="Weather Climate",font=("Felix Titling",10,))
w_label.place(x=25,y=260,height=50,width=210)
w_label1 = Label(win,text="",font=("Times New Roman",14,))
w_label1.place(x=250,y=260,height=50,width=210)

wb_label = Label(win,text="Weather Description",font=("Felix Titling",10,))
wb_label.place(x=25,y=330,height=50,width=210)
wb_label1 = Label(win,text="",font=("Times New Roman",14,))
wb_label1.place(x=250,y=330,height=50,width=210)

temp_label = Label(win,text="Temperature",font=("Felix Titling",10,))
temp_label.place(x=25,y=400,height=50,width=210)
temp_label1 = Label(win,text="", font=("Times New Roman",14,))
temp_label1.place(x=250,y=400,height=50,width=210)

per_label=Label(win,text="Pressure",font=("Felix Titling",10,))
per_label.place(x=25,y=470,height=50,width=210)
per_label1=Label(win,text="",font=("Times New Roman",14,))
per_label1.place(x=250,y=470,height=50,width=210)

done_button = Button(win,text="Done",font=("Algerian",20,"bold"),command=data_get)

done_button.place(y=190,height=50,width=100 ,x=200)


win.mainloop()