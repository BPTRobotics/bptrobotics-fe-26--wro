from threading import Thread, Event
from .custom_characters import rocket_fly_async, up_arrow, down_arrow, right_arrow, clear_screen
from .lcd_driver import write_line

stop_event = Event()
loading_thread = Thread(target=rocket_fly_async, args=(stop_event,), daemon=True)

def safe_stop_lodading_thread():
    global loading_thread
    if loading_thread.is_alive():
        stop_event.set()
        loading_thread.join()

def set_mode(mode):
    if mode == 0:
        safe_stop_lodading_thread()
        clear_screen()
    elif mode == 1:
        loading_thread.start()
    elif mode == 2:
        safe_stop_lodading_thread()
        clear_screen()
        up_arrow()
    elif mode == 3:
        safe_stop_lodading_thread()
        clear_screen()
        down_arrow()
    elif mode == 4:
        safe_stop_lodading_thread()
        clear_screen()
        write_line("PAUSED")
    elif mode == 5:
        safe_stop_lodading_thread()
        clear_screen()
        right_arrow()
