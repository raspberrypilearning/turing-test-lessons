# My Python Program by ...
import os, time

def robot(text):
    os.system("espeak '" + text + "'")

robot("Hello")

time.sleep(1)              

robot('What is your name')
name = input('What is your name: ')           
robot("Nice to meet you " + name)

time.sleep(1)

robot("How old are you")
age = input('How old are you: ')
robot("You do not look like you are aged " + age)

