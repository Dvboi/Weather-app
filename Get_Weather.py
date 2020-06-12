from tkinter import *
from PIL import ImageTk,Image 
import requests
import json
from tkinter import messagebox

root = Tk()
root.title("Weather_App")
root.iconbitmap("cloud.ico")
#root.geometry("400x200")
root.configure(background = "light green")

#"http://api.openweathermap.org/data/2.5/weather?"

def clear_all():
	zip.delete(0,END)
	e1.delete(0,END)
	e2.delete(0,END)
	e3.delete(0,END)
	#shifting cursor back to the city input tab
	zip.focus_set()

def zipLookup():
	e1.delete(0,END)
	e2.delete(0,END)
	e3.delete(0,END)
	try:
		api = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+str(zip.get())+"&appid=e3b02ce18ed1d5654bb85feaa959e44f")
	except:
		messagebox.showwarning("Warning!","Make sure you're connected to the Internet")
		return
	api_content = json.loads(api.content)
	COD = api_content["cod"]
	if COD!="404":		
		z = api_content["weather"]
		Weather = z[0]["description"]
		Temperature = api_content["main"]["temp"]
		Humidity = api_content["main"]["humidity"]
	else:
		messagebox.showerror("Connectivity","City not found\nPlease enter a valid city name")
		zip.delete(0,END)
		return

	e1.insert(0,Weather)
	e2.insert(0,str(int(Temperature)-273)+"\u00B0"+"C")
	e3.insert(0,str(Humidity)+"%")


#Main
Label(root,text = "Enter City Name:",fg = "magenta",bg = "light green",font = ("Helvetica",12)).grid(row = 0,column = 0)
zip = Entry(root)
zip.grid(row = 0,column = 1,stick = W+E+N+S)
#find weather according to code button
zipButton = Button(root,text = "Lookup City",command = zipLookup,fg = "red",bg = "grey",activebackground = "yellow")
zipButton.grid(row = 1,column = 1,stick = W+E+N+S)

#Show retrieved information
Label(root,text ="Weather Type:",fg = "magenta",bg = "light green",font = ("Helvetica",12)).grid(row = 2,column = 0,sticky = "W")
Label(root,text ="Temperature:",fg = "magenta",bg = "light green",font = ("Helvetica",12)).grid(row = 3,column = 0,sticky = "W")
Label(root,text ="Humidity:",fg = "magenta",bg = "light green",font = ("Helvetica",12)).grid(row = 4,column = 0,sticky = "W")


e1 = Entry(root,relief = "raised")
e2 = Entry(root,relief = "raised")
e3 = Entry(root,relief = "raised")

e1.grid(row = 2,column = 1,ipadx = 50)
e2.grid(row = 3,column = 1,ipadx = 50)
e3.grid(row = 4,column = 1,ipadx = 50)

#Clear Button
Button(root,text = "Clear All",fg = "red",bg = "grey",command = clear_all).grid(row = 5,column = 1,sticky = W+E+N+S)

root.mainloop()