"""The Instruction on the paint can say that 1 can of paint can cover 5 square meters of wall.
Given a random height and width of wall, calculate how many cans of paint you`ll need to buy.

number of cans = (wall height X wall widht) / coverage per can.

But because you can`t buy 0.6 of a can of paint, the result should be rounded upto 2 cans."""

import math

def paint_calc(height, width, cover):

    num_can = (height * width)/ cover
    round_can = math.ceil(num_can)
    print(f"you`ll need {round_can} cans of paint.")


test_h = int(input("height of wall(m): "))
test_w = int(input("width of the wall(m): "))
coverage= 5
paint_calc(height=test_h, width=test_w,cover=coverage)


