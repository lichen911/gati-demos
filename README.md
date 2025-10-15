# Gati Demos - Embedded Hardware Projects

A collection of fun embedded hardware projects targeting microcontrollers like ESP32-C3 and RP2040. Each "machine" is a self-contained project with its own hardware configuration and functionality.

## Projects

### 🎵 Song Machine
**Hardware:** RP2040 (CircuitPython)
- Multi-song player with passive buzzers
- Dual buzzer support for increased volume (GPIO2 and GPIO4)
- Features 6 songs including Super Mario Bros, Tetris, Star Wars Imperial March, Hedwig's Theme, Minecraft Pigstep, and an original composition
- Continuous playback with automatic song rotation

### 😄 Joke Machine
**Hardware:** ESP32-C3 Super Mini
- 0.96" OLED display for output
- 6x6 mm tactile button for user input
- Displays jokes from a hard-coded list
- Interactive: button press reveals punchline, next press advances to next joke

### 🚦 Traffic Light
**Hardware:** TBD
- Status: In development

### ⛅ Weather Machine
**Hardware:** TBD
- Status: In development

## Hardware Platforms

### ESP32-C3 Super Mini
- Low-cost microcontroller with WiFi/BLE
- Typically programmed using Arduino IDE or PlatformIO
- Used in: Joke Machine

### RP2040
- Dual-core ARM Cortex-M0+ microcontroller
- Runs CircuitPython for rapid prototyping
- Used in: Song Machine

## Getting Started

### Prerequisites
- **For ESP32-C3 projects:** Arduino IDE or PlatformIO
- **For RP2040 projects:** CircuitPython installed on your board
- USB cable for programming and power

### Project Structure
Each project directory contains:
- Source code (`.ino` for Arduino, `code.py` for CircuitPython)
- Project-specific README with hardware details
- Wiring diagrams (where applicable)

### Running a Project
1. Navigate to the project directory
2. Follow the project-specific README for hardware setup
3. Upload/copy the code to your microcontroller
4. Connect via serial to see debug output (optional)

## Development

### Adding a New Machine
1. Create a new directory: `your_machine/`
2. Add hardware documentation
3. Implement the code
4. Update this README with project details

### Tools
- **Arduino IDE** - For ESP32-C3 development
- **PlatformIO** - Alternative IDE for embedded development
- **Thonny/Mu** - For CircuitPython development
- **Serial Monitor** - For debugging via USB

## Resources

- [ESP32-C3 Documentation](https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/)
- [CircuitPython Documentation](https://docs.circuitpython.org/)
- [RP2040 Datasheet](https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf)

## Author

Created with passion for embedded systems and hardware hacking!
