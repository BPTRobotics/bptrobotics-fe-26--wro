from . import lcd_driver  
import time

lcd = lcd_driver.lcd  



rocket_right = [
    0b00000,
    0b10000,
    0b11110,
    0b11111,
    0b11111,
    0b11110,
    0b10000,
    0b00000
]


dust = [
    0b00000,
    0b00000,
    0b00000,
    0b01011,
    0b01011,
    0b00000,
    0b00000,
    0b00000
]

up_arrow = [
    0b01110,
    0b00100,
    0b00100,
    0b00100,
    0b00100,
    0b11111,
    0b01110,
    0b00100
]

down_arrow = [
    0b00100,
    0b01110,
    0b11111,
    0b00100,
    0b00100,
    0b00100,
    0b00100,
    0b00100
]

right_arrow = [
    0b00100,
    0b01000,
    0b10000,
    0b11111,
    0b10000,
    0b01000,
    0b00100,
    0b00000
]


lcd.create_char(0, rocket_right)
lcd.create_char(1, dust)
lcd.create_char(2, up_arrow)
lcd.create_char(3, down_arrow)
lcd.create_char(4, right_arrow)

def clear_screen():
    lcd_driver.write_line(' ' * 16, line=0)  
    lcd_driver.write_line(' ' * 16, line=1)

def rocket_fly_async(stop_event):
    rocket_slot = 0
    dust_slot = 1
    while not stop_event.is_set():
        for row in range(1, -1, -1):
            for col in range(16):

                
                lcd.cursor_pos = (row, col)
                lcd.write_string(chr(rocket_slot))

                
                if col > 0:
                    lcd.cursor_pos = (row, col-1)
                    lcd.write_string(chr(dust_slot))

                time.sleep(0.05)
            lcd_driver.write_line(' ' * 16, line=row)  

    lcd_driver.write_line(' ' * 16, line=0)  
    lcd_driver.write_line(' ' * 16, line=1)  

def up_arrow():
    lcd.cursor_pos = (0, 15)
    lcd.write_string(chr(2))

def down_arrow():
    lcd.cursor_pos = (1, 15)
    lcd.write_string(chr(3))

def right_arrow():
    lcd.cursor_pos = (1, 15)
    lcd.write_string(chr(4))