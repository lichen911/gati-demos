# 🚦 Traffic Light

A simple traffic light simulator that cycles through red, yellow, and green LEDs. Includes a button to speed up the cycle! 🏎️

## 🎯 Purpose

This demo demonstrates basic GPIO control on an RP2040 Zero board, including digital output for LEDs and digital input for button reading. It's useful for learning timing sequences and interactive hardware control.

## ✨ What It Does

- Cycles through 🟢 green → 🟡 yellow → 🔴 red lights continuously
- Each light stays on for 3 seconds by default ⏱️
- Press the button to increase speed (8 speed levels, each 2x faster) ⚡
- Button press cycles through speeds: 1x → 2x → 4x → 8x → 16x → 32x → 64x → 128x → back to 1x

## 🔌 GPIO Pins

- **GP6** - 🔴 Red LED (with 220Ω resistor to GND)
- **GP7** - 🟡 Yellow LED (with 220Ω resistor to GND)
- **GP8** - 🟢 Green LED (with 220Ω resistor to GND)
- **GP2** - 🔘 Button input (button connects to GND, uses internal pull-up)
