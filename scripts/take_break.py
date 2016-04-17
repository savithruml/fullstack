#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# AUTHOR: Savithru M Lokanath
# PROJECT: HW_1 (Take a break from work)

import webbrowser, time

def takeBreak():
	
	total_breaks = 3
	break_count = 0
	
	print "This program started on " + time.ctime()
	
	while (break_count < total_breaks):
		
		time.sleep(10)
		webbrowser.open("https://www.youtube.com/watch?v=d0RCVX1Wgw4")
		break_count = break_count + 1

if __name__ == '__main__':
	takeBreak()

