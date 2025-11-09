# 🎵 Song Machine

A button-controlled music player using dual passive buzzers. Play through 7 iconic songs with interactive controls!

## 🎯 Purpose

This demo shows how to use PWM (Pulse Width Modulation) to generate musical tones on buzzers, and how to handle button interrupts during playback. Great for learning about sound generation and interactive control.

## ✨ What It Does

- Plays 7 pre-programmed songs using two buzzers
- **Next Button (GP7)**: Skip to next song (even during playback!)
- **Replay Button (GP8)**: Play/restart current song
- Songs loop around - after the last song, it goes back to the first
- You can interrupt any song at any time by pressing a button

## 🔌 GPIO Pins

- **GP2** - 🔊 Buzzer 1 (buzzer + to GP2, - to GND)
- **GP4** - 🔊 Buzzer 2 (buzzer + to GP4, - to GND)
- **GP7** - ⏭️ Next button (button connects to GND, uses internal pull-up)
- **GP8** - 🔁 Replay button (button connects to GND, uses internal pull-up)

**Note:** GP2 and GP4 are on different PWM slices, allowing both buzzers to play the same frequency simultaneously for louder sound!

## 🎶 Song List

The song machine includes these 7 songs:

1. 🍄 **Super Mario Bros Theme**
2. 😊 **Happy Bounce** (original composition)
3. 🧱 **Tetris Theme**
4. ⭐ **Star Wars Imperial March**
5. 🪄 **Hedwig's Theme** (Harry Potter)
6. ⛏️ **Minecraft Pigstep**
7. 🗡️ **The Legend of Zelda Theme**

**Note:** These are buzzer approximations - they sound like the original songs, but buzzers can only beep single notes, so they're a bit simpler than the real thing! 🎵

## 🎮 How to Use

1. Press the **Replay button** to start playing the current song
2. Press the **Next button** to skip to the next song
3. Press buttons during playback to interrupt and change songs immediately
4. Have fun! 🎉
