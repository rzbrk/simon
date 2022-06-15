# Voice Recognition

## Purpose
Testing of Elechouse voice recognition module v3.

## Preparation
### Connection to Arduino

Connect the Elechouse voice recognition module to the Arduino Mega Pro module
accordin to the folowing table:

| VR module | Arduino |
|-----------|---------|
| GND | GND |
| VCC | 5V |
| RXD | D11 |
| TXD | D10 |

Note: The pins D2,D3 do not work with Arduino Mega. The serial communication is
unreliable. Some commands do not work. See:
https://github.com/elechouse/VoiceRecognitionV3/issues/4#issuecomment-285676380.

### Configuration and installation of necessary software tools and libraries
Install and prepare [arduino-cli](https://github.com/arduino/arduino-cli):

    $ mkdir -p ~/.local/bin
    $ curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | BINDIR=~/.local/bin sh
    $ echo "export PATH=$PATH:~/.local/bin" >> ~/.bashrc
    $ source ~/.bashrc
    $ arduino-cli core update-index
    $ arduino-cli core install arduino:avr
    $ arduino-cli core install arduino:megaavr

Install [Elechouse libraries](https://github.com/elechouse/VoiceRecognitionV3)
and examples for the voice recognition module:

    $ mkdir -p ~/Arduino/libraries
    $ cd Arduino/libraries
    $ git clone https://github.com/elechouse/VoiceRecognitionV3.git

Compile and upload sample sketch:

    $ cp -r libraries/VoiceRecognitionV3/examples/vr_sample_train/ .
    $ arduino-cli compile --fqbn arduino:avr:mega vr_sample_train
    $ arduino-cli upload --port /dev/ttyUSB0 --fqbn arduino:avr:mega vr_sample_train

#Train and load records
So far, only the terminal monitor of the Arduino IDE seems to be able to
establish a working connection to the serial interface of the firmware on the
Arduino Mega.

| Tool | Working? | Remarks |
|------|----------|---------|
| miniterm | no | tried all settings for eol (CR,LF,CRLF) |
| picocom | no | tried various arguments for --omap |
| screen | no | command: ``screen /dev/ttyUSB0 115200`` |
| Arduino IDE serial monitor | yes | Enable sending with newline |

The module is capable of being trained to 255 voice commands (records), each
1500 ms long. To list the training status of all records enter the following
command:

    record

To train a voice command select a storage position N (0 - 254) and type in the
following command:

    train N

Follow the commands at the command line. The voice commands has to be spoken at
least 2 times. To verify that the voice command was trained successfully, enter
the following command:

    record N

To test the recognition of the voice command enter the following command:

    load N

Now, speak the command into the microphone and follow the serial output.

