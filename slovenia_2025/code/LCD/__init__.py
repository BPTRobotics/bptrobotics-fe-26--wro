from . import lcd_driver
from .lcd_driver import write_line, scroll_text
from .mode_manager import set_mode

lcd_driver.init_lcd()
