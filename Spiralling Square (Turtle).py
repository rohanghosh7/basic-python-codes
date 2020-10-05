# ______ If you don't have Python installed, use https://repl.it/languages/python_turtle to run your code :) _______

from turtle import *
speed(10)                         # use 10 as parameter of speed() to get a slower turtle for catching your turtle drawing 
pencolor(255,0,255)               # RGB coordinates of the color 'magenta'
                                  # you can use RGB codes like pencolor(139,0,139) for darkmagenta
fd(175)                           # turtle goes forward by 175 units or pixels
lt(90)                            # turtle turns left by 90 degrees
fd(175)                           # again, turtle goes forward by 175 units or pixels
lt(90)                            # again, turtle turns left by 90 degrees
for i in range (170,0,-5):        # for loop to get the spiralling action by cutting off edges of the square at each instance
  fd(i)
  lt(90)
  fd(i)
  lt(90)
