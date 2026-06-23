from .lcd_driver import init_lcd, write_line, scroll_text
import time

def main():
    init_lcd()
    write_line("BPTRobotics Test", line=0)
    write_line("Starting...", line=1)
    time.sleep(2)

    while True:
        # Scroll on line 0
        scroll_text("Scrolling on Line 1 -->", line=0, delay=0.15)
        time.sleep(1)

        # Scroll on line 1
        scroll_text("Scrolling on Line 2 -->", line=1, delay=0.15)
        time.sleep(1)

        # Scroll both lines alternately
        scroll_text("Upper line test [BPT]", line=0, delay=0.15)
        scroll_text("Lower line test [LCD]", line=1, delay=0.15)
        time.sleep(1)

        # Alternating between lines
        for i in range(2):
            scroll_text("BPTRobotics Rocks!", line=i, delay=0.1)
            time.sleep(0.5)

        write_line("Test Done", line=0)
        write_line("All OK", line=1)

        time.sleep(3)

if __name__ == '__main__':
    main()
