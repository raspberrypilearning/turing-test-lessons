# Software Installation

## Downloading and installing espeak

1. After booting, log in using the default login `pi` and password `raspberry`.
2. On the command line type: `sudo apt-get install espeak`.
3. Press `Y` on the keyboard when prompted.

## Forcing sound to headphones

1. Ensure that your headphones are plugged into the sound jack port on the Raspberry Pi.
2. After booting and logging in you can type the following line on the command line: `amixer cset numid=3 1`.
3. Alternatively you can load the desktop by typing `startx`, double-clicking on the **Python Games** icon, selecting **Force headphones** and clicking **OK**.

	![](lesson-3/images/audio_output.png)
