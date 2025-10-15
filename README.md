# Gati Demos - Embedded Hardware Projects

A collection of fun embedded hardware projects for learning and demonstration. Each "machine" is a self-contained project targeting either ESP32-C3 or RP2040 microcontrollers.

## Projects Overview

### 😄 [Joke Machine](joke_machine/)
**Platform:** ESP32-C3 Super Mini | **Language:** MicroPython

A joke-telling device with OLED display and button control. Features 50+ jokes, auto-cycling mode, random selection, and inverted banner headers.

**Hardware:** 0.96" OLED display (I2C), 6x6mm tactile button
**Key Features:** Auto-cycle mode, random jokes, button control

[📖 Read full documentation →](joke_machine/README.md)

---

### 🎵 [Song Machine](song_machine/)
**Platform:** RP2040 | **Language:** CircuitPython

Multi-song music player using dual passive buzzers. Plays 6 iconic songs with accurate melodies and timing.

**Hardware:** 2x passive buzzers (GPIO2, GPIO4)
**Key Features:** Dual buzzer volume boost, 6-song playlist, automatic rotation

**Playlist:** Super Mario Bros, Tetris, Star Wars Imperial March, Harry Potter, Minecraft Pigstep, Happy Bounce (original)

[📖 Read full documentation →](song_machine/README.md)

---

### 🚦 [Traffic Light](traffic_light/)
**Platform:** RP2040 | **Language:** CircuitPython

Realistic traffic light simulator with configurable timing. Great for learning GPIO control and sequential logic.

**Hardware:** 3x LEDs (red, yellow, green), 3x 220Ω resistors (GPIO6, GPIO7, GPIO8)
**Key Features:** Realistic sequence timing, serial debug output, customizable durations

[📖 Read full documentation →](traffic_light/README.md)

---

### ⛅ [Weather Machine](weather_machine/)
**Platform:** RP2040 | **Language:** CircuitPython

Weather station displaying real-time temperature, humidity, and barometric pressure on a 4-digit 7-segment display.

**Hardware:** BME280 sensor (I2C), TM1637 4-digit display
**Key Features:** Rotating display modes, real-time sensor readings, interactive demos

[📖 Read full documentation →](weather_machine/README.md)

## Hardware Platforms

### ESP32-C3 Super Mini
- Low-cost microcontroller with WiFi and Bluetooth LE
- Programmed using MicroPython
- 3.3V logic level, USB-C interface
- **Used in:** Joke Machine

### RP2040
- Dual-core ARM Cortex-M0+ microcontroller by Raspberry Pi Foundation
- Runs CircuitPython for rapid prototyping and easy development
- 3.3V logic level, micro-USB interface
- Flexible PWM, I2C, and GPIO capabilities
- **Used in:** Song Machine, Traffic Light, Weather Machine

## Quick Start

1. **Choose a project** - Click any project link above to view full documentation
2. **Gather hardware** - Each project README lists required components
3. **Set up software** - Install CircuitPython or MicroPython as needed
4. **Follow wiring diagram** - Connect components according to project README
5. **Upload code** - Copy code files to your microcontroller
6. **Power on and enjoy!**

Each project directory contains:
- Complete source code (`main.py` or `code.py`)
- Detailed README with wiring diagrams and setup instructions
- Configuration options and customization guides

## Development Tools

### For ESP32-C3 (MicroPython)
- **Thonny IDE** - Beginner-friendly with built-in REPL
- **esptool** - Firmware flashing utility
- **ampy / rshell** - File transfer tools

### For RP2040 (CircuitPython)
- **Drag-and-drop** - Simply copy files to CIRCUITPY drive
- **Mu Editor** - Simple Python editor with serial console
- **Thonny** - Works with CircuitPython too

### Universal Tools
- **Serial monitor** - View debug output (screen, minicom, PuTTY)
- **Multimeter** - Essential for debugging hardware issues
- **Breadboard** - Quick prototyping without soldering

## Learning Resources

### Documentation
- [CircuitPython Documentation](https://docs.circuitpython.org/) - Official CircuitPython guide
- [MicroPython Documentation](https://docs.micropython.org/) - MicroPython reference
- [ESP32-C3 Documentation](https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/) - ESP32-C3 technical docs
- [RP2040 Datasheet](https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf) - Hardware specifications

### Tutorials
- [Adafruit Learn](https://learn.adafruit.com/) - Excellent CircuitPython tutorials
- [CircuitPython Essentials](https://learn.adafruit.com/circuitpython-essentials) - Getting started guide
- [Raspberry Pi Pico Getting Started](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)

## Project Ideas & Expansions

These projects are just starting points! Consider these enhancements:

- **Add WiFi connectivity** - Report sensor data to the cloud, sync jokes from web API
- **Combine projects** - Use weather data to select appropriate joke mood
- **Add displays** - OLED displays for richer visual feedback
- **Buttons and controls** - Add interactivity with buttons, potentiometers, or encoders
- **Sound and music** - Expand song library, add sound effects to other projects
- **Logging and analytics** - Store data on SD cards, create data visualizations
- **Battery power** - Make projects portable with LiPo batteries and charging circuits

## Repository Structure

```
gati-demos/
├── README.md              # This file - project overview
├── .gitignore            # Git ignore patterns
├── CLAUDE.md             # AI assistant guidance
├── joke_machine/         # ESP32-C3 joke display
│   ├── README.md
│   ├── main.py
│   └── ssd1306.py
├── song_machine/        # RP2040 music player
│   ├── README.md
│   └── code.py
├── traffic_light/       # RP2040 LED sequencer
│   ├── README.md
│   └── code.py
└── weather_machine/     # RP2040 weather station
    ├── README.md
    ├── code.py
    └── lib/             # Required libraries
```

## About

This collection demonstrates various embedded hardware concepts through fun, hands-on projects. Each project is designed to be educational, approachable, and easy to customize.

Perfect for:
- Learning embedded programming
- Classroom demonstrations
- Maker workshops and hackathons
- Personal skill development
- Gift projects for curious minds

Built with passion for embedded systems and hardware hacking!
