"""
Task 1: Display numbers 1, 2, 3 on the micro:bit LED matrix.
Run this on the micro:bit (MicroPython), or adapt to your lab IDE.
"""

from microbit import *

def show_number(n, duration_ms=1000):
    """Show a single digit on the LED matrix."""
    display.show(str(n))
    sleep(duration_ms)


def main():
    display.scroll("LED")
    for number in (1, 2, 3):
        show_number(number)
    display.clear()


main()
