# Song Machine

A multi-song music player for RP2040 using dual passive buzzers. Plays a rotating playlist of 6 iconic songs including video game themes and movie soundtracks.

## Features

- 6 pre-programmed songs with accurate melodies and timing
- Dual buzzer support for approximately 2x volume output
- Continuous playlist rotation with automatic song switching
- PWM-based tone generation for clean audio output
- Serial debug output showing currently playing song

## Hardware Requirements

- RP2040 Development Board (Raspberry Pi Pico or compatible)
- 2x Passive Buzzers (piezo buzzers)
- Jumper wires
- Breadboard (optional)
- USB cable for power and programming

## Wiring Diagram

### Buzzer 1
- Positive (+) → GPIO2
- Negative (-) → GND

### Buzzer 2
- Positive (+) → GPIO4
- Negative (-) → GND

**Important:** GPIO2 and GPIO4 are on different PWM slices of the RP2040, which allows both to use variable frequency mode simultaneously. Do not use GPIO2 and GPIO3 together as they share the same PWM slice.

## Pin Summary
```
RP2040 GPIO Assignments:
├── GP2  → Buzzer 1 (+)
├── GP4  → Buzzer 2 (+)
└── GND  → Both Buzzers (-)
```

## Software Setup

### 1. Install CircuitPython on RP2040

1. Download CircuitPython UF2 file for your RP2040 board from: https://circuitpython.org/
2. Hold BOOTSEL button while plugging in USB
3. Drag and drop UF2 file onto RPI-RP2 drive
4. Board reboots as CIRCUITPY drive

### 2. Upload the Code

Simply copy `code.py` to the CIRCUITPY drive. The program will automatically start running.

### 3. Required Libraries

No additional libraries required! This project uses only CircuitPython built-in modules:
- `board` - GPIO pin definitions
- `pwmio` - PWM output for buzzer control
- `time` - Timing and delays

## Song Playlist

The song machine plays these 6 songs in rotation:

1. **Super Mario Bros Theme** - Classic NES platformer opening theme
2. **Happy Bounce (Original)** - Fast, high-pitched energetic melody
3. **Tetris Theme (Korobeiniki)** - Iconic Russian folk melody
4. **Star Wars Imperial March** - Darth Vader's powerful theme
5. **Hedwig's Theme** - Magical Harry Potter main theme
6. **Minecraft Pigstep** - Funky Nether music disc track

Each song plays once, followed by a 2-second pause before the next song begins. The playlist loops continuously.

## How It Works

### Tone Generation
- Both buzzers are driven simultaneously with identical PWM signals
- 50% duty cycle creates a clean square wave tone
- Variable frequency allows playing different musical notes
- Note frequencies range from 262 Hz (C4) to 1760 Hz (A6)

### Dual Buzzer Volume Boost
- Two buzzers playing in sync create constructive interference
- Approximately doubles the sound pressure level
- Distributes current load across two GPIO pins (safer than single pin)
- Both buzzers must be wired correctly (same polarity) to avoid cancellation

## Customization

### Adjusting Tempo
Edit timing constants in `code.py`:

```python
# Slower tempo (original Mario theme)
EIGHTH = 0.15
QUARTER = 0.3
QUARTER_DOT = 0.45
HALF = 0.6

# Faster tempo (Tetris, Pigstep, etc.)
FAST_SIXTEENTH = 0.08
FAST_EIGHTH = 0.12
FAST_QUARTER = 0.2
FAST_HALF = 0.4
```

### Adding New Songs
Add new melodies to the `songs` list:

```python
# Define your melody
my_song = [
    (NOTE_C5, QUARTER),
    (NOTE_E5, QUARTER),
    (NOTE_G5, HALF),
    # ... more notes
]

# Add to playlist
songs = [
    # ... existing songs
    ("My Song Title", my_song),
]
```

### Changing Song Order
Reorder entries in the `songs` list to change playback sequence.

### Pause Duration Between Songs
Modify the pause time in the main loop:

```python
time.sleep(2.0)  # Change from 2.0 seconds to desired value
```

## Troubleshooting

### No Sound from Buzzers
- Verify GPIO2 and GPIO4 wiring
- Check that you're using **passive** buzzers (not active buzzers)
- Ensure GND connections are solid
- Try increasing duty cycle if sound is too quiet
- Test each buzzer individually by commenting out one in code

### Buzzers Sound Quiet
- Check that both buzzers are wired with correct polarity (+ to GPIO, - to GND)
- If buzzers are out of phase, they can cancel each other out
- Verify 3.3V logic levels are sufficient for your buzzers
- Some buzzers are louder than others - try different models

### PWM Error on Startup
```
ValueError: Invalid variable_frequency
```
- This means GPIO pins are on the same PWM slice
- Solution: Use GPIO2 and GPIO4 (not GPIO2 and GPIO3)
- Check the code is using `board.GP2` and `board.GP4`

### Song Sounds Wrong
- Verify note frequencies match your intended melody
- Check timing constants are correct
- Passive buzzers have frequency response limitations (typically 2-4 kHz optimal)
- Very high or very low notes may sound weak

## Serial Debugging

Connect via serial to see song information:

```bash
screen /dev/ttyACM0 115200
# or
minicom -D /dev/ttyACM0 -b 115200
```

Output shows:
```
Song Machine - Multi-Song Player
========================================
Loaded 6 songs

Now Playing: Super Mario Bros Theme
----------------------------------------
✓ Super Mario Bros Theme complete
```

Press Ctrl+C in serial console to stop and access CircuitPython REPL.

## Technical Details

### PWM Configuration
- Frequency range: 100 Hz - 5000 Hz (music note range)
- Duty cycle: 50% (32768 out of 65535)
- Resolution: 16-bit PWM
- Both PWM channels synchronized in software

### Memory Usage
- All song data stored in flash memory as Python lists
- Minimal RAM usage during playback
- No audio buffering required

### Power Consumption
- Typical: ~50-100 mA (including RP2040 and buzzers)
- Can be powered via USB or battery pack
- No external power supply needed for buzzers

## References

- [CircuitPython PWMOut Documentation](https://docs.circuitpython.org/en/latest/shared-bindings/pwmio/index.html)
- [RP2040 Datasheet](https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf)
- [Musical Note Frequencies](https://pages.mtu.edu/~suits/notefreqs.html)
