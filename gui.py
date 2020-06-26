import os
from tkinter import *
import math
import queue
import time
from tkinter import messagebox

root = Tk()

root.title("BFS PATHFINDING")
root.geometry()


def printtombol(x):
    global maze
    global redX, redY, butR
    global startX, startY, butS

    if(select_mode == 0):
        if(redX != -1 and redY != -1):
            print('non')
            maze[redX][redY] = " "
            btns[butR].configure(bg='blue')

        sisi = len(maze)
        a = x+1
        w = a/sisi
        i = math.ceil(w)
        i = i-1
        b = sisi
        while b < a:
            b = b+sisi
        b = b-sisi
        j = a-b
        j = j-1
        redX = i
        redY = j
        butR = x
        maze[i][j] = "X"
        # print(maze)
        btns[x].configure(bg='red')

        disableMaze()
    elif(select_mode == 1):
        if(startX != -1 and startY != -1):
            print('non')
            maze[startX][startY] = " "
            btns[butS].configure(bg='blue')

        sisi = len(maze)
        a = x+1
        w = a/sisi
        i = math.ceil(w)
        i = i-1
        b = sisi
        while b < a:
            b = b+sisi
        b = b-sisi
        j = a-b
        j = j-1
        startX = i
        startY = j
        butS = x
        maze[i][j] = "O"
        # print(maze)
        btns[x].configure(bg='white')

        disableMaze()


def createMaze():
    maze = []
    maze.append(["#", " ", "#", "#", " ", "#", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", "#", "#", "#", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", " ", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", "#", "#", " ", "#", " ", "#"])

    return maze


def selectEnd():
    global select_mode

    select_mode = 0
    print('selectEnd')
    for x in range(len(btns)):
        if btns[x].cget('bg') == 'blue':
            btns[x]['state'] = NORMAL


def selectStart():
    global select_mode

    select_mode = 1
    print('selectStart')
    for x in range(len(btns)):
        if btns[x].cget('bg') == 'blue':
            btns[x]['state'] = NORMAL


def checkMaze():
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            print(maze[i][j], end=" ")
        print("")


def disableMaze():
    for x in range(len(btns)):
        btns[x]['state'] = DISABLED


def findPath():
    if(startX == -1 and startY == -1):
        response = messagebox.showinfo(
            "Titik Awal Tidak Ditemukan!", "Maaf titik awal tidak ditemukan, silahkan pilih satu kotak biru sebagai titik awal")
        return None

    if(redX == -1 and redY == -1):
        response = messagebox.showinfo(
            "Titik Akhir Tidak Ditemukan!", "Maaf titik akhir tidak ditemukan, silahkan pilih satu kotak biru sebagai titik akhir")
        return None

    panjang = len(maze)
    lebar = len(maze[0])
    print(panjang*lebar)
    nums = queue.Queue()
    nums.put("")
    add = ""
    # response = messagebox.showinfo(
    #     "Rute tidak ditemukan!", "Maaf rute dari start menuju ke tujuan tidak dapat ditemukan")

    while not findEnd(maze, add):
        add = nums.get()
        for j in ["L", "R", "U", "D"]:
            put = add + j
            if valid(maze, put):
                nums.put(put)


def findEnd(maze, moves):

    i = startY
    j = startX
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if maze[j][i] == "X":
        print("Found: " + moves)
        openWindow(maze, moves)

        return True

    return False


def openWindow(maze, path=""):
    top = Toplevel()
    top.title('Short Path')

    btns = []
    btn_nr = -1

    i = startY
    j = startX
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))

    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            btn_nr += 1
            if(col == "#"):
                btns.append(Button(top, bg='black', height=2, width=3, state=DISABLED,
                                   command=lambda x=btn_nr: printtombol(x)))
                btns[btn_nr].grid(row=j, column=i)
            elif(col == "O"):
                btns.append(Button(top, bg='white', height=2, width=3, state=DISABLED,
                                   command=lambda x=btn_nr: printtombol(x)))
                btns[btn_nr].grid(row=j, column=i)
            elif(col == "X"):
                btns.append(Button(top, bg='red', height=2, width=3, state=DISABLED,
                                   command=lambda x=btn_nr: printtombol(x)))
                btns[btn_nr].grid(row=j, column=i)
            else:
                # btns.append(Button(top, bg='blue', height=2, width=3,state=DISABLED,
                #             command=lambda x=btn_nr: printtombol(x)))
                # btns[btn_nr].grid(row=j, column=i)
                if (j, i) in pos:
                    # print("+ ", end="")
                    btns.append(Button(top, bg='yellow', height=2, width=3, state=DISABLED,
                                       command=lambda x=btn_nr: printtombol(x)))
                    btns[btn_nr].grid(row=j, column=i)
                else:
                    btns.append(Button(top, bg='blue', height=2, width=3, state=DISABLED,
                                       command=lambda x=btn_nr: printtombol(x)))
                    btns[btn_nr].grid(row=j, column=i)


def valid(maze, moves):
    # for x, pos in enumerate(maze[0]):
    #     if pos == "O":
    #         start = x

    i = startY
    j = startX
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "#"):
            return False

    return True


frame = LabelFrame(root, padx=20, pady=20)
frame.grid(row=0, column=0)

framemaze = LabelFrame(frame, text="Labirin", padx=40, pady=40)
framemaze.grid(row=0, column=0)

redX = -1
redY = -1
butR = -1

startX = -1
startY = -1
butS = -1

select_mode = -1

btn_nr = -1
btns = []
maze = createMaze()


for j, row in enumerate(maze):
    for i, col in enumerate(row):
        btn_nr += 1
        if(col == "#"):
            btns.append(Button(framemaze, bg='black', height=2, width=3, state=DISABLED,
                               command=lambda x=btn_nr: printtombol(x)))
            btns[btn_nr].grid(row=j, column=i)
        elif(col == "O"):
            btns.append(Button(framemaze, bg='white', height=2, width=3, state=DISABLED,
                               command=lambda x=btn_nr: printtombol(x)))
            btns[btn_nr].grid(row=j, column=i)

        elif(col == "X"):
            btns.append(Button(framemaze, bg='green', height=2, width=3, state=DISABLED,
                               command=lambda x=btn_nr: printtombol(x)))
            btns[btn_nr].grid(row=j, column=i)
        else:
            btns.append(Button(framemaze, bg='blue', height=2, width=3, state=DISABLED,
                               command=lambda x=btn_nr: printtombol(x)))
            btns[btn_nr].grid(row=j, column=i)

frame1 = LabelFrame(root, padx=20, pady=20)
frame1.grid(row=0, column=1)

deskripsi = LabelFrame(frame1, text="Deskripsi", padx=40, pady=40)
deskripsi.grid(row=0, column=0)

bt1 = Button(deskripsi, bg='blue', height=2, width=4,
             state=DISABLED).grid(row=0, column=0)
text1 = Label(deskripsi, text="= Jalan")
text1.grid(row=0, column=1)

bt2 = Button(deskripsi, bg='black', height=2, width=4,
             state=DISABLED).grid(row=1, column=0)
text2 = Label(deskripsi, text="= Tembok")
text2.grid(row=1, column=1)

bt3 = Button(deskripsi, bg='white', height=2, width=4,
             state=DISABLED).grid(row=2, column=0)
text3 = Label(deskripsi, text="= Titik Start")
text3.grid(row=2, column=1)

bt4 = Button(deskripsi, bg='red', height=2, width=4,
             state=DISABLED).grid(row=3, column=0)
text4 = Label(deskripsi, text="= Titik Akhir")
text4.grid(row=3, column=1)

bt5 = Button(deskripsi, bg='yellow', height=2, width=4,
             state=DISABLED).grid(row=4, column=0)
text5 = Label(deskripsi, text="= Jalur BFS")
text5.grid(row=4, column=1)

perintah = LabelFrame(frame1, text="Perintah", padx=40, pady=40)
perintah.grid(row=1, column=0)

start_button = Button(perintah, text="Pick Start",
                      command=selectStart).grid(row=0, column=0)
end_button = Button(perintah, text="Pick End",
                    command=selectEnd).grid(row=1, column=0)


gap = Label(perintah, text=" ")
gap.grid(row=2, column=0)
# status_button = Button(perintah,text="Reset",command=openWindow).grid(row=0,column=2)
status_button = Button(perintah, text="Find Path",
                       command=findPath).grid(row=3, column=0)


root.mainloop()
