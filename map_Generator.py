import quantumblur as qb
import PIL as pil
import numpy as np

#Convert text file to integer for Quantum Manipulation
def text2array(text):
    txt = open(text,"r")
    lines = txt.readlines()
    arr = []
    for line in lines:
        # print(line)
        tmp = []
        for c in line:
            if c == "#":
                tmp.append("1")
            else:
                tmp.append("0")
        arr.append(tmp)
    return arr

# Convert text file to probability array for Quantum manipulation
def text2probs(text):
    arr = text2array(text)
    # print(len(arr), len(arr[0]))
    probs = {}
    for i in range(len(arr)):
        for j in range(len(arr[0])-1):
            probs[(i,j)] = arr[i][j]
    # probs = dict(((j,i), arr[i][j]) for i in range(0,len(arr)) for j in range(0,len(arr[0])) if i<j)
    return probs

def partial_x(qc,fraction):
    for j in range(qc.num_qubits):
         qc.rx(np.pi*fraction, j)

def partial_y(qc, fraction):
    for j in range(qc.num_qubits):
        qc.ry(np.pi*fraction, j)

def partial_z(qc, fraction):
    for j in range(qc.num_qubits):
        qc.rz(np.pi*fraction, j)

def control_x(qc, fraction):
    for j in range(qc.num_qubits):
        if j >= 0 and j < qc.num_qubits:
            qc.cx(j-1, j)
            qc.rx(np.pi*fraction, j)
            qc.cx(j-1, j)

def control_z(qc, fraction):
    for j in range(qc.num_qubits):
        if j >= 0 and j < qc.num_qubits:
            qc.cx(j-1, j)
            qc.rz(np.pi*fraction, j)
            qc.cx(j-1, j)

def control_y(qc, fraction):
    for j in range(qc.num_qubits):
        if j >= 0 and j < qc.num_qubits:
            qc.cx(j-1, j)
            qc.ry(np.pi*fraction, j)
            qc.cx(j-1, j)

# Generate maps using current maps and quantum circuit, saves to generated maps
def generate_maps(number):
    for k in range(20):
        loc = "C:/Users/T_Ana/source/git_repos/Pac_man_quantum/resource/generated_maps/"
        if k == 0:
            map = text2probs("C:/Users/T_Ana/source/git_repos/Pac_man_quantum/resource/level"+ str(number) + ".txt")
        else:
            loc = loc + str(k-1) + "new.txt"
            map = text2probs(loc)

        qc = qb.height2circuit(map)
        rand = 2*np.pi/20

        #Change circuit for different map generation
        partial_x(qc,rand*k)

        probs = qb.circuit2height(qc)
        arr = np.zeros(shape=(32,29))
        for i in probs:
            x = i[0]
            y = i[1]
            arr[x][y] = probs[(x, y)]
        arr = np.round(arr, decimals=1)
        out = ""
        for i in range(0,len(arr)):
            for j in range(0, len(arr[i])):
                if arr[i][j] == 0:
                    out += "_"
                else:
                    out += "#"
            out += "\n"
        newLoc = "C:/Users/T_Ana/source/git_repos/Pac_man_quantum/resource/generated_maps/" + str(k) + "-cxrzcx.txt"
        text_file = open(newLoc , "w")
        text_file.write(out)
        text_file.close()

# def height2text(height):
#     arr = []
#     for e in height.items:
#         print(e)

