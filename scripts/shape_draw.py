#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# AUTHOR: Savithru M Lokanath
# PROJECT: HW_2

import turtle

def draw_art():
	
	art = turtle.Turtle()
	art.shape("turtle")
	art.color("yellow")
	art.speed(10)
	
	for i in range(0,36):
		
		draw_square(art)
		art.right(10)
		
def draw_square(art):
	
	for i in range(0,4):
		
		art.forward(100)
		art.right(90)
		
def draw_circle():
	
	circle = turtle.Turtle()
	circle.shape("arrow")
	circle.color("blue")
	circle.circle(100)
	
def draw_triangle():
	
	triangle = turtle.Turtle()
	triangle.shape("triangle")
	triangle.color("black")
	
	for i in range(0,3):
		
		triangle.forward(100)
		triangle.right(120)

if __name__ == '__main__':
	
	window = turtle.Screen()
	window.bgcolor("red")
	
	#draw_square()
	#draw_circle()
	#draw_triangle()
	draw_art()
	
	window.exitonclick()
	
	

