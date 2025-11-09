# 🌤️ Weather Station

## 🎯 Purpose

This weather station measures temperature, humidity, and air pressure using a BME280 sensor and displays the readings on a 4-digit display. It's a fun way to learn about weather and how sensors work!

## ✨ What It Does

When you power it on, the display shows the **temperature in Fahrenheit** (like `72F`).

Press the button to switch between three modes:
1. 🌡️ **Temperature** - Shows degrees Fahrenheit (example: `72F`)
2. 💧 **Humidity** - Shows percentage with an H (example: `H45`)
3. 🎈 **Pressure** - Shows air pressure in hPa (example: `1013`)

The sensor updates every 2 seconds!

## 📦 Required Modules

You need to copy these files to the `lib/` folder on your CIRCUITPY drive:

- `adafruit_bme280/` (folder with BME280 sensor code)
- `tm1637_display.py` (custom display driver - should be in this project folder)
- `adafruit_bus_device/` (folder - helper for I2C communication)
- `adafruit_register/` (folder - helper for sensor registers)

**Where to get them:**
- Download the CircuitPython library bundle from https://circuitpython.org/libraries
- Find the modules in the `lib/` folder of the bundle
- Copy them to your `lib/` folder on the CIRCUITPY drive
- The `tm1637_display.py` file is custom and should be in this project folder

## 🎮 Fun Things to Try

- 😮 **Breathe on the sensor** - watch humidity jump up!
- 🤲 **Cup your hands around it** - see temperature rise from your body heat!
- 🧊 **Hold an ice pack near it** - watch temperature drop!
