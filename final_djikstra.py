# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 21:14:33 2020

@author: divyam
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 02:36:01 2020

@author: divyam
"""
import numpy as np
import matplotlib.pyplot as plt
import time
import math

blank_list = []
for entries in range(60000):
    entries = math.inf
    blank_list.append(entries)
initial_matrix = np.array(blank_list, dtype = object).reshape(300, 200) 

initial_matrix[0][0] = 0

    

rows = initial_matrix.shape[0]
cols = initial_matrix.shape[1]
flag = False
   

# Obstacles

for h in range(0, rows):
    for k in range(0, cols):
        if (k-225)**2 + (h-50)**2 <= 625: 
            initial_matrix[h][k] = flag

for h in range(0, rows):
    for k in range(0, cols):
        if h<= 13*k -140 and h<= 185 and h<= -(7/5)*k +290 and h<= (6/5)*k +30 and h<= -(6/5)*k +210 and h<= k + 100:
            initial_matrix[h][k] = flag
            
for h in range(0, rows):
    for k in range(0, cols):
        if ((k-150)**2)/1600 + ((h-100)**2)/400 <= 1: 
            initial_matrix[h][k] = flag

# move subfunctions 
def move_right(i,j, map_):
    if not map_[i,j+1]:
        return None
    if j == 300:     
        return None
    else:
        cost = initial_matrix[i][j] + 1   
        j = j + 1
    return (i,j) , cost
    

def move_left(i,j,map_):
    if not map_[i,j-1]:
        return None
    if j == 0:     
        return None
    else:
        cost = initial_matrix[i][j] + 1   
        j = j - 1
    return (i,j) , cost

def move_up(i,j,map_):
    if not map_[i-1,j]:
        return None
    if i == 0:     
        return None
    else:
        cost = initial_matrix[i][j] + 1   
        i = i - 1
    return (i,j) , cost

def move_down(i,j,map_):
    if not map_[i+1,j]:
        return None
    if i == 200:     
        return None
    else:
        cost = initial_matrix[i][j] + 1   
        i = i + 1
    return (i,j) , cost


def move_upright(i,j,map_):
    if not map_[i-1,j+1]:
        return None
    if j == 300 or i == 0:
        return None
    else:
        cost = 1.42 + initial_matrix[i][j]
        j = j + 1
        i = i - 1
    return (i,j) , cost
    

def move_downright(i,j,map_):
    if not map_[i+1,j+1]:
        return None
    if j == 300 or i == 200:
        return None
    else:
        cost = 1.42 + initial_matrix[i][j]
        j = j + 1
        i = i + 1
    return (i,j) , cost
    

def move_upleft(i,j,map_):
    if map_[i-1,j-1]:
        return None 
    if j == 0 or i == 0:
        return None
    else:
        cost = 1.42 + initial_matrix[i][j]
        j = j - 1 
        i = i - 1
    return (i,j) , cost
    

def move_downleft(i,j,map_):
    if not map_[i+1,j-1]:
        return None 
    if j == 0 or i == 200:
        return None
    else:
        cost = 1.42 + initial_matrix[i][j]
        j = j - 1
        i = i + 1
    return (i,j) , cost
    

def get_neighbours(i,j):
    neighbours_cost = []
    index = []
    action_up = move_up(i,j,initial_matrix)
    if action_up is not None:
        neighbours_cost.append(action_up[1])
        index.append(action_up[0])
    action_down = move_down(i,j,initial_matrix)
    if action_down is not None:
        neighbours_cost.append(action_down[1])
        index.append(action_down[0]) 
    action_left = move_left(i,j,initial_matrix)
    if action_left is not None:
        neighbours_cost.append(action_left[1])
        index.append(action_left[0])
    action_right = move_right(i,j,initial_matrix)
    if action_right is not None:
        neighbours_cost.append(action_right[1])
        index.append(action_right[0])    
    action_upright = move_upright(i,j,initial_matrix)
    if action_upright is not None:
        neighbours_cost.append(action_upright[1])
        index.append(action_upright[0])
    action_downright = move_downright(i,j,initial_matrix)
    if action_downright is not None:
        neighbours_cost.append(action_downright[1])
        index.append(action_downright[0]) 
    action_upleft = move_upleft(i,j,initial_matrix)
    if action_upleft is not None:
        neighbours_cost.append(action_upleft[1])
        index.append(action_upleft[0])
    action_downleft = move_downleft(i,j,initial_matrix)
    if action_downleft is not None:
        neighbours_cost.append(action_downleft[1])
        index.append(action_downleft[0])    
               
    return neighbours_cost, index

'''def get_current_value(i,j):
    current_value = initial_matrix[i][j]
    return current_value'''

'''def locate_value_index(mat):
    i,j = np.where(mat == node)
    i = int(i)
    j = int(j)
    return (i,j)'''

def sort_list1(list_a,list_b):
    list_b = [i[1] for i in sorted(zip(list_a, list_b))]
    
def sort_list2(list_a):
    list_a.sort()
    
goal = (200,180)                
ind = (0,0)
node_cost = 0


explore_queue = []  
index_queue = []
index_queue.append(ind)
explore_queue.append(node_cost)
visited = set()
breakwhile = False


start_time = time.clock()
while len(index_queue) != 0 and not breakwhile:
    
    node = index_queue[0]
    visited.add(node)
    #for i in range(len(index_queue)):
    index_queue.pop(0)
    explore_queue.pop(0)
    #print(visited)
    
    
    #val = get_current_value(ind[0],ind[1])
    pair = get_neighbours(node[0],node[1])
    neighbours_cost = pair[0]
    index = pair[1]
    #print(index)
    #print(neighbours_cost)
    
    #######
    if node == goal:
        print('goal reached')
        breakwhile = True
    
    #######
    
    
    for i in range(len(index)):
        if index[i] not in visited:
                        
            old_cost = initial_matrix[index[i][0]][index[i][1]]
            if neighbours_cost[i] < old_cost:
                initial_matrix[index[i][0]][index[i][1]] = neighbours_cost[i]
                if old_cost != math.inf:
                    ind_node = index_queue.index((index[i][0], index[i][1]))
                    index_queue.pop(ind_node)
                    explore_queue.pop(ind_node)
                    
                index_queue.append(index[i])
                explore_queue.append(initial_matrix[index[i][0]][index[i][1]])
            
                    
                
                
                
                
            
            
    
    
        #for i in range(len(index)):
        #    if index[i] == goal:            
        #        print("goal reached")
        #        breakwhile = True
        #        break
        #    else: 
        #        continue
            
    sort_list1(explore_queue,index_queue)
    sort_list2(explore_queue)
   

end_time = time.clock()
print(end_time - start_time)































            

