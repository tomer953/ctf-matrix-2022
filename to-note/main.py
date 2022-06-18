from tkinter import *
import random


def main():
    # create canvas
    w = Canvas(Tk(), width=2500, height=800)
    w.pack()

    # read data
    with open('flag.txt') as f:
        data = [float(x) for x in f.readline().split(' ')]

    # read all coords from file, 3 at a time
    for m, x, y in zip(*[iter(data)]*3):
        # draw rectangle in x,y coordinate
        w.create_rectangle(x-10, y-10, x+10, y+10, fill=random.choice(["orange", "lightgreen"]))

    mainloop()


main()
