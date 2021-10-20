import eel
import pyowm

owm = pyowm.OWM("90cae8778a11ab0ad6c637a14a66a9d2")



@eel.expose
def get_weather(place):
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(city)
    w = observation.weather

    temp = w.temperature('celsius')['temp']

    return "В городе " + city + " сейчас " + str(temp) + " градусов!"

eel.init("web")
eel.start("main.html", size = (700,700))    