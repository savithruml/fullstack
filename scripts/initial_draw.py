#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# AUTHOR: Savithru M Lokanath
# PROJECT: HW_3 (Draw Initial)

import turtle

def draw_initial_M():
	
	initial.pu()
	initial.setpos(-50,0)
	initial.pd()
	initial.seth(90)
	initial.forward(100)
	initial.right(140)
	initial.forward(60)
	initial.left(100)
	initial.forward(60)
	initial.seth(270)
	initial.forward(100)
	
def draw_initial_L():
	
	initial.pu()
	initial.setpos(50,100)
	initial.pd()
	initial.seth(-90)
	initial.forward(100)
	initial.left(90)
	initial.forward(80)
	

if __name__ == '__main__':
	
	window = turtle.Screen()
	window.bgcolor("red")
	
	initial = turtle.Turtle()
	initial.shape("arrow")
	initial.color("yellow")
	initial.speed(10)

	draw_initial_M()
	draw_initial_L()
	
	window.exitonclick()
