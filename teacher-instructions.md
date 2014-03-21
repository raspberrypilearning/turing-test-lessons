## Teacher Setup Instructions

For this scheme of work students will need access to:

- A Raspberry Pi
- A keyboard and mouse connected to the RPi
- A monitor connected to the RPi
- Latest NOOBS SD card with Raspbian installed (instructions below)
- espeak downloaded and installed on each SD card (instructions below)

For lesson 3 students will need this additional equipment:

- A headphone splitter connected to the RPi audio jack if students are working in pairs on one RPi
- A pair of headphones connected to the splitter or RPi per student.


### Downloading and installing NOOBS

Instructions for best practice on [downloading and installing NOOBS can be read here](https://github.com/raspberrypi/documentation/blob/master/installation/noobs.md).


### Downloading and installing espeak

1. After booting, log in using the default log in `pi` and password `raspberry`.
2. On the command line type: `sudo apt-get install espeak`.
3. Press `Y` on the keyboard when prompted.


### Forcing sound to headphones

1. Ensure that your headphones are plugged into the sound jack port on the Raspberry Pi.
2. After booting and logging in you can type the following line on the command line: `amixer cset numid=3 1`.
3. Alternatively you can load the desktop by typing `startx` and double clicking on the **Python Games** icon, and select **Force headphones** and click **OK**.

	![](Lesson-3/audio_output.png)
	
### Making a class set of SD cards

Once you have completed the steps above, you are able to make a copy of your master SD card and then use that to make a class set.

1. Place your master SD card in a computer or laptop with an SD card reader. 
2. On windows use [Win disk 32 imager](http://sourceforge.net/projects/win32diskimager/) to make a copy of an SD card. On MAC OSX you can use the `dd` command or a [dd-gui](http://www.gingerbeardman.com/dd-gui/).
3. Remove the master SD card and keep it safe.
4. Take a fresh SD card and insert it into your computer or laptop. 
5. Format the SD card then using your imaging software, select the image and write it to the card.
6. Repeat the last step for the rest of your cards. 