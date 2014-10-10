# Lesson 1 - How Do Computers Think? 

##Introduction

How do computers think? In this lesson, students will consider how computers and robots need to follow a sequence of instructions to complete a task. Much of this lesson is dedicated to getting students using a Raspberry Pi for the first time, logging in, accessing IDLE3, and typing a small sequence of instructions to make a shape.

## Learning objectives

- Know that computers follow a sequence of instructions to make something happen.
- Be able to set up a Raspberry Pi, and give a set of instructions in Python to make a shape.


## Learning outcomes

###All students are able to:

- Know that computers run programs that are a sequence of instructions to make something happen. 
- Write a simple program. 

###Most students are able to:

- Know that Python is a computer programming language.  
- Write a simple Python program and explain the sequence it is following.

###Some students are able to:

- Write a program to create a more complex shape.


## Lesson summary

- An introduction to the basic physical parts of a Raspberry Pi
- A demonstration that the Raspberry Pi can behave like a traditional computer
- The first Python program

## Starter

First nominate three or four students to act as robots, then divide the remaining students into three or four teams. Each team are in a race to see who can get a 'robot' around the classroom or 'maze'. Note that this could be an outdoor task. Explain to the 'robots' that they are to play dumb and only follow the instructions they are given. Then, begin the race.

Throughout the race, ensure that students are using instructions like "step forward 10 paces" or "turn 90 degrees to the right".

After the race has been won, discuss any problems the teams encountered getting their robot to follow their instructions. Draw out through questioning that the robot could not make decisions for itself, and so the students had to be very specific about turns and steps.

Explain that a computer works by executing statements one after another in a specific order. A given order of statements is called a **program**. Each program executes with a given **control flow** ; this describes which statement we are executing, and what the next statement will be.

## Main development

1. Have a demonstration Raspberry Pi already connected and the final chatting robot program running. Hold up a Raspberry Pi board and ask the students what they think it is. Explain that it’s actually a computer and that in the coming lessons we’re going to do something special with it. Instead of running apps and games other people have created for us, we’re going to learn to write our own software to make a robot that chats to us.

2. Start with all the parts of the Raspberry Pi on a table: keyboard, mouse, speaker, memory card, power supply, monitor, monitor cable and the Raspberry Pi itself. Ask the class to name and describe each component as you connect it to the Raspberry Pi in front of the class. Finally, plug in the power and watch it boot up. An alternative demonstration would be to leave out the memory card and attempt to boot the Pi, which will fail. You can then describe the memory card as something that contains instructions to tell the Raspberry Pi how to start. The Raspberry Pis should all be booted and sitting on the login prompt waiting for authentication.

2. Ask students to set up their Raspberry Pi equipment, turn it on and log into their Pi using the username `pi` and the password `raspberry`.

	*Note that students will not see any text when typing the password but assure them it is working. Why do they think this might be the case? Hint: what might happen if someone was looking over their shoulder?*
	
3. Next, students should load the graphical environment by typing `startx`. Once the desktop has loaded, show students how to open **IDLE3** either by double-clicking on the desktop icon, or by clicking on the **Main Menu** followed by **Education** and selecting **IDLE3**.
	
	*Note that this series of lessons uses Python 3. If students run IDLE then their code may not run.*

4. Explain to students that **IDLE3** is an application or environment that allows you to write a simple program using the programming language **Python**. It allows you to write, edit and run code. 

5. Show students how to draw a shape by typing a sequence of instructions, line by line. See the [Student Instructions](student-instructions-1.md) for the steps required to complete this task.

6. Ask students to shut down their Raspberry Pis by clicking on the **Shut Down** icon on the desktop. 

## Plenary

Write the following list of words on the board:

- Instructions
- Sequence
- Raspberry Pi
- Python
- IDLE3

Select a student randomly from the class. They must select one of the words from the board, stand up and point to someone else in the class who must then give the meaning of the word. That person then chooses the next person to give a word to.

## Homework

Students should write a sequence of instructions for a task, such as getting dressed for school or their favourite dance moves.

