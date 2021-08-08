import tkinter as tk
import requests
from tkinter import font

HEIGHT = 600
WIDTH = 600
SKY = '#80c1ff'


# eae839fcb7c625f500ec769515ec6bf8
# api.openweathermap.org/data/2.5/forecast?q={city name},{state code}&appid={API key}

def format_response(weather):
	try:
		name = weather['name']
		description = weather['weather'][0]['description']
		temperature = weather['main']['temp']

		final_str = 'City: %s \n Conditions: %s \n Temperature: %s' % (name, description, temperature)

	except:
		final_str = 'There was a problem retrieving that information'

	return final_str

def get_weather(city):
	weather_key = 'eae839fcb7c625f500ec769515ec6bf8'
	url = 'http://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
	response = requests.get(url, params= params )
	weather = response.json()

	label['text'] = format_response(weather)

root = tk.Tk()

#size of the window
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

#bg image
background_image = tk.PhotoImage(file = 'landscape.png')
background_label = tk.Label(root, image = background_image)
background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

#main frame with the label in it
frame = tk.Frame(root, bg = SKY, bd = 10)
frame.place(relx = 0.15, rely = 0.25, relwidth = 0.7, relheight = 0.6)

#frame with entry and button in it
skinnyframe = tk.Frame(root, bg = SKY, bd = 5)
skinnyframe.place(relx = 0.15, rely = 0.1, relwidth = 0.7, relheight = 0.08)

#for info
entry = tk.Entry(skinnyframe, bg = 'white')
entry.place(relwidth = 0.6, relheight = 1)

#for the button
button = tk.Button(skinnyframe, text = "Get Weather", fg = "black", bg = "white", command = lambda: get_weather(entry.get()))
button.place(relx = 0.69, relwidth = 0.3, relheight = 1)

#displays info
label = tk.Label(frame, font = ('Courier', 20), bg = 'white')
label.place(relwidth = 1, relheight = 1)

#end of Graphics User Interface (GUI)
root.mainloop()
