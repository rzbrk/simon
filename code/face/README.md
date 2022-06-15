# face

## Purpose
This code generates a face that can be outputted to either a file or a
ILI9341 color display with 320x240 pixeln connected via SPI.
The face can be also animated producing random eye moving and blinking.

## Usage
### Output to ILI9341 display connected to Raspberry Pi
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

Tested with Raspberry Pi 3 single board computer.

#### Execution of Python code
If not already done, install Python virtual environment:

    $ pipenv install

Run the example program:

    $ pipenv run python rpi_display_output.py

### Output to file
If not already done, install Python virtual environment:

    $ pipenv install

Run the example program:

    $ pipenv run python file_output.py

In the file ``file_output.py`` the variables ``outfile`` and ``append_counter``
can be adjusted. With ``append_counter = True`` to each output filename a
counter will be added that is incremented for every frame. This way, the set of
files can be used to create an video or animated gif, e.g. using ffmpeg:

    $ cd out/
    $ ffmpeg -framerate 1 -i face_%8d.png face.gif

