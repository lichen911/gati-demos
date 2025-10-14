# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a collection of embedded hardware projects targeting ESP32-C3 microcontrollers. Each subdirectory represents a standalone "machine" project with specific hardware functionality.

## Project Structure

The repository is organized into separate machine projects:

- `joke_machine/` - ESP32-C3 Super Mini with 0.96" OLED display and tactile button for displaying jokes
- `song_machine/` - (To be implemented)
- `weather_machine/` - (To be implemented)

Each machine is a self-contained project with its own hardware configuration and code.

## Hardware Platform

All projects target the **ESP32-C3 Super Mini** microcontroller. When working with these projects:

- Development is typically done using Arduino IDE or PlatformIO
- Code files are usually `.ino` (Arduino sketches) or `.cpp/.h` (C++ for PlatformIO)
- Each project may have different hardware peripherals (displays, buttons, sensors)

## joke_machine Specifications

Hardware:
- ESP32-C3 Super Mini microcontroller
- 0.96" OLED display for output
- 6x6 mm tactile button for user input

Behavior:
- Displays jokes from a hard-coded list
- On boot: shows a joke question
- Button press: reveals the joke answer
- Next button press: advances to the next joke
- Cycles through the joke list

## Development Workflow

Since this is an embedded hardware repository, typical development involves:

1. Writing Arduino sketches (.ino) or C++ code for ESP32-C3
2. Building and uploading firmware to the physical device
3. Testing with actual hardware (OLED displays, buttons, sensors)
4. Serial debugging via USB connection

Common commands will depend on the development environment chosen (Arduino IDE, PlatformIO, ESP-IDF).
