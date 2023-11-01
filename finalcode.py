import machine
import urequests
import time
from machine import Pin, I2C

# Initialize I2C for LCD
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
lcd = I2C_LCD1602(i2c, 2, 16)  # Replace I2C_LCD1602 with your LCD library

# Pin configuration
SENSOR_PIN = 0
PIN_QUIET = Pin(0, Pin.OUT)
PIN_MODERATE = Pin(2, Pin.OUT)
PIN_LOUD = Pin(14, Pin.OUT)

# Network configuration
SSID = "kiran"  # Replace with your Wi-Fi SSID
PASSWORD = "12345678"  # Replace with your Wi-Fi password
API_KEY = "A2L4O6NCDAE49T3B"  # Replace with your ThingSpeak API key

# Blynk configuration
BLYNK_AUTH = "2NauRnAmwHgKSSfVXrpssR8Ud8Jvk2lZ"  # Replace with your Blynk authentication token

# ThingSpeak server
THINGSPEAK_SERVER = "api.thingspeak.com"
THINGSPEAK_PORT = 80

# Sample window width in ms (50 ms = 20 Hz)
SAMPLE_WINDOW = 50

db = 0
sample = 0

# Function to connect to Wi-Fi
def connect_wifi():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to WiFi...")
        wlan.connect(SSID, PASSWORD)
        while not wlan.isconnected():
            pass
    print("WiFi connected!")

# Function to post data to ThingSpeak
def post_to_thingspeak(data):
    url = "http://{}:{}/update?api_key={}&field1={}".format(
        THINGSPEAK_SERVER, THINGSPEAK_PORT, API_KEY, data
    )
    response = urequests.get(url)
    response.close()

# Function to read sensor data
def read_sensor_data():
    global sample, db
    start_millis = time.ticks_ms()  # Start of sample window
    peak_to_peak = 0  # Peak-to-peak level
    signal_max = 0  # Minimum value
    signal_min = 1024  # Maximum value

    # Collect data for SAMPLE_WINDOW ms
    while time.ticks_diff(time.ticks_ms(), start_millis) < SAMPLE_WINDOW:
        sample = machine.ADC(SENSOR_PIN).read()
        if sample < 1024:
            if sample > signal_max:
                signal_max = sample
            elif sample < signal_min:
                signal_min = sample

    peak_to_peak = signal_max - signal_min
    db = (peak_to_peak - 20) / 8  # Calibrate for decibels

# Main program
connect_wifi()
while True:
    read_sensor_data()
    lcd.clear()
    lcd.setCursor(0, 0)
    lcd.print("Loudness: {} dB".format(db))
    
    if db <= 55:
        lcd.setCursor(0, 1)
        lcd.print("Level: Quiet")
        PIN_QUIET.value(1)
        PIN_MODERATE.value(0)
        PIN_LOUD.value(0)
    elif 55 < db < 85:
        lcd.setCursor(0, 1)
        lcd.print("Level: Moderate")
        PIN_QUIET.value(0)
        PIN_MODERATE.value(1)
        PIN_LOUD.value(0)
        # Notify for moderate noise
    elif db >= 85:
        lcd.setCursor(0, 1)
        lcd.print("Level: High")
        PIN_QUIET.value(0)
        PIN_MODERATE.value(0)
        PIN_LOUD.value(1)
        # Notify for high noise
    post_to_thingspeak(db)
    time.sleep(15)
