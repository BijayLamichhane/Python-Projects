import json
import os
from dotenv import load_dotenv
import requests
import win32com.client as wincl

load_dotenv()
api_key = os.getenv("API_KEY")

city = input("Enter the city name: ")

url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

r = requests.post(url)
# print(r.text)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
l = wdic["current"]["last_updated"]
wind = wdic["current"]["wind_kph"]
h = wdic["current"]["humidity"]

speaker_number = 1
spk = wincl.Dispatch("SAPI.SpVoice")
vcs = spk.GetVoices()
SVSFlag = 11
spk.Voice
spk.SetVoice(vcs.Item(speaker_number))
spk.Speak(f"The Current Weather in {city} is {w} degrees. Current wind speed is {wind} kilometer per hour and humidity is {h}")
spk.Speak(f"It was last updated in {l}")