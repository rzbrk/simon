"""
    Example program to output an animated face
    to a ILI9341 display (320x240 pixel) connected
    to the SPI0 interface of a Raspberry Pi single
    board computer. Tested with Raspberry Pi 3.
"""

import time
from threading import Thread

import digitalio
import board
from adafruit_rgb_display import ili9341

import face

ani_run = False
ani_upd_per = 1.0 # seconds

# Define the pins the display is connected to
cs_pin = digitalio.DigitalInOut(board.D23)
dc_pin = digitalio.DigitalInOut(board.D24)
reset_pin = digitalio.DigitalInOut(board.D25)
spi_baudrate = 24000000

# Create instance for display connected via SPI
disp = ili9341.ILI9341(
    spi=board.SPI(),
    rotation=90,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=spi_baudrate,
)

# Create face object
face = face.Face()

def ani_thread():
    while ani_run:
        # Time at start of loop
        t0 = time.time()

        # Update face frame
        face.update()

        # Output face frame to display
        disp.image(face.frame)

        # Wait until update period has passed
        dt = ani_upd_per - (time.time() - t0)
        if dt > 0:
            time.sleep(dt)

def animate(stop = False):
    global ani_run

    if stop:
        ani_run = False
    else:
        if not ani_run:
            ani_run = True
            a = Thread(target=ani_thread, daemon=True)
            a.start()


