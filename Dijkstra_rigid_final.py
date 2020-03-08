import numpy as np
import matplotlib.pyplot as plt
import time
import math
import cv2

blank_list = []
for entries in range(140000):
    entries = math.inf
    blank_list.append(entries)
initial_matrix = np.array(blank_list, dtype=object).reshape(400, 350)

ind1 = 5  # 5
ind2 = 5  # 5
ind = (ind1, 200 - ind2)

goal1 = 295  # 295
goal2 = 195  # 195
goal = (goal1, 200 - goal2)

initial_matrix[ind[0]][ind[1]] = 1

rows = initial_matrix.shape[0]
cols = initial_matrix.shape[1]

img_map = np.zeros([cols, rows, 3], dtype=np.uint8)
flag = False

r = 2
c = 2
cr1 = 102.54 - (r + c) * math.sqrt(1.3481)  # rectangle
cr2 = 341 + (r + c) * math.sqrt(4.24)
cr3 = 114.46 + (r + c) * math.sqrt(1.3481)
cr4 = 186 - (r + c) * math.sqrt(4.24)

ck1 = 25 - (r + c) * math.sqrt(1.36)  # kite
ck2 = 295 - (r + c) * math.sqrt(1.36)
ck3 = 55 + (r + c) * math.sqrt(1.36)
ck4 = 325 + (r + c) * math.sqrt(1.36)

p11 = 15 - (r + c)  # big P1
p12 = 120 + (r + c) * math.sqrt(2.96)
p13 = 100 + (r + c) * math.sqrt(2)
p14 = 340 - (r + c) * math.sqrt(170)

p21 = (r + c) * math.sqrt(2.96)  # big P2
p22 = (r + c) * math.sqrt(2.44)
p23 = (r + c) * math.sqrt(2.96)
p24 = (r + c) * math.sqrt(2.44)


# Obstacles
def obstacle_here():
    img_map[ind[1], ind[0]] = (255, 255, 255)
    img_map[goal[1], goal[0]] = (255, 255, 255)

    for h in range(0, rows):  # Circle
        for k in range(0, cols):
            if ((h - 225) ** 2) / (25 + r + c) ** 2 + ((k - 50) ** 2) / (25 + r + c) ** 2 <= 1:
                initial_matrix[h][k] = flag
                img_map[k, h] = (120, 0, 200)

    for h in range(0, rows):  # kite
        for k in range(0, cols):
            if (k >= 0.6 * h + ck1) and (k >= -0.6 * h + ck2) and (k <= 0.6 * h + ck3) and (k <= -0.6 * h + ck4):
                initial_matrix[h][k] = flag
                img_map[k, h] = (120, 0, 200)

    for h in range(0, 115):  # big P1
        for k in range(0, 100):
            if (k >= p11) and (k <= -(7 / 5) * h + p12) and (k <= -h + p13) and (k >= -13 * h + p14):
                initial_matrix[h][k] = flag
                img_map[k, h] = (120, 0, 200)

            if (k <= (7 / 5) * h - 90 - p21):
                initial_matrix[h][k] = entries
                img_map[k, h] = (0, 0, 0)

    for h in range(0, 115):  # big P2
        for k in range(0, 100):
            if (k >= (7 / 5) * h - 90 - p21) and (k <= -(6 / 5) * h + 170 + p22) and (k <= (7 / 5) * h - 25 + p23) and (
                    k >= -(6 / 5) * h + 105 - p24):
                initial_matrix[h][k] = flag
                img_map[k, h] = (120, 0, 200)

            if (k <= p11):
                initial_matrix[h][k] = entries
                img_map[k, h] = (0, 0, 0)

    for h in range(100, 210):  # ellipse
        for k in range(70, 130):
            if ((h - 150) ** 2) / (40 + r + c) ** 2 + ((k - 100) ** 2) / (20 + r + c) ** 2 <= 1:
                initial_matrix[h][k] = flag
                img_map[k, h] = (120, 0, 200)

    for h in range(0, rows):  # rectangle
        for k in range(0, cols):
            if (k >= 0.59 * h + cr1) and (k <= -1.8 * h + cr2) and (k <= 0.59 * h + cr3) and (k >= -1.8 * h + cr4):
                initial_matrix[h][k] = flag
                img_map[k, h] = (120, 0, 200)

    for h in range(0, rows):  # lower border
        for k in range(0, cols):
            if (k >= 200 - (r + c)):
                initial_matrix[h][k] = flag
                img_map[k, h] = (255, 0, 0)

    for h in range(0, rows):  # upper border
        for k in range(0, 200):
            if (k <= (r + c)):
                initial_matrix[h][k] = flag
                img_map[k, h] = (255, 0, 0)

    for h in range(0, rows):  # left border
        for k in range(0, cols):
            if (h <= (r + c)):
                initial_matrix[h][k] = flag
                img_map[k, h] = (255, 0, 0)

    for h in range(0, rows):  # right border
        for k in range(0, cols):
            if (h >= 300 - (r + c)):
                initial_matrix[h][k] = flag
                img_map[k, h] = (255, 0, 0)
    ##############################################################overlapping###########

    for h in range(0, rows):  # Circle
        for k in range(0, cols):
            if ((h - 225) ** 2) / 625 + ((k - 50) ** 2) / 625 <= 1:
                initial_matrix[h][k] = flag
                img_map[k, h] = (255, 255, 255)

    for h in range(0, rows):  # kite
        for k in range(0, cols):
            if (k >= 0.6 * h + 25) and (k >= -0.6 * h + 295) and (k <= 0.6 * h + 55) and (k <= -0.6 * h + 325):
                initial_matrix[h][k] = flag
                img_map[k, h] = (255, 255, 255)

    for h in range(0, rows):  # big C
        for k in range(0, cols):
            if (k >= 15) and (k <= -(7 / 5) * h + 120) and (k <= -h + 100) and (k >= -13 * h + 340):
                initial_matrix[h][k] = flag
                img_map[k, h] = (255, 255, 255)

    for h in range(0, rows):
        for k in range(0, cols):
            if (k >= (7 / 5) * h - 90) and (k <= -(6 / 5) * h + 170) and (k <= (7 / 5) * h - 25) and (
                    k >= -(6 / 5) * h + 105):
                initial_matrix[h][k] = flag
                img_map[k, h] = (255, 255, 255)

    for h in range(100, 195):  # ellipse
        for k in range(70, 130):
            if ((h - 150) ** 2) / 1600 + ((k - 100) ** 2) / 400 <= 1:
                initial_matrix[h][k] = flag
                img_map[k, h] = (255, 255, 255)

    for h in range(25, 170):  # rectangle
        for k in range(120, 175):
            if (k >= 0.59 * h + 102.54) and (k <= -1.8 * h + 341) and (k <= 0.59 * h + 114.46) and (
                    k >= -1.8 * h + 186):
                initial_matrix[h][k] = flag
                img_map[k, h] = (255, 255, 255)


obstacle_here()

if initial_matrix[ind[0]][ind[1]] == flag:
    print("initial node in the obstacle")
else:
    pass

if initial_matrix[goal[0]][goal[1]] == flag:
    print("goal node in the obstacle")
else:
    pass


# cv2.imshow('aaaa', img_map)
# plt.imshow(img_map, cmap="gray")
# plt.show()
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# move subfunctions

# root_two = math.sqrt(2)


def move_right(i, j, map_):
    try:
        if not map_[i, j + 1]:
            return None
    except:
        pass
    if j >= 300:
        return None
    else:
        cost = initial_matrix[i][j] + 1
        j = j + 1
    return (i, j), cost


def move_left(i, j, map_):
    try:
        if not map_[i, j - 1]:
            return None
    except:
        pass
    if j <= 0:
        return None
    else:
        cost = initial_matrix[i][j] + 1
        j = j - 1
    return (i, j), cost


def move_up(i, j, map_):
    try:
        if not map_[i - 1, j]:
            return None
    except:
        pass
    if i <= 0:
        return None
    else:
        cost = initial_matrix[i][j] + 1
        i = i - 1
    return (i, j), cost


def move_down(i, j, map_):
    try:
        if not map_[i + 1, j]:
            return None
    except:
        pass
    if i >= 300:
        return None
    else:
        cost = initial_matrix[i][j] + 1
        i = i + 1
    return (i, j), cost


def move_upright(i, j, map_):
    try:
        if not map_[i - 1, j + 1]:
            return None
    except:
        pass
    if j >= 200 or i <= 0:
        return None
    else:
        cost = 1.42 + initial_matrix[i][j]
        j = j + 1
        i = i - 1
    return (i, j), cost


def move_downright(i, j, map_):
    try:
        if not map_[i + 1, j + 1]:
            return None
    except:
        pass
    if j >= 200 or i >= 300:
        return None
    else:
        cost = 1.42 + initial_matrix[i][j]
        j = j + 1
        i = i + 1
    return (i, j), cost


def move_upleft(i, j, map_):
    try:
        if map_[i - 1, j - 1]:
            return None
    except:
        pass
    if j <= 0 or i <= 0:
        return None
    else:
        cost = 1.42 + initial_matrix[i][j]
        j = j - 1
        i = i - 1
    return (i, j), cost


def move_downleft(i, j, map_):
    try:
        if not map_[i + 1, j - 1]:
            return None
    except:
        pass
    if j <= 0 or i >= 300:
        return None
    else:
        cost = 1.42 + initial_matrix[i][j]
        j = j - 1
        i = i + 1
    return (i, j), cost


def get_neighbours(i, j):
    neighbours_cost = []
    index = []
    action_up = move_up(i, j, initial_matrix)
    if action_up is not None:
        neighbours_cost.append(action_up[1])
        index.append(action_up[0])
    action_down = move_down(i, j, initial_matrix)
    if action_down is not None:
        neighbours_cost.append(action_down[1])
        index.append(action_down[0])
    action_left = move_left(i, j, initial_matrix)
    if action_left is not None:
        neighbours_cost.append(action_left[1])
        index.append(action_left[0])
    action_right = move_right(i, j, initial_matrix)
    if action_right is not None:
        neighbours_cost.append(action_right[1])
        index.append(action_right[0])
    action_upright = move_upright(i, j, initial_matrix)
    if action_upright is not None:
        neighbours_cost.append(action_upright[1])
        index.append(action_upright[0])
    action_downright = move_downright(i, j, initial_matrix)
    if action_downright is not None:
        neighbours_cost.append(action_downright[1])
        index.append(action_downright[0])
    action_upleft = move_upleft(i, j, initial_matrix)
    if action_upleft is not None:
        neighbours_cost.append(action_upleft[1])
        index.append(action_upleft[0])
    action_downleft = move_downleft(i, j, initial_matrix)
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


def sort_list1(list_a, list_b):
    list_b = [i[1] for i in sorted(zip(list_a, list_b))]


def sort_list2(list_a):
    list_a.sort()


# goal = (295,195)
# ind = (5,5)
node_cost = 0
# initial_matrix[ind[0]][ind[1]] = 0

explore_queue = []
index_queue = []
index_queue.append(ind)
explore_queue.append(node_cost)
visited = set()
visited_list = []
breakwhile = False

start_time = time.clock()


def anim(visited, img_map, parent_map, node):
    path_list = []
    parent = parent_map[node]
    path_list.append(node)
    while parent is not None:
        path_list.append(parent)
        parent = parent_map[parent]

    # cv2.imshow('hh',img_map)
    for ani in visited:
        y = ani[1]
        x = ani[0]

        img_map[y, x] = (0, 255, 255)
        # ind[0, 1] = (0, 255, 0)
        #   img_map[ind[1],ind[0]] = (0,255,0)
        # print(img_map[y,x],x,y)
        # plt.imshow(img_map, cmap="gray")
        cv2.imshow('map', img_map)
        # cv2.imshow('node',ind)
        if cv2.waitKey(1) == 27:
            break

    for ind in path_list:
        img_map[ind[1], ind[0]] = (0, 0, 255)

    cv2.imshow('map', img_map)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


parent_map = {}
parent_map[ind] = None
while len(index_queue) != 0 and not breakwhile:
    node = index_queue[0]
    visited.add(node)
    visited_list.append(node)

    # print(index_queue[0], explore_queue[0])
    index_queue.pop(0)
    explore_queue.pop(0)
    pair = get_neighbours(node[0], node[1])
    # print('pair',pair)
    neighbours_cost = pair[0]
    index = pair[1]
    # print(index)
    # print(neighbours_cost)

    #######
    if node == goal:
        print('goal reached')
        anim(visited_list, img_map, parent_map, node)
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
                parent_map[index[i]] = node

        # for i in range(len(index)):
        #    if index[i] == goal:
        #        print("goal reached")
        #        breakwhile = True
        #        break
        #    else:
        #        continue

    sort_list1(explore_queue, index_queue)
    sort_list2(explore_queue)

end_time = time.clock()
print("time", end_time - start_time)
