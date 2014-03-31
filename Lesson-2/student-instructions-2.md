# Student Instructions 2

## Connecting your Raspberry Pi

The Raspberry Pi is a bare bones computer. It’s not much use on its own. In order to program a chatting robot with it, we need to connect a number of things to it:

- **An SD card**. This card contains the programs that can be loaded onto the Raspberry Pi in order for it to do things. You need to slide the card into the slot with the metal pins facing in towards the Raspberry Pi. The label should be visible when it is inserted.
- **A keyboard**. Plug the keyboard into one of the two USB ports. USB stands for Universal Serial Bus. It’s a kind of connector for all sorts of devices. The keyboard will be the main tool we will use to communicate our programs to the Raspberry Pi.
- **A mouse**. Plug the mouse into the other of the two USB ports.
- **A sound splitter**. This is a cable that will split the audio signal two ways. Plug this into the
audio jack on the Raspberry Pi.
- **Headphones**. These will allow you to hear the sound you will produce. Plug these into the sound splitter.
- **A monitor**. This will allow you to see the program you’re currently creating. Plug the HDMI connector into the Raspberry Pi’s HDMI port. Plug the other end of the HDMI cable into your monitor. You’ll want to make sure you have power to the monitor, that it’s switched on and that it’s set to view what comes in on the HDMI cable (typically the digital option).
- **A power adaptor**. Plug the power adaptor into a socket and then the small USB connector into the Raspberry Pi. When you turn the socket switch on, you should see the Raspberry Pi flash and text should appear on the monitor.

## Logging in

1. Once the Raspberry Pi has completed booting and the text has stopped whirring past on the screen, you’ll be greeted with a simple prompt for your username. 
2. Type `pi` and then press **Enter**. 
3. Next, you’ll be asked for your password. Type `raspberry` and press **Enter** again. Don’t worry that you don’t see the password on the screen as you type it. This is a security feature to stop people snooping over your shoulder and stealing your password. You should now be greeted with a strange text prompt.

## Starting the graphical environment

The strange text prompt that you see is one of the most powerful ways to communicate with a computer. However, it’s not very easy and is full of strange arcane commands, much like the contents of a magic spell. We can therefore move to a more familiar graphical environment, with windows and menu bars, that may perhaps feel a bit more comfortable. To do this, type the magic spell `startx` into the text terminal and press **Enter**.

## Starting the Python 3 programming environment

Once the graphical environment has started, you can click on the **start menu** in the bottom left (it looks like a little bird) and choose **IDLE3** from the **Programming menu**. 

![](idle3.png)

## Writing a simple program

You are going to write a program to ask the user some questions and respond to them.

1. Start by opening a new text editor window by clicking on **File** and **New Window**.

2. Type the following code into your new window remembering to add your name:

	
	```python
	
	# My Python Program by ....
	
	name = input("what is your name: ")
	print("Nice to meet you ", name)
	```
	
	**Note that the spaces before `"` in the string are important.**
	
	Save the file as a Python file by clicking on **File** then **Save As**, and name it **robot**.
	
	Then run the file by clicking on **Run** then **Run Module**.
	
	![](program-1.png)
	
	What happened?
	

3. Now add your own input and `print` statements, perhaps asking for the user's age or their favourite colour. For example, you could add:

	```python
	
	age = input("How old are you: ")
	print("You do not look like you are aged ", age)
	```
	
	**Don't forget to save and test your code after each question.**
	
	![](program-2.png)
	
4. In a conversation there is usually a pause between answering a question and asking the next one. The goal is to create a chatting robot that might be confused for a real person; therefore, we need to place a pause in between the questions. This can be achieved using the `time` module.

	
	Add the module by typing `import time` underneath the comment at the top of the program and before the questions. Then between the questions type `time.sleep(1)`, where the value `1` represents 1 second, like this:
	
	```python
	# My Python Program by...
	import time
	
	name = input("What is your name")
	print("Nice to meet you ", name)
	
	time.sleep(1)
	
	age = input("How old are you: ")
	print("You do not look like you are aged ", age)
	```

	![](program-3.png)
