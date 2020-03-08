# ENPM_661_Project-2
Djikstra Algorithm for point and rigid robot

                                        ENPM661    Project 2 : - Djikstra Implementation . 


Group :- Divyam Garg and Preyash Parikh

Nodes are explored by Djikstra's algorithm and backtracking was applied with same giving the most optimal path and avoiding the obstacles.

The code is to be run in Python 3

1) Imported libraries :
     	-import numpy as np
     	-import matplotlib.pyplot as plt
     	-import time
     	-import math
     	-import cv2


2) User inputs :-  
     	- Start node and goal node coordinates are asked to enter by user.

3) Point robot:- 
     	-If start node or goal node is in the obstacle the statement ("start/goal in the obstacle is mentioned"). 
     	-The start node and goal nodes are identified by white color pixel. 

4) Rigid robot:- 
     	-Clearance of 'c' is given with the added clearance of radius of robot (r) making it total of r+c
     	-Predefined values of r and c is 2. 
     	-You can vary value of r and c by varying values at line number at 30 and 31 respectively. 
     	-If values of r and c is increased, also change the starting node location from (5,5). If not,  it would be in border and program won't run.

5) Time:-
	- Total time of run (including backtracking) for "dijkstra_point.py" is 142.708 seconds for starting point (5,5) and goal node    	    at (295,195)
	- Total time of run (including backtracking) for "dijkstra_rigid.py" is 128.34480 seconds with robot radius as 2 px and 		  clearance as 2 px  for starting point (5,5) and goal node at (295,195).

 
