# face

## Usage
### Output to ILI9341 display connected to Raspberry Pi
#### Connection of display to Raspberry Pi GPIO

Connect the ILI9341 display to the Raspberry Pi GPIO according to the following
table.

| ILI9341 Pin | RPi GPIO | Note |
|-------------|----------|------|
| GND | GND | |
| VCC | 3.3V | |
| LED | 3.3V | Brightness could be adjusted by using PWM-enabled output |
| MOSI | SPI0_MOSI (GPIO10) | |
| MISO | SPI0_MISO (GPIO9) | |
| SCLK | SPI0_CLK (GPIO11) | |
| CS | GPIO_GEN4 (GPIO23) | ILI9341 Chip select |
| CD | GPIO_GEN5 (GPIO24) | ILI9341 Command/Data |
| Reset | NC | |

Tested with Raspberry Pi 3 single board computer.

#### Execution of Python code
If not already done, install Python virtual environment:

    $ pipenv install

Start the python virtual environment (shell):

    $ pipenv run python

In the python shell load and execute the example script:

    >>> exec(open("rpi_display_output.py").read())

Then start the animation on the display by calling the function ``animate()``:

    >>> animate()

You should see the animation on the display. If not, check the wiring and redo
the instructions above.

You can interact with the face by adjusting the attributes of the instance
``face``.

Examples:

    >>> face.pup_pos_hor = -0.9     # look left
    >>> face.pup_pos_hor = 0.9      # look right
    >>> face.pup_pos_hor = 0        # look straight
    >>> face.pup_pos_vert = -0.9    # look up

The attributes ``face.pup_pos_hor`` and ``face.pup_pos_vert`` can be combined
to let the SIMON face look diagonal.

    >>> face.eye_right_closed = 0.9 # close right eye
    >>> face.eye_right_closed = 0   # open right eye

Default is having eyes closed with ``face.eye_[right,left]_closed = 0.2``.

    >>> face.mood = "sad"
    >>> face.mood = "happy"

    >>> face.ani_talk = True        # Enable opening/closing mouth
    >>> face.ani_talk = False       # Disable talking animation

