#!/bin/env python3

import time
import digitalio
import board
from adafruit_rgb_display import ili9341

import face

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

try:
    print("Press Ctrl+c to exit.")
    while True:
        # Time at start of loop
        t0 = time.time()

        # Update face frame
        face.animation_thread()

        # Output face frame to display
        disp.image(face.face)

        # Wait until update period has passed
        dt = ani_upd_per - (time.time() - t0)
        if dt > 0:
            time.sleep(dt)

except KeyboardInterrupt:
    print("Exiting loop.")
    exit
