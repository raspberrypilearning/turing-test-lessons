# Student Instructions 1

## Connecting your Raspberry Pi

The Raspberry Pi is a bare bones computer. It’s not much use on its own. In order to program sounds with it, we need to connect a number of things to it:

- **An SD card**. This card contains the programs that can be loaded onto the Raspberry Pi in order for it to do things. You need to slide the card into the slot with the metal pins facing in towards the Raspberry Pi. The label should be visible when it is inserted.
- **A keyboard**. Plug the keyboard into one of the two USB ports. USB stands for Universal Serial Bus. It’s a kind of connector for all sorts of devices. The keyboard will be the main tool we will use to communicate our programs to the Raspberry Pi.
- **A mouse**. Plug the mouse into the other of the two USB ports.
- **A sound splitter**. This is a cable that will split the audio signal two ways. Plug this into the
audio jack on the Raspberry Pi.
- **Headphones**. These will allow you to hear the sound you will produce. Plug these into the sound splitter.
- **A monitor**. This will allow you to see the program you’re currently creating. Plug the HDMI connector into the Raspberry Pi’s HDMI port. Plug the other end of the HDMI cable into your monitor. You’ll want to make sure you have power to the monitor, that it’s switched on and that it’s set to view what comes in on the HDMI cable (typically the digital option).
- **A power adaptor**. Plug the power adaptor into a socket and then the small USB connector into the Raspberry Pi. When you turn the socket switch on, you should see the Raspberry Pi flash and text should appear on the monitor.

## Logging In

1. Once the Raspberry Pi has completed booting and the text has stopped whirring past on the screen, you’ll be greeted with a simple prompt for your username. 
2. Type `pi` and then press **Enter**. 
3. Next, you’ll be asked for your password. Type `raspberry` and press **Enter** again. Don’t worry that you don’t see the password on the screen as you type it. This is a security feature to stop people snooping over your shoulder and stealing your password. You should now be greeted with a strange text prompt.

## Starting the Graphical Environment

The strange text prompt that you see is one of the most powerful ways to communicate with a computer. However, it’s not very easy and is full of strange arcane commands, much like the contents of a magic spell. We can therefore move to a more familiar graphical environment, with windows and menu bars, that may perhaps feel a bit more comfortable. To do this, type the magic spell `startx` into the text terminal and press **Enter**.

## Starting the Python 3 Programming Environment

Once the graphical environment has started, you can click on the **start menu** in the bottom left (it looks like a little bird) and choose **IDLE3** from the **Programming menu**. 

![](idle3.png)

## Writing a Simple Program

You are going to write a program to make a drawing of a shape.

1. Next to the three arrows `>>>` or prompt type: 

	```python
	import turtle
	```
	Then press **Enter**.
	
2. At the next `>>>` or prompt type:

	```python
	robot = turtle.Turtle()
	```
			
	This command opens the Turtle Graphics window with an arrow in the middle. This is your turtle, called robot, and you can give it instructions to move.
	
3. Let's make it look more like a robot turtle by typing:

	```python
	robot.shape("turtle")
	```

4. To instruct your robot turtle to move type:

	```python
	robot.forward(100)
	robot.right(90)
	```
	
	What happens? What more would you need to type to make a square shape?		
	![](robot-turtle.png)
