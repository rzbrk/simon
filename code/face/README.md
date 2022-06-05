# face

## Purpose
This code generates a face that can be outputted to either a file or a
ILI9341 color display with 320x240 pixeln connected via SPI.
The face can be also animated producing random eye moving and blinking.

## Usage
### Output to display
#### Connection of display to Raspberry Pi GPIO

Connect the ILI9341 display to the Raspberry Pi GPIO according to the following
table.

| ILI9341 Pin | RPi GPIO | Note |
|-------------|----------|------|
| GND | GND | |
| VCC | 3.3V | |
| MOSI | SPI0_MOSI (GPIO10) | |
| MISO | SPI0_MISO (GPIO9) | |
| SCLK | SPI0_CLK (GPIO11) | |
| CS | GPIO_GEN4 (GPIO23) | ILI9341 Chip select |
| CD | GPIO_GEN5 (GPIO24) | ILI9341 Command/Data |
| Reset | NC | |

#### Execution of Python code
If not already done, install Python virtual environment:

    $ pipenv install

Launch Python shell from within Python virtual environment:

    $ pipenv run python

Within the Python shell start face animation:

    >>> import face
    >>> f = face.Face(outdev="display")
    >>> f.animate()

Now, you can e.g. move the eyes (pupils):

    >>> f.pup_pos_hor=-1 	# Looking left
    >>> f.pup_pos_hor=1 	# Looking right
    >>> f.pup_pos_vert=-1	# Looking up
    >>> f.pup_pos_vert=0	# Looking straight

You can also set the mood:

    >>> f.mood="sad"
    >>> f.mood="happy"
    >>> f.mood="surprised"

### Output to file
If not already done, install Python virtual environment:

    $ pipenv install

Launch Python shell from within Python virtual environment:

    $ pipenv run python

Within the Python shell start face animation. The default output file
is ``face.png`` in the current working directory:

    >>> import face
    >>> f = face.Face(outdev="file")
    >>> f.animate()

Now, you can e.g. move the eyes (pupils):

    >>> f.pup_pos_hor=-1 	# Looking left
    >>> f.pup_pos_hor=1 	# Looking right
    >>> f.pup_pos_vert=-1	# Looking up
    >>> f.pup_pos_vert=0	# Looking straight

You can also set the mood:

    >>> f.mood="sad"
    >>> f.mood="happy"
    >>> f.mood="surprised"

