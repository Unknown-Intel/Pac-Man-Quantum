import string
import numpy as np
import random

# Convert text file into integer array for manipulation
def text2array(text):
    txt = open(text,"r")
    lines = txt.readlines()
    arr = []
    for line in lines:
        # print(line)
        tmp = []
        for c in line:
            tmp.append(c)
        arr.append(tmp)
    return arr

# Convert integer array into text file for game access
def array2text(arr):
    out = ""
    for i in range(0,len(arr)):
        for j in range(0, len(arr[i])):
            out += str(arr[i][j])
    return out

def array2text_nl(arr):
    out = ""
    for i in range(0,len(arr)):
        for j in range(0, len(arr[i])):
            out += str(arr[i][j])
        out += "\n"
    return out

# Add Player, Ghost spawn points, Ghost cage through DFS
def post_processing(text):
    arr = text2array(text)
    visited = dfs(arr, (0, 0))
    add_ghost(arr, visited)
    add_player(arr, visited)
    add_cages(arr, visited)
    out = array2text(arr)
    newLoc = "C:/Users/T_Ana/source/git_repos/Pac_man_quantum/resource/level15.txt"
    text_file = open(newLoc , "w")
    text_file.write(out)
    text_file.close()

# DFS to traverse map to look for accessible locations
def dfs(arr, node):
    visited = []
    _dfs(arr, node, visited)
    return visited


def _dfs(arr, node, visited):
    rowNbr = [ -1, 0, 0, 1] 
    colNbr = [  0, -1, 1, 0] 

    if node not in visited and node[0] >= 0 and node[0] < len(arr) and node[1] >= 0  and node[1] < len(arr[node[0]]):
        if (arr[node[0]][node[1]] != "#" and  arr[node[0]][node[1]] != "\n"):
            arr[node[0]][node[1]] = "."
            visited.append(node)

            for k in range(4):
                if node[0] + rowNbr[k] >= 0 and node[0] + rowNbr[k] < len(arr) and node[1] + colNbr[k] >= 0 and node[1] + colNbr[k] <  len(arr[node[0]]):
                    _dfs(arr, (node[0] + rowNbr[k], node[1] + colNbr[k]), visited)

# Add Ghost Spawn Points
def add_ghost(arr, visited):
    spawn_point_x = 100
    spawn_point_y = 100

    for i in range(random.randint(1,4)):
        while (spawn_point_x, spawn_point_y) not in visited:
            spawn_point_x = random.randint(0, len(arr))
            spawn_point_y = random.randint(0, len(arr[0]))
        visited.remove((spawn_point_x, spawn_point_y))
        arr[spawn_point_x][spawn_point_y] = "&"

# Add Player Spawn Points
def add_player(arr, visited):
    spawn_point_x = 100
    spawn_point_y = 100

    while (spawn_point_x, spawn_point_y) not in visited:
        spawn_point_x = random.randint(0, len(arr))
        spawn_point_y = random.randint(0, len(arr[0]))
    visited.remove((spawn_point_x, spawn_point_y))
    arr[spawn_point_x][spawn_point_y] = "@"

# Add Ghost Cage
def add_cages(arr, visited):
    listofwall= []
    listoflocations = []
    rowNbr = [ -1, 0, 0, 1, -1, -1, 1, 1] 
    colNbr = [  0, -1, 1, 0, -1, 1, -1, 1] 
    spawn_point_x = 100
    spawn_point_y = 100
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if arr[i][j] == "#":
                listofwall.append((i,j))
    for node in listofwall:
        x = node[0]
        y = node[1]
        location = (0, 0)
        if (x - 1, y + 1) in listofwall and (x - 1, y - 1) in listofwall:
            if arr[x - 3][y] == "." and arr[x - 2][y] != "#":
                location = (x - 1, y)
                if location not in listoflocations:
                    listoflocations.append(location)
        if (x + 1, y + 1) in listofwall and (x, y + 2) in listofwall:
            if arr[x - 2][y + 1] == "." and arr[x - 1][y + 1] != "#":
                location = (x, y + 1)
                if location not in listoflocations:
                    listoflocations.append(location)
        if (x + 1, y - 1) in listofwall and (x, y - 2) in listofwall:
            if arr[x - 2][y - 1] == "." and arr[x - 1][y - 1] != "#":
                location = (x, y - 1)
                if location not in listoflocations:
                    listoflocations.append(location)
    for node in listoflocations:
        for k in range(8):
            if node[0] + rowNbr[k] >= 0 and node[0] + rowNbr[k] < len(arr) and node[1] + colNbr[k] >= 0 and node[1] + colNbr[k] <  len(arr[node[0]]):
                temp = (node[0] + rowNbr[k], node[1] + colNbr[k])
                if temp in listoflocations:
                    listoflocations.remove(temp)
    while (spawn_point_x, spawn_point_y) not in listoflocations:
            spawn_point_x = random.randint(0, len(arr))
            spawn_point_y = random.randint(0, len(arr[0]))
    arr[spawn_point_x][spawn_point_y] = "%"
    arr[spawn_point_x - 1][spawn_point_y] = "$"



















# Sams attempt at DFS pls take note keep FOREVER
# def dfs1(arr, node, visited):
#     global visited
#     if visited[node[0]][node[1]] == 1:
#         return
#     elif visited[node[0]][node[1]] == 0:
#         if arr[node[0]][node[1]] == "#":
#             visited[node[0]][node[1]] = 2
#             return
#         else:
#             visited[node[0]][node[1]] = 1
#         for i in range(-1, 1):
#             if node[0] + i >= len(arr)-1:
#                 x = 0
#             elif node[0] + i < 0:
#                 x = len(arr)
#             else:
#                 x = node[0] + i
#             for j in range(-1, 1):
#                 if node[1] + j >= len(arr[node[0]])-1:
#                     y = 0
#                 elif node[1] + j < 0:
#                     y = len(arr[node[0]])
#                 else:
#                     y = node[1] + j
#                 node = (x,y)
#                 bfs(arr,node)
    
# def print_visited():
#     return visited
