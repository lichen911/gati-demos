"""
Song Machine - Multi-Song Player
Hardware: RP2040 with passive buzzers on GPIO2 and GPIO4
Plays multiple songs in a loop with dual buzzers for increased volume
"""

import board
import pwmio
import time

# Initialize PWM on GPIO2 and GPIO4 for dual buzzers
# Note: GP2 and GP4 are on different PWM slices, allowing both to use variable_frequency
buzzer1 = pwmio.PWMOut(board.GP2, variable_frequency=True)
buzzer2 = pwmio.PWMOut(board.GP4, variable_frequency=True)

# Define note frequencies (in Hz)
NOTE_C4 = 262
NOTE_D4 = 294
NOTE_E4 = 330
NOTE_F4 = 349
NOTE_G4 = 392
NOTE_A4 = 440
NOTE_B4 = 494
NOTE_C5 = 523
NOTE_D5 = 587
NOTE_E5 = 659
NOTE_F5 = 698
NOTE_G5 = 784
NOTE_A5 = 880
NOTE_B5 = 988
NOTE_C6 = 1047
NOTE_D6 = 1175
NOTE_E6 = 1319
NOTE_F6 = 1397
NOTE_G6 = 1568
NOTE_A6 = 1760
NOTE_REST = 0

# Define note durations for Mario (slower tempo)
# Tempo: ~180 BPM
EIGHTH = 0.15
QUARTER = 0.3
QUARTER_DOT = 0.45
HALF = 0.6
HALF_DOT = 0.9

# Define note durations for fast songs (faster tempo)
# Tempo: ~240 BPM
FAST_SIXTEENTH = 0.08
FAST_EIGHTH = 0.12
FAST_QUARTER = 0.2
FAST_HALF = 0.4

# Super Mario Bros Main Theme - Opening section
# Format: (note_frequency, duration)
mario_theme = [
    # Intro: "E E _ E _ C E _ G _ _ _"
    (NOTE_E5, EIGHTH),
    (NOTE_E5, EIGHTH),
    (NOTE_REST, EIGHTH),
    (NOTE_E5, EIGHTH),
    (NOTE_REST, EIGHTH),
    (NOTE_C5, EIGHTH),
    (NOTE_E5, EIGHTH),
    (NOTE_REST, EIGHTH),
    (NOTE_G5, EIGHTH),
    (NOTE_REST, EIGHTH),
    (NOTE_REST, EIGHTH),
    (NOTE_REST, EIGHTH),
    (NOTE_G4, EIGHTH),
    (NOTE_REST, EIGHTH),
    (NOTE_REST, EIGHTH),
    (NOTE_REST, EIGHTH),

    # Verse
    (NOTE_C5, EIGHTH),
    (NOTE_REST, EIGHTH),
    (NOTE_REST, EIGHTH),
    (NOTE_G4, EIGHTH),
    (NOTE_REST, EIGHTH),
    (NOTE_REST, EIGHTH),
    (NOTE_E4, EIGHTH),
    (NOTE_REST, EIGHTH),
    (NOTE_REST, EIGHTH),
    (NOTE_A4, EIGHTH),
    (NOTE_REST, EIGHTH),
    (NOTE_B4, EIGHTH),
    (NOTE_REST, EIGHTH),
    (NOTE_A4, EIGHTH),
    (NOTE_A4, EIGHTH),
    (NOTE_REST, EIGHTH),

    (NOTE_G4, EIGHTH),
    (NOTE_E5, EIGHTH),
    (NOTE_G5, EIGHTH),
    (NOTE_A5, EIGHTH),
    (NOTE_REST, EIGHTH),
    (NOTE_F5, EIGHTH),
    (NOTE_G5, EIGHTH),
    (NOTE_REST, EIGHTH),
    (NOTE_E5, EIGHTH),
    (NOTE_REST, EIGHTH),
    (NOTE_C5, EIGHTH),
    (NOTE_D5, EIGHTH),
    (NOTE_B4, EIGHTH),
    (NOTE_REST, EIGHTH),
    (NOTE_REST, EIGHTH),
    (NOTE_REST, EIGHTH),
]

# Happy Bounce - Original upbeat melody with high frequencies
# Fast tempo, high pitched, cheerful and energetic
happy_bounce = [
    # Pattern 1: Ascending happy melody
    (NOTE_C6, FAST_EIGHTH),
    (NOTE_E6, FAST_EIGHTH),
    (NOTE_G6, FAST_EIGHTH),
    (NOTE_E6, FAST_EIGHTH),
    (NOTE_C6, FAST_EIGHTH),
    (NOTE_E6, FAST_EIGHTH),
    (NOTE_G6, FAST_QUARTER),
    (NOTE_REST, FAST_EIGHTH),

    # Pattern 2: Bouncy rhythm
    (NOTE_A6, FAST_EIGHTH),
    (NOTE_A6, FAST_EIGHTH),
    (NOTE_G6, FAST_EIGHTH),
    (NOTE_E6, FAST_EIGHTH),
    (NOTE_C6, FAST_EIGHTH),
    (NOTE_REST, FAST_EIGHTH),
    (NOTE_D6, FAST_EIGHTH),
    (NOTE_F6, FAST_QUARTER),

    # Pattern 3: Quick ascending run
    (NOTE_E6, FAST_SIXTEENTH),
    (NOTE_F6, FAST_SIXTEENTH),
    (NOTE_G6, FAST_SIXTEENTH),
    (NOTE_A6, FAST_SIXTEENTH),
    (NOTE_G6, FAST_EIGHTH),
    (NOTE_E6, FAST_EIGHTH),
    (NOTE_C6, FAST_EIGHTH),
    (NOTE_E6, FAST_EIGHTH),
    (NOTE_D6, FAST_QUARTER),
    (NOTE_REST, FAST_EIGHTH),

    # Pattern 4: High energy finale
    (NOTE_G6, FAST_EIGHTH),
    (NOTE_G6, FAST_EIGHTH),
    (NOTE_A6, FAST_EIGHTH),
    (NOTE_G6, FAST_EIGHTH),
    (NOTE_F6, FAST_EIGHTH),
    (NOTE_E6, FAST_EIGHTH),
    (NOTE_D6, FAST_EIGHTH),
    (NOTE_C6, FAST_EIGHTH),
    (NOTE_E6, FAST_EIGHTH),
    (NOTE_G6, FAST_QUARTER),
    (NOTE_C6, FAST_HALF),
]

# Tetris Theme (Korobeiniki) - Fast Russian folk melody
tetris_theme = [
    # Main melody line 1
    (NOTE_E5, FAST_QUARTER),
    (NOTE_B4, FAST_EIGHTH),
    (NOTE_C5, FAST_EIGHTH),
    (NOTE_D5, FAST_QUARTER),
    (NOTE_C5, FAST_EIGHTH),
    (NOTE_B4, FAST_EIGHTH),
    (NOTE_A4, FAST_QUARTER),
    (NOTE_A4, FAST_EIGHTH),
    (NOTE_C5, FAST_EIGHTH),
    (NOTE_E5, FAST_QUARTER),
    (NOTE_D5, FAST_EIGHTH),
    (NOTE_C5, FAST_EIGHTH),
    (NOTE_B4, FAST_QUARTER),
    (NOTE_B4, FAST_EIGHTH),
    (NOTE_C5, FAST_EIGHTH),
    (NOTE_D5, FAST_QUARTER),
    (NOTE_E5, FAST_QUARTER),
    (NOTE_C5, FAST_QUARTER),
    (NOTE_A4, FAST_QUARTER),
    (NOTE_A4, FAST_QUARTER),
    (NOTE_REST, FAST_EIGHTH),

    # Melody line 2
    (NOTE_D5, FAST_QUARTER),
    (NOTE_F5, FAST_EIGHTH),
    (NOTE_A5, FAST_QUARTER),
    (NOTE_G5, FAST_EIGHTH),
    (NOTE_F5, FAST_EIGHTH),
    (NOTE_E5, FAST_QUARTER),
    (NOTE_E5, FAST_EIGHTH),
    (NOTE_C5, FAST_EIGHTH),
    (NOTE_E5, FAST_QUARTER),
    (NOTE_D5, FAST_EIGHTH),
    (NOTE_C5, FAST_EIGHTH),
    (NOTE_B4, FAST_QUARTER),
    (NOTE_B4, FAST_EIGHTH),
    (NOTE_C5, FAST_EIGHTH),
    (NOTE_D5, FAST_QUARTER),
    (NOTE_E5, FAST_QUARTER),
    (NOTE_C5, FAST_QUARTER),
    (NOTE_A4, FAST_QUARTER),
    (NOTE_A4, FAST_QUARTER),
]

# Star Wars Imperial March - Powerful and iconic
imperial_march = [
    # "Dum dum dum, dum-da-dum, dum-da-dum"
    (NOTE_G4, QUARTER),
    (NOTE_G4, QUARTER),
    (NOTE_G4, QUARTER),
    (NOTE_E4, QUARTER_DOT),
    (NOTE_B4, EIGHTH),
    (NOTE_G4, QUARTER),
    (NOTE_E4, QUARTER_DOT),
    (NOTE_B4, EIGHTH),
    (NOTE_G4, HALF),
    (NOTE_REST, QUARTER),

    # Second phrase
    (NOTE_D5, QUARTER),
    (NOTE_D5, QUARTER),
    (NOTE_D5, QUARTER),
    (NOTE_E5, QUARTER_DOT),
    (NOTE_B4, EIGHTH),
    (NOTE_G4, QUARTER),
    (NOTE_E4, QUARTER_DOT),
    (NOTE_B4, EIGHTH),
    (NOTE_G4, HALF),
    (NOTE_REST, QUARTER),

    # Bridge
    (NOTE_G5, QUARTER),
    (NOTE_G4, QUARTER_DOT),
    (NOTE_G4, EIGHTH),
    (NOTE_G5, QUARTER),
    (NOTE_F5, QUARTER_DOT),
    (NOTE_E5, EIGHTH),
    (NOTE_D5, EIGHTH),
    (NOTE_C5, EIGHTH),
    (NOTE_B4, QUARTER),
    (NOTE_REST, EIGHTH),
]

# Hedwig's Theme (Harry Potter) - Magical and mysterious
hedwigs_theme = [
    # Opening motif
    (NOTE_B4, FAST_EIGHTH),
    (NOTE_E5, FAST_QUARTER),
    (NOTE_G5, FAST_EIGHTH),
    (NOTE_F5, FAST_EIGHTH),
    (NOTE_E5, FAST_QUARTER),
    (NOTE_B5, FAST_HALF),
    (NOTE_A5, FAST_HALF),
    (NOTE_REST, FAST_EIGHTH),

    # Second phrase
    (NOTE_E5, FAST_HALF),
    (NOTE_G5, FAST_EIGHTH),
    (NOTE_F5, FAST_EIGHTH),
    (NOTE_D5, FAST_QUARTER),
    (NOTE_F5, FAST_HALF),
    (NOTE_B4, FAST_HALF),
    (NOTE_REST, FAST_EIGHTH),

    # Third phrase
    (NOTE_B4, FAST_EIGHTH),
    (NOTE_E5, FAST_QUARTER),
    (NOTE_G5, FAST_EIGHTH),
    (NOTE_F5, FAST_EIGHTH),
    (NOTE_E5, FAST_QUARTER),
    (NOTE_B5, FAST_HALF),
    (NOTE_D6, FAST_HALF),
    (NOTE_REST, FAST_EIGHTH),

    # Descending finale
    (NOTE_C6, FAST_QUARTER),
    (NOTE_B5, FAST_EIGHTH),
    (NOTE_A5, FAST_EIGHTH),
    (NOTE_B5, FAST_HALF),
    (NOTE_G5, FAST_EIGHTH),
    (NOTE_E5, FAST_HALF),
    (NOTE_B4, FAST_QUARTER),
    (NOTE_E5, FAST_HALF),
]

# Minecraft Pigstep - Funky Nether track
pigstep = [
    # Intro - Funky bass-like pattern
    (NOTE_D4, FAST_EIGHTH),
    (NOTE_D4, FAST_EIGHTH),
    (NOTE_D5, FAST_EIGHTH),
    (NOTE_D4, FAST_EIGHTH),
    (NOTE_REST, FAST_EIGHTH),
    (NOTE_D4, FAST_EIGHTH),
    (NOTE_C5, FAST_EIGHTH),
    (NOTE_D4, FAST_EIGHTH),

    # Main melody - syncopated rhythm
    (NOTE_D5, FAST_QUARTER),
    (NOTE_F5, FAST_EIGHTH),
    (NOTE_D5, FAST_EIGHTH),
    (NOTE_C5, FAST_EIGHTH),
    (NOTE_A4, FAST_EIGHTH),
    (NOTE_REST, FAST_EIGHTH),
    (NOTE_D5, FAST_EIGHTH),
    (NOTE_F5, FAST_QUARTER),
    (NOTE_G5, FAST_EIGHTH),
    (NOTE_F5, FAST_EIGHTH),
    (NOTE_D5, FAST_QUARTER),
    (NOTE_REST, FAST_EIGHTH),

    # Funky middle section
    (NOTE_A4, FAST_EIGHTH),
    (NOTE_A4, FAST_EIGHTH),
    (NOTE_D5, FAST_EIGHTH),
    (NOTE_F5, FAST_EIGHTH),
    (NOTE_G5, FAST_EIGHTH),
    (NOTE_F5, FAST_EIGHTH),
    (NOTE_D5, FAST_EIGHTH),
    (NOTE_C5, FAST_EIGHTH),
    (NOTE_D5, FAST_QUARTER),
    (NOTE_REST, FAST_EIGHTH),
    (NOTE_A4, FAST_EIGHTH),

    # High section
    (NOTE_D6, FAST_EIGHTH),
    (NOTE_D6, FAST_EIGHTH),
    (NOTE_C6, FAST_EIGHTH),
    (NOTE_A5, FAST_EIGHTH),
    (NOTE_F5, FAST_QUARTER),
    (NOTE_D5, FAST_EIGHTH),
    (NOTE_F5, FAST_EIGHTH),
    (NOTE_G5, FAST_QUARTER),
    (NOTE_REST, FAST_EIGHTH),

    # Closing phrase
    (NOTE_D5, FAST_EIGHTH),
    (NOTE_F5, FAST_EIGHTH),
    (NOTE_D5, FAST_EIGHTH),
    (NOTE_C5, FAST_EIGHTH),
    (NOTE_D5, FAST_EIGHTH),
    (NOTE_A4, FAST_QUARTER),
    (NOTE_REST, FAST_QUARTER),
    (NOTE_D4, FAST_EIGHTH),
    (NOTE_D5, FAST_QUARTER),
]

# Song library
songs = [
    ("Super Mario Bros Theme", mario_theme),
    ("Happy Bounce (Original)", happy_bounce),
    ("Tetris Theme", tetris_theme),
    ("Star Wars Imperial March", imperial_march),
    ("Hedwig's Theme (Harry Potter)", hedwigs_theme),
    ("Minecraft Pigstep", pigstep),
]

def play_note(frequency, duration):
    """Play a note for the specified duration on both buzzers"""
    if frequency == NOTE_REST:
        buzzer1.duty_cycle = 0  # Silence
        buzzer2.duty_cycle = 0
    else:
        buzzer1.frequency = frequency
        buzzer2.frequency = frequency
        buzzer1.duty_cycle = 32768  # 50% duty cycle
        buzzer2.duty_cycle = 32768
    time.sleep(duration)

print("Song Machine - Multi-Song Player")
print("=" * 40)
print(f"Loaded {len(songs)} songs")
print()

# Main loop - cycle through all songs
while True:
    for song_name, melody in songs:
        print(f"Now Playing: {song_name}")
        print("-" * 40)

        for note, duration in melody:
            play_note(note, duration)

        # Pause between songs
        buzzer1.duty_cycle = 0
        buzzer2.duty_cycle = 0
        print(f"✓ {song_name} complete\n")
        time.sleep(2.0)
