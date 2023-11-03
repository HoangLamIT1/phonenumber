import tkinter
import os
import tkintermapview
import phonenumbers
import opencage

from key import key
from phonenumbers import geocoder
from phonenumbers import carrier

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

from opencage.geocoder import OpenCageGeocode

root = tkinter.Tk()
root.geometry("700x700")

label1 = Label(text="Get address with phonenumbers")
label1.pack()

def getResult():
    num = number.get("1.0", END)
    try:
        num1 = phonenumbers.parse(num)
    except:
        messagebox.showerror("Lỗi !", "Số điện thoại này không tồn tại, hãy kiểm tra lại")
    localtion = geocoder.description_for_number(num1, "vi")
    service_provider = carrier.name_for_number(num1, "vi")
    ocg = OpenCageGeocode(key)
    query = str(localtion)
    results = ocg.geocode(query)
    
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    
    my_label = LabelFrame(root)
    my_label.pack(pady=20)
    
    map_widget = tkintermapview.TkinterMapView(my_label, width=450, height=450, corner_radius=0)
    map_widget.set_position(lat,lng)
    map_widget.set_marker(lat, lng, text = "Victim")
    map_widget.set_zoom(10)
    map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    map_widget.pack()
    
    
    adr = tkintermapview.convert_coordinates_to_address(lat,lng)
    result.insert(END, "\n")
    result.insert(END, "\nWARNING ! Kết quả có thể không đúng 100%")
    result.insert(END, "\n-----------------------------------------")
    result.insert(END, "\nQuốc gia: " + localtion)
    result.insert(END, "\nNhà mạng: " + service_provider)
    result.insert(END,"\nVĩ độ : " + str(lat))
    result.insert(END, "\nKinh Độ : " + str(lng))
    result.insert(END, "\nĐường (Street): " + adr.street)
    result.insert(END, "\nThành Phố (City): " + adr.city)
    result.insert(END, "\nPostcode: " + adr.postal)

number = Text(height=1)
number.pack()

style = Style()
style.configure("TButton", font=('calibri',20,'bold'),borderwidth='20')
style.map('TButton', foreground = [('active', '!disabled', 'green')],
                     background = [('active','black')])

button = Button(text="Search", command=getResult)
button.pack(pady = 10, padx = 100)

result = Text(height=7)
result.pack()

root.mainloop()
