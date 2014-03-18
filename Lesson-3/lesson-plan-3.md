## Lesson 3 - Getting Started with Python Programming 

###Introduction

This lesson will give an introduction to Python Programming by writing a simple program to gain user input, and then print statements to the screen. It is a step up from using a visual programing language and Scratch could be used instead.


### Learning Objectives

- Know that computers follow a sequence of instructions to make something happen.
- Understand how to use the Python Programming environment IDLE3.
- Be able to create and debug a simple computer program in Python using print and user input.


### Learning Outcomes

**All students are able to**

- Be able to write a simple Python Program and check that it works.


**Most students are able to:**

- Know that Python is a computer programming language.  
- Be able to write a simple Python Program, and explain the sequence it is following.

**Some stufents are able to:**

- Understand the limitations of computers in comparison with human intelligence when following a sequence of instructions. 


### Lesson Summary

- The first Python program

### Starter




### Main Development

1. Ask students to set up their Raspberry Pi equipment, turn it on and log into their Pi using the username `pi` and the password `raspberry`

	*Note that students will not see any text when typing the password but rest assured it is working. Why do you think this might be the case? Hint: What might happen if someone was looking over your shoulder?*
	
2. Next students should load the graphical user interface by typing `startx`. To use Python, students will need to access the programming environment, **IDLE3**. To open IDLE3, students can either double click on the IDLE3 icon on the desktop or click on the main menu and select Programming, followed by IDLE 3.

	![](idle3.png)

3. Demonstrate to students the IDLE interpreter window. Explain that commands can be typed directly into this window after the prompt which looks like this:  `>>>` This window is referred to as the interpreter or shell. You can type a line of code after this prompt and press enter. This will run that line of code. You can demonstrate this with `print("Hello World!")`. Ask students what they could replace the “Hello World” with. Have them experiment using the interpreter window for a few minutes. Explain that the computer can only follow one instruction at a time, in **sequence**. 

4. Explain to students that when you are writing many lines of code in a program it can become tiresome to use the interpreter and should you want to save your code, that it is better to use a text editor. Show students how to create a new text editor file by clicking on **File>New Window** from the menu at the top of the **IDLE3** window. Show students how to save this file, by clicking on **File>Save As** and naming it `name1.py`.

5. Ask students to type the following code into the test editor window. Point out the difference between a comment and a line of code. Also explain a string.

	```python
	
	# My Python Program by ....
	
	name = input('what is your name: '),
	print("Nice to meet you ", name)
	```

6. Students can then add their own input and print statements perhaps asking for the users age, or their favourite colour. For example adding:

	```python
	
	age = input('How old are you: ')
	print("You do not look like you are aged ", age)
	```

### Plenary



### Homework

Students should think of five questions that they would like their chatting robot to ask ready for the next lesson.
