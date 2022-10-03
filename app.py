from msilib import datasizemask
from flask import Flask, current_app
import time, sys
from fhict_cb_01.CustomPymata4 import CustomPymata4

app = Flask(__name__)

# Constants

DHTPIN = 12
LDRPIN = 2

# Globals

humidity = 0
temperature = 0
brightness = 0

data = {
    'currentValue':0,
    'valueList':[],
    'averageValue':0
}

stats = {
    'humidity':data,
    'temperature':data,
    'brightness':data,
    'time':0
}

# def get_max_temp():
    

def measure(data):
    global humidity, temperature, stats
    t = time.localtime()
    currentTime = time.strftime("%H:%M:%S", t)
    
    if data[3] == 0:
        
        humidity = data[4]
        temperature = data[5]
        
# def avg_measure():

def measureLDR(data):
    global brightness
    brightness = data[2]
    
           
def store_values():
    global stats, data, brightness, humidity, temperature
    
    stats['brightness'][data]['currentValue'].append(brightness)
    stats['humidity'][data]['currentValue'].append(humidity)
    stats['temperature'][data]['currentValue'].append(temperature)
    

def setup():
    global board
    board = CustomPymata4(com_port="COM3")
    board.set_pin_mode_dht(DHTPIN, sensor_type=11, differential=.05, callback = measure)
    board.set_pin_mode_analog_input(LDRPIN, callback=measureLDR, differential=10)

setup()

@app.route('/')
def hello_world():
    return "<p>Hello, world!</p>"

@app.route('/')