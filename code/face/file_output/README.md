# face

## Purpose
This code generates a face that can be outputted to either a file or a
ILI9341 color display with 320x240 pixel connected via SPI.
The face can be also animated producing random eye moving and blinking.

## Usage
### Output to file
If not already done, install Python virtual environment:

    $ pipenv install

Start the python virtual environment (shell):

    $ pipenv run python

In the python shell load and execute the example script:

    >>> exec(open("rpi_display_output.py").read())

Then start the animation by calling the function ``animate()``:

    >>> animate()

The animation can be stopped by the following command:

    >>> animate(stop=True)

In the file ``file_output.py`` the variables ``outfile`` and ``append_counter``
can be adjusted. With ``append_counter = True`` to each output filename a
counter will be added that is incremented for every frame. This way, the set of
files can be used to create an video or animated gif, e.g. using ffmpeg:

    $ cd out/
    $ ffmpeg -framerate 1 -i face_%8d.png face.gif

If teh file ``file_output.py`` is changes, reload the file with the
``exec`` command above to let the changes take effect.

Example output:

![SIMON face](./../face.gif)<br>
SIMON animated face
