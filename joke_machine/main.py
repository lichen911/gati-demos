"""
Joke Machine - MicroPython implementation for ESP32-C3
Displays jokes on 0.96" OLED display with button navigation
"""

from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
import time
import random

# Configuration
AUTO_MODE = True  # Set to True for auto-cycling, False for button-only mode
AUTO_DISPLAY_TIME = 5  # Seconds to display each question/answer in auto mode
RANDOM_MODE = False  # Set to True for random jokes, False for sequential order

# Hardware configuration
I2C_SDA_PIN = 8  # GPIO8 for SDA
I2C_SCL_PIN = 9  # GPIO9 for SCL
BUTTON_PIN = 10  # GPIO10 for button input
DISPLAY_WIDTH = 128
DISPLAY_HEIGHT = 64

# Joke database - list of (question, answer) tuples
JOKES = [
    ("Why did the cookie go to the doctor?",
     "Because it felt crumbly!"),

    ("Why do seagulls fly over the ocean?",
     "Because if they flew over the bay they'd be called bagels"),
     
    ("What do you call a bear with no teeth?",
     "A gummy bear!"),

    ("Why did the banana go to the doctor?",
     "Because it wasn't peeling well!"),

    ("What do you call cheese that isn't yours?",
     "Nacho cheese!"),

    ("Why don't eggs tell jokes?",
     "They'd crack each other up!"),

    ("What do you call a dinosaur that crashes its car?",
     "Tyrannosaurus WRECKS!"),

    ("Why did the math book look so sad?",
     "Because it had too many problems!"),

    ("What did the ocean say to the beach?",
     "Nothing, it just waved!"),

    ("Why don't scientists trust atoms?",
     "Because they make up everything!"),

    ("What do you call a pig that does karate?",
     "A pork chop!"),

    ("Why did the bicycle fall over?",
     "Because it was two tired!"),

    ("What's orange and sounds like a parrot?",
     "A carrot!"),

    ("Why did the student eat their homework?",
     "Because the teacher said it was a piece of cake!"),

    ("What do you call a sleeping bull?",
     "A bulldozer!"),

    ("Why don't skeletons fight each other?",
     "They don't have the guts!"),

    ("What did one wall say to the other wall?",
     "I'll meet you at the corner!"),

    ("What do you call a fake noodle?",
     "An impasta!"),

    ("Why can't you give Elsa a balloon?",
     "Because she'll let it go!"),

    ("What's a pirate's favorite letter?",
     "You'd think it's R, but it's the C!"),

    ("Why did the chicken join a band?",
     "Because it had the drumsticks!"),

    ("What do you call a snowman with a six-pack?",
     "An abdominal snowman!"),

    ("Why don't oysters share their pearls?",
     "Because they're shelfish!"),

    ("What did the left eye say to the right eye?",
     "Between you and me, something smells!"),

    ("Why did the scarecrow win an award?",
     "Because he was outstanding in his field!"),

    ("What do you call a dinosaur with an extensive vocabulary?",
     "A thesaurus!"),

    ("What did the zero say to the eight?",
     "Nice belt!"),

    ("Why was the broom late?",
     "It over-swept!"),

    ("What do you call a can opener that doesn't work?",
     "A can't opener!"),

    ("Why did the computer go to the doctor?",
     "Because it had a virus!"),

    ("What's a tornado's favorite game?",
     "Twister!"),

    ("Why did the music teacher need a ladder?",
     "To reach the high notes!"),

    ("What do you call a boomerang that won't come back?",
     "A stick!"),

    ("Why don't penguins like talking to strangers?",
     "They find it hard to break the ice!"),

    ("What did the limestone say to the geologist?",
     "Don't take me for granite!"),

    ("Why did the frog take the bus to work?",
     "Because his car got toad!"),

    ("What do you call a dancing sheep?",
     "A baa-llerina!"),

    ("Why did the golfer bring two pairs of pants?",
     "In case he got a hole in one!"),

    ("What's a computer's favorite snack?",
     "Microchips!"),

    ("Why did the sun go to school?",
     "To get a little brighter!"),

    ("What do you call a sleeping dinosaur?",
     "A dino-snore!"),

    ("Why don't mummies take vacations?",
     "They're afraid they'll relax and unwind!"),

    ("What did one plate say to the other?",
     "Dinner's on me!"),

    ("Why was the equal sign so humble?",
     "Because it knew it wasn't greater or less than!"),

    ("What do you call a belt made of watches?",
     "A waist of time!"),

    ("Why did the robot go on vacation?",
     "To recharge its batteries!"),

    ("What's a ghost's favorite fruit?",
     "Boo-berries!"),

    ("Why did the teacher wear sunglasses?",
     "Because her students were so bright!"),

    ("What do you call a fish wearing a crown?",
     "A king fish!"),

    ("What did the ocean say to the shore?",
     "Nothing, it just saved"),
]

class JokeMachine:
    def __init__(self):
        # Initialize I2C for OLED display
        self.i2c = SoftI2C(scl=Pin(I2C_SCL_PIN), sda=Pin(I2C_SDA_PIN))
        self.display = SSD1306_I2C(DISPLAY_WIDTH, DISPLAY_HEIGHT, self.i2c)

        # Initialize button with pull-up resistor
        self.button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

        # State management
        self.current_joke_index = 0
        self.showing_answer = False
        self.last_button_state = 1
        self.debounce_time = 0
        self.last_auto_change_time = time.ticks_ms()

    def wrap_text(self, text, max_width=14):
        """Wrap text to fit display width (approximately 16 chars per line)"""
        words = text.split()
        lines = []
        current_line = ""

        for word in words:
            if len(current_line) + len(word) + 1 <= max_width:
                current_line += word + " "
            else:
                if current_line:
                    lines.append(current_line.strip())
                current_line = word + " "

        if current_line:
            lines.append(current_line.strip())

        return lines

    def display_text(self, text, header=None):
        """Display text on OLED with optional header in yellow strip"""
        self.display.fill(0)

        # If header provided, create a banner in the yellow strip area
        start_y_content = 0
        if header:
            # Fill the top 16 pixels (yellow strip) to create solid banner
            self.display.fill_rect(0, 0, DISPLAY_WIDTH, 16, 1)
            # Display header text in black (inverted) by drawing in color 0
            # Center the text horizontally
            text_width = len(header) * 8  # Approximate width (8 pixels per char)
            x_pos = (DISPLAY_WIDTH - text_width) // 2
            # Draw inverted text by using framebuf's text with color 0 on filled area
            # We need to manually invert, so draw black text on white background
            for i, char in enumerate(header):
                char_x = x_pos + (i * 8)
                self.display.text(char, char_x, 4, 0)  # color 0 = black on white
            start_y_content = 16  # Start content below yellow strip

        # Split text by newlines if present
        if '\n' in text:
            lines = text.split('\n')
        else:
            lines = self.wrap_text(text)

        # Calculate starting Y position for vertical centering (below header)
        line_height = 10
        total_height = len(lines) * line_height
        available_height = DISPLAY_HEIGHT - start_y_content
        start_y = start_y_content + (available_height - total_height) // 2

        # Display each line
        for i, line in enumerate(lines):
            y_pos = start_y + (i * line_height)
            self.display.text(line, 0, y_pos)

        self.display.show()

    def show_question(self):
        """Display the current joke question"""
        question, _ = JOKES[self.current_joke_index]
        self.display_text(question, header="Question?")
        self.showing_answer = False

    def show_answer(self):
        """Display the current joke answer"""
        _, answer = JOKES[self.current_joke_index]
        self.display_text(answer, header="Answer")
        self.showing_answer = True

    def next_joke(self):
        """Move to the next joke (sequential or random based on config)"""
        if RANDOM_MODE:
            # Pick a random joke (avoid showing the same joke twice in a row)
            new_index = random.randint(0, len(JOKES) - 1)
            while new_index == self.current_joke_index and len(JOKES) > 1:
                new_index = random.randint(0, len(JOKES) - 1)
            self.current_joke_index = new_index
        else:
            # Sequential mode - wrap around
            self.current_joke_index = (self.current_joke_index + 1) % len(JOKES)
        self.show_question()

    def handle_button_press(self):
        """Handle button press with debouncing"""
        current_time = time.ticks_ms()

        # Read button state (0 = pressed due to pull-up)
        button_state = self.button.value()

        # Detect falling edge (button press) with debounce
        if button_state == 0 and self.last_button_state == 1:
            if time.ticks_diff(current_time, self.debounce_time) > 200:
                self.debounce_time = current_time
                # Reset auto timer when button is pressed
                self.last_auto_change_time = current_time

                if self.showing_answer:
                    # If showing answer, go to next joke
                    self.next_joke()
                else:
                    # If showing question, reveal answer
                    self.show_answer()

        self.last_button_state = button_state

    def handle_auto_mode(self):
        """Handle automatic cycling through jokes"""
        current_time = time.ticks_ms()
        elapsed = time.ticks_diff(current_time, self.last_auto_change_time)

        # Convert AUTO_DISPLAY_TIME to milliseconds
        auto_interval_ms = AUTO_DISPLAY_TIME * 1000

        if elapsed >= auto_interval_ms:
            self.last_auto_change_time = current_time

            if self.showing_answer:
                # If showing answer, go to next joke
                self.next_joke()
            else:
                # If showing question, reveal answer
                self.show_answer()

    def run(self):
        """Main loop"""
        # Show initial joke question
        self.show_question()

        mode_str = "AUTO" if AUTO_MODE else "BUTTON"
        order_str = "RANDOM" if RANDOM_MODE else "SEQUENTIAL"
        print(f"Joke Machine started in {mode_str} mode!")
        print(f"Loaded {len(JOKES)} jokes ({order_str} order)")
        if AUTO_MODE:
            print(f"Auto-cycling every {AUTO_DISPLAY_TIME} seconds")

        while True:
            # Always check for button press (works in both modes)
            self.handle_button_press()

            # In auto mode, also handle automatic cycling
            if AUTO_MODE:
                self.handle_auto_mode()

            time.sleep(0.01)  # Small delay to prevent busy-waiting


# Main entry point
if __name__ == "__main__":
    try:
        machine = JokeMachine()
        machine.run()
    except Exception as e:
        print(f"Error: {e}")
        # Try to show error on display if possible
        try:
            import sys
            sys.print_exception(e)
        except:
            pass
