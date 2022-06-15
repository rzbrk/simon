# Voice Generation

Voice audio output can be generated using already existing tools under Linux
distributions. For project SIMON, the speech synthesizer [eSpeak NG](https://github.com/espeak-ng/espeak-ng) can be used. Voice output in different languages are possible.

## Installation and Configuration

    # apt install alsa alsa-tools espeak espeak-ng

Now, adjust sound volume with alsamixer to ~ 12 dB. Now, test general audio
output:

    $ aplay /usr/share/sounds/alsa/Front_Center.wav

## Test of voice output

English:

    $ espeak "Hi, I am SIMON. How are you?"

German:

    $ espeak -vde "Hallo, ich bin SIMON. Wie geht es Dir?"


