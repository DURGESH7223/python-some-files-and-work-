# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:51:40 2019

@author: Durgesh
"""

import turtle
def rectangle(color):
    t.begin_fill()
    t.fillcolor(color)
    for i in range(2):
        t.forward(400)
        t.right(90)
        t.forward(100)
        t.right(90)
        t.end_fill()
    
    
t =turtle.Turtle()
t.up()
t.goto(0,-300)
t.down()
t.goto(0,400)
rectangle('orange')