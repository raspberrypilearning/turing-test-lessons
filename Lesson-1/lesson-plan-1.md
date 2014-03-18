## Lesson 1 - Getting Started with Python Programming 

###Introduction

This lesson will give an introduction to Python Programming by writing a simple program to gain user input, and then print statements to the screen. It is a step up from using Scratch but this could translated for Scratch instead.


### Learning Objectives

- Know that computers follow a sequence of instructions to make something happen.
- Understand how to use the Python Programming environment IDLE3.
- Be able to create and debug a simple computer program in Python using print and user input.


### Learning Outcomes

**All students are able to**

- Know that computers run programs that are a sequence of instructions to make something happen. 
- Be able to write a simple Python Program and check that it works.


**Most students are able to:**

- Know that Python is a computer programming language.  
- Be able to write a simple Python Program, and explain the sequence it is following.

**Some stufents are able to:**

- Understand the limitations of computers in comparison with human intelligence when following a sequence of instructions. 


### Lesson Summary

- An introduction to the basic physical parts of a RPi
- A demonstration that the RPi can behave like a traditional computer application
- The first Python program

### Starter

Have a demonstration Raspberry Pi already connected and final chatting robot program running. Hold up an RPi board and ask the students what they think it is. Explain that it’s actually a computer and that in the coming lessons we’re going to do something special with it. Instead of running apps and games other people have created for us, we’re going to learn to write our own software - to make a robot that chats to us.

Direct students to a website containing a chat bot, or display a website with a chat bot to the class, e.g [Elbot](http://www.elbot.com/). You could even use siri on an Apple OS device. Through intereacting with the chat bot do students think that computers think for themselves?

Draw out from questioning that computers execute or run programs that follow a sequence of instructions, and that they can only follow this sequence. 


### Main Development

1. Start with all the parts of the Raspberry Pi on a table: keyboard, mouse, speaker, memory card, power supply, monitor, monitor cable and RPi itself. Ask the class to name and describe each component as you connect it to the RPi in front of the class. Finally, plug in the power and watch it boot up. An alternative to this demonstration is to leave out the memory card and try and boot it to no avail. It should then be possible to describe the memory card as something that contains instructions to tell the RPi how to start. The RPis should all be booted and sitting on the login prompt waiting for authentication.

2. Ask students to set up their Raspberry Pi equipment, turn it on and log into their Pi using the username `pi` and the password `raspberry`

	*Note that students will not see any text when typing the password but rest assured it is working. Why do you think this might be the case? Hint: What might happen if someone was looking over your shoulder?*
	
3. Next students should load the graphical user interface by typing `startx`. To use Python, students will need to access the programming environment, **IDLE3**. To open IDLE3, students can either double click on the IDLE3 icon on the desktop or click on the main menu and select Programming, followed by IDLE 3.

	![](idle3.png)

4. Demonstrate to students the IDLE interpreter window. Explain that commands can be typed directly into this window after the prompt which looks like this:  `>>>` This window is referred to as the interpreter or shell. You can type a line of code after this prompt and press enter. This will run that line of code. You can demonstrate this with `print("Hello World!")`. Ask students what they could replace the “Hello World” with. Have them experiment using the interpreter window for a few minutes. 

5. Explain to students that when you are writing many lines of code in a program it can become tiresome to use the interpreter and should you want to save your code, that it is better to use a text editor. Show students how to create a new text editor file by clicking on **File>New Window** from the menu at the top of the **IDLE3** window. Show students how to save this file, by clicking on **File>Save As** and naming it `name1.py`.

6. Ask students to type the following code into the test editor window. Point out the difference between a comment and a line of code. Also explain a string.

	```python
	
	# My Python Program by ....
	
	name = input('what is your name: '),
	print("Nice to meet you ", name)
	
	```

7. Students can then add their own input and print statements perhaps asking for the users age, or their favourite colour. For example adding:

	```python
	
	age = input('How old are you: ')
	print("You do not look like you are aged ", age)
	
	```

### Plenary

Groups should be invited to choose card orderings for other groups to act out. Following this, a discussion should be held about how this relates to a computer. A computer works by executing statements one after another in a specific order. A given order of statements is called a **program**. Each program executes with a given **control flow** which describes which statement we are executing and what the next statement will be.

### Homework



