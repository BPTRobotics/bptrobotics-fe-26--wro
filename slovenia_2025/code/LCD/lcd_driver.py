from RPLCD.i2c import CharLCD

# Create an LCD object using the correct I2C settings
lcd = CharLCD(
    i2c_expander='PCF8574',
    address=0x27,     # Change if your LCD is on a different address
    port=1,           # I2C bus number (1 on Pi)
    cols=16,          # Number of columns
    rows=2,           # Number of rows
    dotsize=8         # Character height (usually 8)
)

def init_lcd():
    """Clears the display and sets initial state."""
    lcd.clear()

def write_line(text, line=0):
    """Writes text to a given line."""
    lcd.cursor_pos = (line, 0)
    lcd.write_string(text.ljust(16))  # Pad to full width

def scroll_text(text, line=0, delay=0.2):
    """Scroll long text on specified line."""
    import time
    padded = text + " " * 16
    for i in range(len(padded) - 15):
        lcd.cursor_pos = (line, 0)
        lcd.write_string(padded[i:i+16])
        time.sleep(delay)
