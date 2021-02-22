import quantumblur as qb
import PIL as pil
import numpy as np

def text2probs(text):
    txt = open(text,"r")
    lines = txt.readlines()
    arr = []
    for line in lines:
        tmp = []
        for c in line:
            if c == "#":
                tmp.append(1)
            else:
                tmp.append(0)
        arr.append(tmp)
    probs = dict(((j,i), arr[i][j]) for i in range(0,len(arr)) for j in range(0,len(arr[0])) if i<j)
    return probs


def height2text(height):
    arr = []
    for e in height.items:
        print(e)
