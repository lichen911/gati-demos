# RP2040 Weather Station

## Project Overview
A complete weather station demo using an RP2040 microcontroller with BME280 environmental sensor and TM1637 4-digit 7-segment display. Displays temperature, humidity, and barometric pressure readings in real-time.

## Hardware Components

### Microcontroller
- **RP2040 Development Board**
  - Dual-core ARM Cortex-M0+ processor
  - No built-in WiFi (using local sensor data)
  - Runs CircuitPython for easy development
  - 3.3V logic level

### Sensor
- **BME280 Environmental Sensor**
  - Measures temperature: -40°C to +85°C (±1°C accuracy)
  - Measures humidity: 0-100% RH (±3% accuracy)
  - Measures barometric pressure: 300-1100 hPa (±1 hPa accuracy)
  - Communication: I2C interface
  - Operating voltage: 3.3V
  - I2C address: 0x76 or 0x77 (default is usually 0x77)

### Display
- **TM1637 4-Digit 7-Segment Display**
  - 4-digit LED display with colon separator
  - Uses TM1637 driver chip
  - 2-wire interface (CLK and DIO)
  - Operating voltage: 5V (display), 3.3V logic compatible
  - Adjustable brightness

## Wiring Diagram

### BME280 Sensor Connections (I2C)
| BME280 Pin | RP2040 Pin | Description |
|------------|------------|-------------|
| VCC/VIN    | 3.3V       | Power supply (3.3V) |
| GND        | GND        | Ground |
| SCL        | GP5        | I2C Clock |
| SDA        | GP4        | I2C Data |

**Note:** GP4 and GP5 are standard I2C0 pins on RP2040. You can use other GPIO pins, but these are the default hardware I2C pins for better reliability.

### TM1637 Display Connections
| TM1637 Pin | RP2040 Pin | Description |
|------------|------------|-------------|
| VCC        | VBUS (5V)  | Power supply (5V for brightness) |
| GND        | GND        | Ground |
| CLK        | GP2        | Clock signal |
| DIO        | GP3        | Data I/O signal |

**Note:** TM1637 uses a 2-wire protocol (not I2C). CLK and DIO can be any GPIO pins. The display works at 3.3V logic levels even though powered by 5V.

## Pin Summary
```
RP2040 GPIO Assignments:
├── GP2  → TM1637 CLK
├── GP3  → TM1637 DIO
├── GP4  → BME280 SDA (I2C0)
├── GP5  → BME280 SCL (I2C0)
├── 3.3V → BME280 VCC
├── VBUS → TM1637 VCC (5V from USB)
└── GND  → Common Ground (BME280 + TM1637)
```

## Power Requirements
- **Total power draw**: ~100mA (well within USB 2.0 spec of 500mA)
- **Power source**: USB 5V battery pack
  - RP2040 has onboard 3.3V regulator
  - BME280 runs on regulated 3.3V
  - TM1637 runs on 5V directly from USB (VBUS pin)

## Software Requirements

### CircuitPython Installation
1. Download CircuitPython UF2 file for RP2040 from: https://circuitpython.org/board/raspberry_pi_pico/
2. Hold BOOTSEL button while plugging in USB
3. Drag and drop UF2 file onto RPI-RP2 drive
4. Board reboots as CIRCUITPY drive

### Required Libraries
Download the CircuitPython library bundle from: https://circuitpython.org/libraries

Copy these to the `lib/` folder on CIRCUITPY drive:
- `adafruit_bme280.mpy` (or `adafruit_bme280/` folder)
- `adafruit_tm1637.py`
- `adafruit_bus_device/` (folder - required dependency for BME280)
- `adafruit_register/` (folder - required dependency for BME280)

### Code Structure
```
CIRCUITPY/
├── code.py              # Main program (auto-runs on boot)
├── lib/
│   ├── adafruit_bme280.mpy
│   ├── adafruit_tm1637.py
│   ├── adafruit_bus_device/
│   └── adafruit_register/
└── README.md            # This file
```

## Functionality

### Display Modes
The code should cycle through three display modes:

1. **Temperature Display**
   - Show temperature in Fahrenheit (or Celsius)
   - Display format: `72.5` (with decimal point) or `72` (integer)
   - Update every 2-3 seconds

2. **Humidity Display**
   - Show relative humidity percentage
   - Display format: `45.2` (with decimal) or show `H` prefix if possible
   - Update every 2-3 seconds

3. **Pressure Display**
   - Show barometric pressure in hPa (hectopascals/millibars)
   - Display format: `1013` (4 digits fits perfectly)
   - Update every 2-3 seconds

### Features to Implement
- [ ] Read BME280 sensor data via I2C
- [ ] Display readings on TM1637 in rotation
- [ ] Adjustable display brightness
- [ ] Serial output for debugging (print all readings to console)
- [ ] Error handling for sensor communication failures
- [ ] Optional: Use colon separator to indicate which reading is displayed
- [ ] Optional: Add button to manually cycle through display modes

## Classroom Demo Tips

### Interactive Elements
- **Breathe on sensor**: Humidity spikes dramatically (kids love this!)
- **Cup hands around it**: Temperature rises from body heat
- **Ice pack test**: Show temperature dropping in real-time
- **Weather prediction**: Explain how falling pressure = incoming storms

### Teaching Moments
- Explain what each measurement means for weather
- Show how pressure changes throughout the day
- Discuss why humidity matters (comfort, weather)
- Demonstrate sensor response time

## Troubleshooting

### BME280 Not Detected
- Check I2C address (try 0x76 if 0x77 doesn't work)
- Verify wiring: SDA and SCL not swapped
- Ensure 3.3V power, not 5V (can damage sensor)
- Try adding pull-up resistors (4.7kΩ) on SDA/SCL if using long wires

### TM1637 Display Issues
- Verify CLK and DIO connections
- Check 5V power supply (dim display = low voltage)
- Try different GPIO pins if no response
- Reduce brightness if display is too dim

### General Issues
- Press CTRL+C in serial console to stop running code
- Check serial output for error messages
- Verify all libraries are in `lib/` folder
- Re-flash CircuitPython if unstable

## Next Steps / Enhancements
- Add OLED display to show all three readings simultaneously
- Log data to SD card or CSV file
- Add WiFi module to upload data to cloud
- Create graphs of pressure trends (weather forecasting)
- Add LED indicators for comfort levels (temp/humidity ranges)
- Calculate heat index or dew point from temp + humidity

## References
- CircuitPython BME280 Guide: https://learn.adafruit.com/adafruit-bme280-humidity-barometric-pressure-temperature-sensor-breakout
- TM1637 Library Docs: https://docs.circuitpython.org/projects/tm1637/en/latest/
- RP2040 Pinout: https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf