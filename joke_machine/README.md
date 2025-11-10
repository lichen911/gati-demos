# 😂 Joke Machine

A fun joke-telling device using an OLED display and buttons. Navigate through 50+ kid-friendly jokes!

## 🎯 Purpose

This demo shows how to use an I2C OLED display with MicroPython, handle button input, and manage state (showing questions vs answers). Great for learning text display, user interaction, and sequential navigation.

## ✨ What It Does

- Displays 50+ jokes on a small OLED screen
- Shows jokes in random order (shuffled at startup)
- **Forward Button (GPIO2)**: Reveals answer or goes to next joke
- **Back Button (GPIO3)**: Shows question or goes to previous joke
- Nice headers in the yellow display strip ("Question?" / "Answer")
- Smart text wrapping to fit the tiny screen

## 🔌 GPIO Pins

- **GPIO8** - I2C SDA (display data)
- **GPIO9** - I2C SCL (display clock)
- **GPIO2** - ⏭️ Forward button (button connects to GND, uses internal pull-up)
- **GPIO3** - ⏮️ Back button (button connects to GND, uses internal pull-up)

## 🖥️ Hardware

- **ESP32-C3 Super Mini** microcontroller
- **0.96" OLED display** (SSD1306, 128x64 pixels, I2C, yellow/blue)
- **2 buttons** (6x6mm tactile buttons work great)

## 📚 Required File

You need the `ssd1306.py` driver file on your ESP32-C3. This is the standard MicroPython SSD1306 OLED driver.

## 🎮 How to Use

1. Power on - shows a random joke question
2. Press **Forward** to see the answer
3. Press **Forward** again to go to the next joke
4. Press **Back** to go back to the question (or previous joke)
5. Jokes wrap around - after the last one, it goes back to the first!

**Note:** The jokes are shuffled randomly each time you restart, so you'll see them in a different order every time! 🎲
