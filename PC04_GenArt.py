#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 18:11:08 2021
@author: Caroline Holzapfel and Maggie Paul
"""
# We used for loops to create a range of circles filled and unfilled,
# with different colors, and pensizes. This was to create a bubble effect 
# with our generative art. We took Jacquie Silvern's psuedocode idea of 
# Olympic Rings and decided to take the idea of colorful circles a step
#further.


import turtle, random, math
from random import randint 

turtle.colormode(255)
turtle.tracer(0)
turtle.speed(1)

panel = turtle.Screen()
w = 600
h = 600
panel.setup(width=w, height=h)

panel.bgcolor(0,0,0) # background color black


palette = ["DarkSeaGreen","coral1","CornflowerBlue","LightPink"]
pPalette = ["gray70", "LightBlue3","MediumPurple","linen"]

fillCircle = turtle.Turtle() # turtle is a filled in circle of various sizes, and colors


fillCircle.begin_fill()

for i in range(35):  # for loop in psuedo pattern, in order to make filled circle
    fillCircle.color(random.choice(palette)) # random choice of colors from palette
    fillCircle.pensize(1+i)
    for i in range(35):
        fillCircle.begin_fill()
        fillCircle.circle(10+5)
    fillCircle.end_fill()
    fillCircle.penup()
    fillCircle.goto(random.randint(-300,300),random.randint(-300,300)) 
    # random randint for location in order to allow circles to be all over the panel
    fillCircle.pendown()
    

circle = turtle.Turtle() # turtle is a non filled in circle of various sizes,colors and pensizes
circle.pendown()


for i in range(35): # for loop in psuedo pattern, in order to make unfilled circle
    circle.color(random.choice(pPalette)) # random choice of colors from pPalette
    circle.pensize(1+i)
    for i in range(35):
        circle.circle(15+5)
    circle.penup()
    circle.goto(random.randint(-300,300),random.randint(-300,300))
   # random randint for location in order to allow circles to be all over the panel
    circle.pendown()

circle.done()
fillCircle.done()


