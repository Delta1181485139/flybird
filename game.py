import pygame,sys
import random
from element import Element
# from code import build_BIRD
# from code import build_CLOUD
# from code import build_SWITCH
# from code import LETTER
# from code import build_OBSTACLE
#图像对象


black = (0,0,0)
white = (255,255,255)

#数字
color = (0,0,0)
letter_0 = ( ((2,1), color),((3,1), color),((1,2),color),((4,2),color),((1,3),color),((4,3),color),((1,4),color),((4,4),color),((2,5),color),((3,5),color) )
letter_1 = ( ((2,1), color),((1,2), color),((2,2),color),((2,3),color),((2,4),color),((1,5),color),((2,5),color),((3,5),color) )
letter_2 = ( ((2,1), color),((3,1), color),((1,2),color),((4,2),color),((3,3),color),((2,4),color),((1,5),color),((2,5),color),((3,5),color),((4,5),color), )
letter_3 = ( ((2,1), color),((3,1), color),((1,2),color),((4,2),color),((3,3),color),((1,4),color),((4,4),color),((2,5),color),((3,5),color) )
letter_4 = ( ((3,1), color),((2,2), color),((1,3),color),((3,3),color),((1,4),color),((2,4),color),((3,4),color),((4,4),color),((3,5),color) )
letter_5 = ( ((1,1), color),((2,1), color),((3,1),color),((4,1),color),((1,2),color),((1,3),color),((2,3),color),((3,3),color),((4,4),color),((1,5),color),((2,5),color),((3,5),color) )
letter_6 = ( ((2,1), color),((3,1), color),((1,2),color),((1,3),color),((2,3),color),((3,3),color),((1,4),color),((4,4),color),((2,5),color),((3,5),color) )
letter_7 = ( ((1,1), color),((2,1), color),((3,1), color),((4,2),color),((4,3),color),((3,4),color),((3,5),color) )
letter_8 = ( ((2,1), color),((3,1), color),((1,2),color),((4,2),color),((2,3),color),((3,3),color),((1,4),color),((4,4),color),((2,5),color),((3,5),color) )
letter_9 = ( ((2,1), color),((3,1), color),((1,2),color),((4,2),color),((2,3),color),((3,3),color),((4,3),color),((4,4),color),((3,5),color) )
LETTER = (letter_0,letter_1,letter_2,letter_3,letter_4,letter_5,letter_6,letter_7,letter_8,letter_9)

#鸟用到的颜色
buff = (255,214,0)
yellow = (251,192,45)
deep_yellow = (255,152,0)
aqua = (178,223,219)
orange = (255,87,34)

build_BIRD=(
((7, 1), black),
((8, 1), black),
((9, 1), black),
((10, 1), black),
((11, 1), black),
((12, 1), black),

((5, 2), black),
((6, 2), black),
((7, 2), buff),
((8, 2), buff),
((9, 2), buff),
((10, 2), black),
((11, 2), white),
((12, 2), white),
((13, 2), black),

((4, 3), black),
((5, 3), buff),
((6, 3), buff),
((7, 3), yellow),
((8, 3), yellow),
((9, 3), black),
((10, 3), white),
((11, 3), white),
((12, 3), white),
((13, 3), white),
((14, 3), black),

((2, 4), black),
((3, 4), black),
((4, 4), black),
((5, 4), black),
((6, 4), yellow),
((7, 4), yellow),
((8, 4), yellow),
((9, 4), black),
((10, 4), aqua),
((11, 4), white),
((12, 4), white),
((13, 4), black),
((14, 4), white),
((15, 4), black),

((1, 5), black),
((2, 5), white),
((3, 5), white),
((4, 5), white),
((5, 5), white),
((6, 5), black),
((7, 5), yellow),
((8, 5), yellow),
((9, 5), black),
((10, 5), aqua),
((11, 5), white),
((12, 5), white),
((13, 5), black),
((14, 5), white),
((15, 5), black),

((1, 6), black),
((2, 6), white),
((3, 6), white),
((4, 6), white),
((5, 6), white),
((6, 6), white),
((7, 6), black),
((8, 6), yellow),
((9, 6), yellow),
((10, 6), black),
((11, 6), aqua),
((12, 6), white),
((13, 6), white),
((14, 6), white),
((15, 6), black),

((1, 7), black),
((2, 7), buff),
((3, 7), white),
((4, 7), white),
((5, 7), white),
((6, 7), buff),
((7, 7), black),
((8, 7), yellow),
((9, 7), yellow),
((10, 7), yellow),
((11, 7), black),
((12, 7), black),
((13, 7), black),
((14, 7), black),
((15, 7), black),
((16, 7), black),

((2, 8), black),
((3, 8), buff),
((4, 8), buff),
((5, 8), buff),
((6, 8), black),
((7, 8), yellow),
((8, 8), yellow),
((9, 8), yellow),
((10, 8), black),
((11, 8), orange),
((12, 8), orange),
((13, 8), orange),
((14, 8), orange),
((15, 8), orange),
((16, 8), orange),
((17, 8), black),

((3, 9), black),
((4, 9), black),
((5, 9), black),
((6, 9), yellow),
((7, 9), yellow),
((8, 9), yellow),
((9, 9), black),
((10, 9), orange),
((11, 9), black),
((12, 9), black),
((13, 9), black),
((14, 9), black),
((15, 9), black),
((16, 9), black),
((17, 9), black),

((3, 10), black),
((4, 10), deep_yellow),
((5, 10), deep_yellow),
((6, 10), yellow),
((7, 10), yellow),
((8, 10), yellow),
((9, 10), yellow),
((10, 10), black),
((11, 10), orange),
((12, 10), orange),
((13, 10), orange),
((14, 10), orange),
((15, 10), orange),
((16, 10), black),

((4, 11), black),
((5, 11), black),
((6, 11), deep_yellow),
((7, 11), deep_yellow),
((8, 11), deep_yellow),
((9, 11), deep_yellow),
((10, 11), deep_yellow),
((11, 11), black),
((12, 11), black),
((13, 11), black),
((14, 11), black),
((15, 11), black),

((6, 12), black),
((7, 12), black),
((8, 12), black),
((9, 12), black),
((10, 12), black)
)

#云用到的颜色*****************************************************************************
light_blue = (0,188,212)
blue = (3,169,244)
pink = (233,30,99)

build_CLOUD=(
((7,1), blue),
((8,1), blue),
((9,1), blue),
((10,1), blue),

((6,2), blue),
((7,2), white),
((8,2), white),
((9,2), light_blue),
((10,2), light_blue),
((11,2), blue),

((5,3), blue),
((6,3), white),
((7,3), white),
((8,3), white),
((9,3), white),
((10,3), light_blue),
((11,3), light_blue),
((12,3), blue),
((13,3), blue),
((14,3), blue),
((15,3), blue),

((3,4), blue),
((4,4), blue),
((5,4), blue),
((6,4), white),
((7,4), white),
((8,4), white),
((9,4), white),
((10,4), light_blue),
((11,4), light_blue),
((12,4), blue),
((13,4), white),
((14,4), white),
((15,4), light_blue),
((16,4), blue),

((2,5), blue),
((3,5), white),
((4,5), white),
((5,5), blue),
((6,5), white),
((7,5), white),
((8,5), white),
((9,5), white),
((10,5), white),
((11,5), white),
((12,5), white),
((13,5), white),
((14,5), white),
((15,5), white),
((16,5), light_blue),
((17,5), blue),

((1,6), blue),
((2,6), white),
((3,6), white),
((4,6), white),
((5,6), white),
((6,6), white),
((7,6), white),
((8,6), white),
((9,6), white),
((10,6), white),
((11,6), white),
((12,6), white),
((13,6), white),
((14,6), white),
((15,6), white),
((16,6), light_blue),
((17,6), blue),

((1,7), blue),
((2,7), white),
((3,7), white),
((4,7), white),
((5,7), black),
((6,7), white),
((7,7), white),
((8,7), white),
((9,7), white),
((10,7), white),
((11,7), white),
((12,7), white),
((13,7), black),
((14,7), white),
((15,7), white),
((16,7), light_blue),
((17,7), blue),
((19,7), blue),

((1,8), blue),
((2,8), white),
((3,8), white),
((4,8), white),
((5,8), black),
((6,8), white),
((7,8), white),
((8,8), white),
((9,8), white),
((10,8), white),
((11,8), white),
((12,8), white),
((13,8), black),
((14,8), white),
((15,8), white),
((16,8), blue),
((17,8), blue),
((18,8), blue),
((19,8), blue),

((1,9),blue),
((2,9), white),
((3,9), white),
((4,9), pink),
((5,9), white),
((6,9), pink),
((7,9), white),
((8,9), white),
((9,9), white),
((10,9), white),
((11,9), white),
((12,9), pink),
((13,9), white),
((14,9), pink),
((15,9), white),
((16,9), white),
((17,9), white),
((18,9), light_blue),
((19,9), blue),

((2,10), blue),
((3,10), white),
((4,10), pink),
((5,10), pink),
((6,10), pink),
((7,10), black),
((8,10), black),
((9,10), black),
((10,10), black),
((11,10), black),
((12,10), pink),
((13,10), pink),
((14,10), pink),
((15,10), white),
((16,10), light_blue),
((17,10), light_blue),
((18,10), blue),

((3,11), blue),
((4,11), blue),
((5,11), white),
((6,11), white),
((7,11), black),
((8,11), white),
((9,11), white),
((10,11), white),
((11,11), black),
((12,11), white),
((13,11), white),
((14,11), white),
((15,11), blue),
((16,11), blue),
((17,11), blue),

((4,12), blue),
((5,12), white),
((6,12), white),
((7,12), white),
((8,12), black),
((9,12), black),
((10,12), black),
((11,12), white),
((12,12), white),
((13,12), white),
((14,12), light_blue),
((15,12), blue),

((4,13), blue),
((5,13), light_blue),
((6,13), white),
((7,13), white),
((8,13), white),
((9,13), white),
((10,13), white),
((11,13), white),
((12,13), white),
((13,13), light_blue),
((14,13), light_blue),
((15,13), blue),

((5,14), blue),
((6,14), light_blue),
((7,14), light_blue),
((8,14), light_blue),
((9,14), blue),
((10,14), light_blue),
((11,14), light_blue),
((12,14), light_blue),
((13,14), light_blue),
((14,14), blue),

((6,15), blue),
((7,15), blue),
((8,15), blue),
((10,15), blue),
((11,15), blue),
((12,15), blue),
((13,15), blue)
)

#启动开关用到的颜色*****************************************************
green = (120,240,90)

build_SWITCH=(
((4, 1), green),
((5, 1), green),
((6, 1), green),
((7, 1), green),
((8, 1), green),
((9, 1), green),
((10, 1), green),
((11, 1), green),
((12, 1), green),
((13, 1), green),
((14, 1), green),
((15, 1), green),

((3, 2), green),
((4, 2), white),
((5, 2), white),
((6, 2), white),
((7, 2), white),
((8, 2), white),
((9, 2), white),
((10, 2), white),
((11, 2), white),
((12, 2), white),
((13, 2), white),
((14, 2), white),
((15, 2), white),
((16, 2), green),

((2, 3), green),
((3, 3), white),
((4, 3), white),
((5, 3), white),
((6, 3), white),
((7, 3), pink),
((8, 3), white),
((9, 3), white),
((10, 3), white),
((11, 3), white),
((12, 3), white),
((13, 3), white),
((14, 3), white),
((15, 3), white),
((16, 3), white),
((17, 3), green),

((1, 4), green),
((2, 4), white),
((3, 4), white),
((4, 4), white),
((5, 4), white),
((6, 4), white),
((7, 4), pink),
((8, 4), pink),
((9, 4), white),
((10, 4), white),
((11, 4), white),
((12, 4), white),
((13, 4), white),
((14, 4), white),
((15, 4), white),
((16, 4), white),
((17, 4), white),
((18, 4), green),

((1, 5), green),
((2, 5), white),
((3, 5), white),
((4, 5), white),
((5, 5), white),
((6, 5), white),
((7, 5), pink),
((8, 5), pink),
((9, 5), pink),
((10, 5), pink),
((11, 5), white),
((12, 5), white),
((13, 5), white),
((14, 5), white),
((15, 5), white),
((16, 5), white),
((17, 5), white),
((18, 5), green),

((1, 6), green),
((2, 6), white),
((3, 6), white),
((4, 6), white),
((5, 6), white),
((6, 6), white),
((7, 6), pink),
((8, 6), pink),
((9, 6), pink),
((10, 6), pink),
((11, 6), pink),
((12, 6), white),
((13, 6), white),
((14, 6), white),
((15, 6), white),
((16, 6), white),
((17, 6), white),
((18, 6), green),

((1, 7), green),
((2, 7), white),
((3, 7), white),
((4, 7), white),
((5, 7), white),
((6, 7), white),
((7, 7), pink),
((8, 7), pink),
((9, 7), pink),
((10, 7), pink),
((11, 7), pink),
((12, 7), pink),
((13, 7), white),
((14, 7), white),
((15, 7), white),
((16, 7), white),
((17, 7), white),
((18, 7), green),

((1, 8), green),
((2, 8), white),
((3, 8), white),
((4, 8), white),
((5, 8), white),
((6, 8), white),
((7, 8), pink),
((8, 8), pink),
((9, 8), pink),
((10, 8), pink),
((11, 8), pink),
((12, 8), white),
((13, 8), white),
((14, 8), white),
((15, 8), white),
((16, 8), white),
((17, 8), white),
((18, 8), green),

((1, 9), green),
((2, 9), white),
((3, 9), white),
((4, 9), white),
((5, 9), white),
((6, 9), white),
((7, 9), pink),
((8, 9), pink),
((9, 9), pink),
((10, 9), pink),
((11, 9), white),
((12, 9), white),
((13, 9), white),
((14, 9), white),
((15, 9), white),
((16, 9), white),
((17, 9), white),
((18, 9), green),

((1, 10), green),
((2, 10), white),
((3, 10), white),
((4, 10), white),
((5, 10), white),
((6, 10), white),
((7, 10), pink),
((8, 10), pink),
((9, 10), white),
((10, 10), white),
((11, 10), white),
((12, 10), white),
((13, 10), white),
((14, 10), white),
((15, 10), white),
((16, 10), white),
((17, 10), white),
((18, 10), green),

((2, 11), green),
((3, 11), white),
((4, 11), white),
((5, 11), white),
((6, 11), white),
((7, 11), pink),
((8, 11), white),
((9, 11), white),
((10, 11), white),
((11, 11), white),
((12, 11), white),
((13, 11), white),
((14, 11), white),
((15, 11), white),
((16, 11), white),
((17, 11), green),

((3, 12), green),
((4, 12), white),
((5, 12), white),
((6, 12), white),
((7, 12), white),
((8, 12), white),
((9, 12), white),
((10, 12), white),
((11, 12), white),
((12, 12), white),
((13, 12), white),
((14, 12), white),
((15, 12), white),
((16, 12), green),

((4, 13), green),
((5, 13), green),
((6, 13), green),
((7, 13), green),
((8, 13), green),
((9, 13), green),
((10, 13), green),
((11, 13), green),
((12, 13), green),
((13, 13), green),
((14, 13), green),
((15, 13), green),
)

#障碍物用到的颜色
green_1 = (203,251,174)
green_2 = (169,251,57)
green_3 = (15,220,10)

build_OBSTACLE = [
    ((1, 1), black),((2, 1), black),((3, 1), black),((4, 1), black),((5, 1), black),((6, 1), black),((7, 1), black),
    ((8, 1), black),((9, 1), black),((10, 1), black),((11, 1), black),((12, 1), black),((13, 1), black),
    ((14, 1), black),((15, 1), black),((16, 1), black),((17, 1), black),((18, 1), black),((19, 1), black),
    ((20, 1), black),((21, 1), black),

    ((1, 2), black),((2, 2), green_2),((3, 2), green_2),((4, 2), green_2),((5, 2), green_2),((6, 2), green_2),
    ((7, 2), green_2),((8, 2), green_2),((9, 2), green_2),((10, 2), green_2),((11, 2), green_2),((12, 2), green_2),
    ((13, 2), green_2),((14, 2), green_2),((15, 2), green_2),((16, 2), green_2),((17, 2), green_2),((18, 2), green_2),
    ((19, 2), green_2),((20, 2), green_2),((21, 2), black),

    ((1, 3), black),((2, 3), green_3),((3, 3), green_3),((4, 3), green_3),((5, 3), green_3),((6, 3), green_2),
    ((7, 3), green_1),((8, 3), green_2),((9, 3), green_3),((10, 3), green_3),((11, 3), green_3),((12, 3), green_3),
    ((13, 3), green_3),((14, 3), green_3),((15, 3), green_3),((16, 3), green_3),((17, 3), green_3),((18, 3), green_3),
    ((19, 3), green_3),((20, 3), green_3),((21, 3), black),

    ((1, 4), black), ((2, 4), green_1), ((3, 4), green_2), ((4, 4), green_3), ((5, 4), green_3), ((6, 4), green_1),
    ((7, 4), green_2), ((8, 4), green_1), ((9, 4), green_3), ((10, 4), green_1), ((11, 4), green_3), ((12, 4), green_3),
    ((13, 4), green_3), ((14, 4), green_2), ((15, 4), green_3), ((16, 4), green_2), ((17, 4), green_3),
    ((18, 4), green_2),((19, 4), green_1), ((20, 4), green_2), ((21, 4), black),

    ((1, 5), black), ((2, 5), green_2), ((3, 5), green_1), ((4, 5), green_3), ((5, 5), green_3), ((6, 5), green_2),
    ((7, 5), green_1), ((8, 5), green_2), ((9, 5), green_3), ((10, 5), green_1), ((11, 5), green_3), ((12, 5), green_3),
    ((13, 5), green_3), ((14, 5), green_3), ((15, 5), green_2), ((16, 5), green_3), ((17, 5), green_2),
    ((18, 5), green_3),((19, 5), green_2), ((20, 5), green_2), ((21, 5), black),

    ((1, 6), black), ((2, 6), green_1), ((3, 6), green_2), ((4, 6), green_3), ((5, 6), green_3), ((6, 6), green_1),
    ((7, 6), green_2), ((8, 6), green_1), ((9, 6), green_3), ((10, 6), green_1), ((11, 6), green_3), ((12, 6), green_3),
    ((13, 6), green_3), ((14, 6), green_2), ((15, 6), green_3), ((16, 6), green_2), ((17, 6), green_3),
    ((18, 6), green_2), ((19, 6), green_1), ((20, 6), green_2), ((21, 6), black),

    ((1, 7), black), ((2, 7), black), ((3, 7), black), ((4, 7), black), ((5, 7), black), ((6, 7), black),
    ((7, 7), black),
    ((8, 7), black), ((9, 7), black), ((10, 7), black), ((11, 7), black), ((12, 7), black), ((13, 7), black),
    ((14, 7), black), ((15, 7), black), ((16, 7), black), ((17, 7), black), ((18, 7), black), ((19, 7), black),
    ((20, 7), black), ((21, 7), black),

    ((3, 8), black), ((4, 8), green_2), ((5, 8), green_3), ((6, 8), green_3),((7, 8), green_2),((8, 8), green_1),
    ((9, 8), green_2), ((10, 8), green_3), ((11, 8), green_1), ((12, 8), green_3), ((13, 8), green_3),
    ((14, 8), green_3), ((15, 8), green_2), ((16, 8), green_3), ((17, 8), green_2), ((18, 8), green_2),
    ((19, 8), black),

    ((3, 9), black), ((4, 9), green_1), ((5, 9), green_3), ((6, 9), green_3), ((7, 9), green_1), ((8, 9), green_2),
    ((9, 9), green_1), ((10, 9), green_3), ((11, 9), green_1), ((12, 9), green_3), ((13, 9), green_3),
    ((14, 9), green_3), ((15, 9), green_3), ((16, 9), green_2), ((17, 9), green_1), ((18, 9), green_2),
    ((19, 9), black),

    ((3, 10), black), ((4, 10), green_2), ((5, 10), green_3), ((6, 10), green_3), ((7, 10), green_2), ((8, 10), green_1),
    ((9, 10), green_2), ((10, 10), green_3), ((11, 10), green_1), ((12, 10), green_3), ((13, 10), green_3),
    ((14, 10), green_3), ((15, 10), green_2), ((16, 10), green_3), ((17, 10), green_2), ((18, 10), green_2),
    ((19, 10), black),

    ((3, 11), black), ((4, 11), green_1), ((5, 11), green_3), ((6, 11), green_3), ((7, 11), green_1), ((8, 11), green_2),
    ((9, 11), green_1), ((10, 11), green_3), ((11, 11), green_1), ((12, 11), green_3), ((13, 11), green_3),
    ((14, 11), green_3), ((15, 11), green_3), ((16, 11), green_2), ((17, 11), green_1), ((18, 11), green_2),
    ((19, 11), black),

    ((3, 12), black), ((4, 12), green_2), ((5, 12), green_3), ((6, 12), green_3), ((7, 12), green_2),
    ((8, 12), green_1),
    ((9, 12), green_2), ((10, 12), green_3), ((11, 12), green_1), ((12, 12), green_3), ((13, 12), green_3),
    ((14, 12), green_3), ((15, 12), green_2), ((16, 12), green_3), ((17, 12), green_2), ((18, 12), green_2),
    ((19, 12), black),

    ((3, 13), black), ((4, 13), green_1), ((5, 13), green_3), ((6, 13), green_3), ((7, 13), green_1),
    ((8, 13), green_2),
    ((9, 13), green_1), ((10, 13), green_3), ((11, 13), green_1), ((12, 13), green_3), ((13, 13), green_3),
    ((14, 13), green_3), ((15, 13), green_3), ((16, 13), green_2), ((17, 13), green_1), ((18, 13), green_2),
    ((19, 13), black),

    ((3, 14), black), ((4, 14), green_2), ((5, 14), green_3), ((6, 14), green_3), ((7, 14), green_2),
    ((8, 14), green_1),
    ((9, 14), green_2), ((10, 14), green_3), ((11, 14), green_1), ((12, 14), green_3), ((13, 14), green_3),
    ((14, 14), green_3), ((15, 14), green_2), ((16, 14), green_3), ((17, 14), green_2), ((18, 14), green_2),
    ((19, 14), black),

    ((3, 15), black), ((4, 15), green_1), ((5, 15), green_3), ((6, 15), green_3), ((7, 15), green_1),
    ((8, 15), green_2),
    ((9, 15), green_1), ((10, 15), green_3), ((11, 15), green_1), ((12, 15), green_3), ((13, 15), green_3),
    ((14, 15), green_3), ((15, 15), green_3), ((16, 15), green_2), ((17, 15), green_1), ((18, 15), green_2),
    ((19, 15), black),

    ((3, 16), black), ((4, 16), green_2), ((5, 16), green_3), ((6, 16), green_3), ((7, 16), green_2),
    ((8, 16), green_1),
    ((9, 16), green_2), ((10, 16), green_3), ((11, 16), green_1), ((12, 16), green_3), ((13, 16), green_3),
    ((14, 16), green_3), ((15, 16), green_2), ((16, 16), green_3), ((17, 16), green_2), ((18, 16), green_2),
    ((19, 16), black),

    ((3, 17), black), ((4, 17), green_1), ((5, 17), green_3), ((6, 17), green_3), ((7, 17), green_1),
    ((8, 17), green_2),
    ((9, 17), green_1), ((10, 17), green_3), ((11, 17), green_1), ((12, 17), green_3), ((13, 17), green_3),
    ((14, 17), green_3), ((15, 17), green_3), ((16, 17), green_2), ((17, 17), green_1), ((18, 17), green_2),
    ((19, 17), black),

    ((3, 18), black), ((4, 18), green_2), ((5, 18), green_3), ((6, 18), green_3), ((7, 18), green_2),
    ((8, 18), green_1),
    ((9, 18), green_2), ((10, 18), green_3), ((11, 18), green_1), ((12, 18), green_3), ((13, 18), green_3),
    ((14, 18), green_3), ((15, 18), green_2), ((16, 18), green_3), ((17, 18), green_2), ((18, 18), green_2),
    ((19, 18), black),

    ((3, 19), black), ((4, 19), green_1), ((5, 19), green_3), ((6, 19), green_3), ((7, 19), green_1),
    ((8, 19), green_2),
    ((9, 19), green_1), ((10, 19), green_3), ((11, 19), green_1), ((12, 19), green_3), ((13, 19), green_3),
    ((14, 19), green_3), ((15, 19), green_3), ((16, 19), green_2), ((17, 19), green_1), ((18, 19), green_2),
    ((19, 19), black),

    ((3, 20), black), ((4, 20), green_2), ((5, 20), green_3), ((6, 20), green_3), ((7, 20), green_2),
    ((8, 20), green_1),
    ((9, 20), green_2), ((10, 20), green_3), ((11, 20), green_1), ((12, 20), green_3), ((13, 20), green_3),
    ((14, 20), green_3), ((15, 20), green_2), ((16, 20), green_3), ((17, 20), green_2), ((18, 20), green_2),
    ((19, 20), black),

    ((3, 21), black), ((4, 21), green_1), ((5, 21), green_3), ((6, 21), green_3), ((7, 21), green_1),
    ((8, 21), green_2),
    ((9, 21), green_1), ((10, 21), green_3), ((11, 21), green_1), ((12, 21), green_3), ((13, 21), green_3),
    ((14, 21), green_3), ((15, 21), green_3), ((16, 21), green_2), ((17, 21), green_1), ((18, 21), green_2),
    ((19, 21), black),

    ((3, 22), black), ((4, 22), green_2), ((5, 22), green_3), ((6, 22), green_3), ((7, 22), green_2),
    ((8, 22), green_1),
    ((9, 22), green_2), ((10, 22), green_3), ((11, 22), green_1), ((12, 22), green_3), ((13, 22), green_3),
    ((14, 22), green_3), ((15, 22), green_2), ((16, 22), green_3), ((17, 22), green_2), ((18, 22), green_2),
    ((19, 22), black),

    ((3, 23), black), ((4, 23), green_1), ((5, 23), green_3), ((6, 23), green_3), ((7, 23), green_1),
    ((8, 23), green_2),
    ((9, 23), green_1), ((10, 23), green_3), ((11, 23), green_1), ((12, 23), green_3), ((13, 23), green_3),
    ((14, 23), green_3), ((15, 23), green_3), ((16, 23), green_2), ((17, 23), green_1), ((18, 23), green_2),
    ((19, 23), black),

    ((3, 24), black), ((4, 24), green_2), ((5, 24), green_3), ((6, 24), green_3), ((7, 24), green_2),
    ((8, 24), green_1),
    ((9, 24), green_2), ((10, 24), green_3), ((11, 24), green_1), ((12, 24), green_3), ((13, 24), green_3),
    ((14, 24), green_3), ((15, 24), green_2), ((16, 24), green_3), ((17, 24), green_2), ((18, 24), green_2),
    ((19, 24), black),

    ((3, 25), black), ((4, 25), green_1), ((5, 25), green_3), ((6, 25), green_3), ((7, 25), green_1),
    ((8, 25), green_2),
    ((9, 25), green_1), ((10, 25), green_3), ((11, 25), green_1), ((12, 25), green_3), ((13, 25), green_3),
    ((14, 25), green_3), ((15, 25), green_3), ((16, 25), green_2), ((17, 25), green_1), ((18, 25), green_2),
    ((19, 25), black),

    ((3, 26), black), ((4, 26), green_2), ((5, 26), green_3), ((6, 26), green_3), ((7, 26), green_2),
    ((8, 26), green_1),
    ((9, 26), green_2), ((10, 26), green_3), ((11, 26), green_1), ((12, 26), green_3), ((13, 26), green_3),
    ((14, 26), green_3), ((15, 26), green_2), ((16, 26), green_3), ((17, 26), green_2), ((18, 26), green_2),
    ((19, 26), black),

    ((3, 27), black), ((4, 27), green_1), ((5, 27), green_3), ((6, 27), green_3), ((7, 27), green_1),
    ((8, 27), green_2),
    ((9, 27), green_1), ((10, 27), green_3), ((11, 27), green_1), ((12, 27), green_3), ((13, 27), green_3),
    ((14, 27), green_3), ((15, 27), green_3), ((16, 27), green_2), ((17, 27), green_1), ((18, 27), green_2),
    ((19, 27), black),

    ((3, 28), black), ((4, 28), green_2), ((5, 28), green_3), ((6, 28), green_3), ((7, 28), green_2),
    ((8, 28), green_1),
    ((9, 28), green_2), ((10, 28), green_3), ((11, 28), green_1), ((12, 28), green_3), ((13, 28), green_3),
    ((14, 28), green_3), ((15, 28), green_2), ((16, 28), green_3), ((17, 28), green_2), ((18, 28), green_2),
    ((19, 28), black),

    ((3, 29), black), ((4, 29), green_1), ((5, 29), green_3), ((6, 29), green_3), ((7, 29), green_1),
    ((8, 29), green_2),
    ((9, 29), green_1), ((10, 29), green_3), ((11, 29), green_1), ((12, 29), green_3), ((13, 29), green_3),
    ((14, 29), green_3), ((15, 29), green_3), ((16, 29), green_2), ((17, 29), green_1), ((18, 29), green_2),
    ((19, 29), black),

    ((3, 30), black), ((4, 30), green_2), ((5, 30), green_3), ((6, 30), green_3), ((7, 30), green_2),
    ((8, 30), green_1),
    ((9, 30), green_2), ((10, 30), green_3), ((11, 30), green_1), ((12, 30), green_3), ((13, 30), green_3),
    ((14, 30), green_3), ((15, 30), green_2), ((16, 30), green_3), ((17, 30), green_2), ((18, 30), green_2),
    ((19, 30), black),

    ((3, 31), black), ((4, 31), green_1), ((5, 31), green_3), ((6, 31), green_3), ((7, 31), green_1),
    ((8, 31), green_2),
    ((9, 31), green_1), ((10, 31), green_3), ((11, 31), green_1), ((12, 31), green_3), ((13, 31), green_3),
    ((14, 31), green_3), ((15, 31), green_3), ((16, 31), green_2), ((17, 31), green_1), ((18, 31), green_2),
    ((19, 31), black),

    ((3, 32), black), ((4, 32), green_2), ((5, 32), green_3), ((6, 32), green_3), ((7, 32), green_2),
    ((8, 32), green_1),
    ((9, 32), green_2), ((10, 32), green_3), ((11, 32), green_1), ((12, 32), green_3), ((13, 32), green_3),
    ((14, 32), green_3), ((15, 32), green_2), ((16, 32), green_3), ((17, 32), green_2), ((18, 32), green_2),
    ((19, 32), black),

    ((3, 33), black), ((4, 33), green_1), ((5, 33), green_3), ((6, 33), green_3), ((7, 33), green_1),
    ((8, 33), green_2),
    ((9, 33), green_1), ((10, 33), green_3), ((11, 33), green_1), ((12, 33), green_3), ((13, 33), green_3),
    ((14, 33), green_3), ((15, 33), green_3), ((16, 33), green_2), ((17, 33), green_1), ((18, 33), green_2),
    ((19, 33), black),

    ((3, 34), black), ((4, 34), green_2), ((5, 34), green_3), ((6, 34), green_3), ((7, 34), green_2),
    ((8, 34), green_1),
    ((9, 34), green_2), ((10, 34), green_3), ((11, 34), green_1), ((12, 34), green_3), ((13, 34), green_3),
    ((14, 34), green_3), ((15, 34), green_2), ((16, 34), green_3), ((17, 34), green_2), ((18, 34), green_2),
    ((19, 34), black),

    ((3, 35), black), ((4, 35), green_1), ((5, 35), green_3), ((6, 35), green_3), ((7, 35), green_1),
    ((8, 35), green_2),
    ((9, 35), green_1), ((10, 35), green_3), ((11, 35), green_1), ((12, 35), green_3), ((13, 35), green_3),
    ((14, 35), green_3), ((15, 35), green_3), ((16, 35), green_2), ((17, 35), green_1), ((18, 35), green_2),
    ((19, 35), black),

    ((3, 36), black), ((4, 36), green_2), ((5, 36), green_3), ((6, 36), green_3), ((7, 36), green_2),
    ((8, 36), green_1),
    ((9, 36), green_2), ((10, 36), green_3), ((11, 36), green_1), ((12, 36), green_3), ((13, 36), green_3),
    ((14, 36), green_3), ((15, 36), green_2), ((16, 36), green_3), ((17, 36), green_2), ((18, 36), green_2),
    ((19, 36), black),

    ((3, 37), black), ((4, 37), green_1), ((5, 37), green_3), ((6, 37), green_3), ((7, 37), green_1),
    ((8, 37), green_2),
    ((9, 37), green_1), ((10, 37), green_3), ((11, 37), green_1), ((12, 37), green_3), ((13, 37), green_3),
    ((14, 37), green_3), ((15, 37), green_3), ((16, 37), green_2), ((17, 37), green_1), ((18, 37), green_2),
    ((19, 37), black),

    ((3, 38), black), ((4, 38), green_2), ((5, 38), green_3), ((6, 38), green_3), ((7, 38), green_2),
    ((8, 38), green_1),
    ((9, 38), green_2), ((10, 38), green_3), ((11, 38), green_1), ((12, 38), green_3), ((13, 38), green_3),
    ((14, 38), green_3), ((15, 38), green_2), ((16, 38), green_3), ((17, 38), green_2), ((18, 38), green_2),
    ((19, 38), black),

    ((3, 39), black), ((4, 39), green_1), ((5, 39), green_3), ((6, 39), green_3), ((7, 39), green_1),
    ((8, 39), green_2),
    ((9, 39), green_1), ((10, 39), green_3), ((11, 39), green_1), ((12, 39), green_3), ((13, 39), green_3),
    ((14, 39), green_3), ((15, 39), green_3), ((16, 39), green_2), ((17, 39), green_1), ((18, 39), green_2),
    ((19, 39), black),

    ((3, 40), black), ((4, 40), green_2), ((5, 40), green_3), ((6, 40), green_3), ((7, 40), green_2),
    ((8, 40), green_1),
    ((9, 40), green_2), ((10, 40), green_3), ((11, 40), green_1), ((12, 40), green_3), ((13, 40), green_3),
    ((14, 40), green_3), ((15, 40), green_2), ((16, 40), green_3), ((17, 40), green_2), ((18, 40), green_2),
    ((19, 40), black),

    ((3, 41), black), ((4, 41), green_1), ((5, 41), green_3), ((6, 41), green_3), ((7, 41), green_1),
    ((8, 41), green_2),
    ((9, 41), green_1), ((10, 41), green_3), ((11, 41), green_1), ((12, 41), green_3), ((13, 41), green_3),
    ((14, 41), green_3), ((15, 41), green_3), ((16, 41), green_2), ((17, 41), green_1), ((18, 41), green_2),
    ((19, 41), black),

    ((3, 42), black), ((4, 42), green_2), ((5, 42), green_3), ((6, 42), green_3), ((7, 42), green_2),
    ((8, 42), green_1),
    ((9, 42), green_2), ((10, 42), green_3), ((11, 42), green_1), ((12, 42), green_3), ((13, 42), green_3),
    ((14, 42), green_3), ((15, 42), green_2), ((16, 42), green_3), ((17, 42), green_2), ((18, 42), green_2),
    ((19, 42), black),

    ((3, 43), black), ((4, 43), green_1), ((5, 43), green_3), ((6, 43), green_3), ((7, 43), green_1),
    ((8, 43), green_2),
    ((9, 43), green_1), ((10, 43), green_3), ((11, 43), green_1), ((12, 43), green_3), ((13, 43), green_3),
    ((14, 43), green_3), ((15, 43), green_3), ((16, 43), green_2), ((17, 43), green_1), ((18, 43), green_2),
    ((19, 43), black),

    ((3, 44), black), ((4, 44), green_2), ((5, 44), green_3), ((6, 44), green_3), ((7, 44), green_2),
    ((8, 44), green_1),
    ((9, 44), green_2), ((10, 44), green_3), ((11, 44), green_1), ((12, 44), green_3), ((13, 44), green_3),
    ((14, 44), green_3), ((15, 44), green_2), ((16, 44), green_3), ((17, 44), green_2), ((18, 44), green_2),
    ((19, 44), black),

    ((3, 45), black), ((4, 45), green_1), ((5, 45), green_3), ((6, 45), green_3), ((7, 45), green_1),
    ((8, 45), green_2),
    ((9, 45), green_1), ((10, 45), green_3), ((11, 45), green_1), ((12, 45), green_3), ((13, 45), green_3),
    ((14, 45), green_3), ((15, 45), green_3), ((16, 45), green_2), ((17, 45), green_1), ((18, 45), green_2),
    ((19, 45), black),

    ((3, 46), black), ((4, 46), green_2), ((5, 46), green_3), ((6, 46), green_3), ((7, 46), green_2),
    ((8, 46), green_1),
    ((9, 46), green_2), ((10, 46), green_3), ((11, 46), green_1), ((12, 46), green_3), ((13, 46), green_3),
    ((14, 46), green_3), ((15, 46), green_2), ((16, 46), green_3), ((17, 46), green_2), ((18, 46), green_2),
    ((19, 46), black),

    ((3, 47), black), ((4, 47), green_1), ((5, 47), green_3), ((6, 47), green_3), ((7, 47), green_1),
    ((8, 47), green_2),
    ((9, 47), green_1), ((10, 47), green_3), ((11, 47), green_1), ((12, 47), green_3), ((13, 47), green_3),
    ((14, 47), green_3), ((15, 47), green_3), ((16, 47), green_2), ((17, 47), green_1), ((18, 47), green_2),
    ((19, 47), black),

    ((3, 48), black), ((4, 48), green_2), ((5, 48), green_3), ((6, 48), green_3), ((7, 48), green_2),
    ((8, 48), green_1),
    ((9, 48), green_2), ((10, 48), green_3), ((11, 48), green_1), ((12, 48), green_3), ((13, 48), green_3),
    ((14, 48), green_3), ((15, 48), green_2), ((16, 48), green_3), ((17, 48), green_2), ((18, 48), green_2),
    ((19, 48), black),

    ((3, 49), black), ((4, 49), green_1), ((5, 49), green_3), ((6, 49), green_3), ((7, 49), green_1),
    ((8, 49), green_2),
    ((9, 49), green_1), ((10, 49), green_3), ((11, 49), green_1), ((12, 49), green_3), ((13, 49), green_3),
    ((14, 49), green_3), ((15, 49), green_3), ((16, 49), green_2), ((17, 49), green_1), ((18, 49), green_2),
    ((19, 49), black),

    ((3, 50), black), ((4, 50), green_2), ((5, 50), green_3), ((6, 50), green_3), ((7, 50), green_2),
    ((8, 50), green_1),
    ((9, 50), green_2), ((10, 50), green_3), ((11, 50), green_1), ((12, 50), green_3), ((13, 50), green_3),
    ((14, 50), green_3), ((15, 50), green_2), ((16, 50), green_3), ((17, 50), green_2), ((18, 50), green_2),
    ((19, 50), black),

    ((3, 51), black), ((4, 51), green_1), ((5, 51), green_3), ((6, 51), green_3), ((7, 51), green_1),
    ((8, 51), green_2),
    ((9, 51), green_1), ((10, 51), green_3), ((11, 51), green_1), ((12, 51), green_3), ((13, 51), green_3),
    ((14, 51), green_3), ((15, 51), green_3), ((16, 51), green_2), ((17, 51), green_1), ((18, 51), green_2),
    ((19, 51), black),

    ((3, 52), black), ((4, 52), green_2), ((5, 52), green_3), ((6, 52), green_3), ((7, 52), green_2),
    ((8, 52), green_1),
    ((9, 52), green_2), ((10, 52), green_3), ((11, 52), green_1), ((12, 52), green_3), ((13, 52), green_3),
    ((14, 52), green_3), ((15, 52), green_2), ((16, 52), green_3), ((17, 52), green_2), ((18, 52), green_2),
    ((19, 52), black),

    ((3, 53), black), ((4, 53), green_1), ((5, 53), green_3), ((6, 53), green_3), ((7, 53), green_1),
    ((8, 53), green_2),
    ((9, 53), green_1), ((10, 53), green_3), ((11, 53), green_1), ((12, 53), green_3), ((13, 53), green_3),
    ((14, 53), green_3), ((15, 53), green_3), ((16, 53), green_2), ((17, 53), green_1), ((18, 53), green_2),
    ((19, 53), black),

    ((3, 54), black), ((4, 54), green_2), ((5, 54), green_3), ((6, 54), green_3), ((7, 54), green_2),
    ((8, 54), green_1),
    ((9, 54), green_2), ((10, 54), green_3), ((11, 54), green_1), ((12, 54), green_3), ((13, 54), green_3),
    ((14, 54), green_3), ((15, 54), green_2), ((16, 54), green_3), ((17, 54), green_2), ((18, 54), green_2),
    ((19, 54), black),

    ((3, 55), black), ((4, 55), green_1), ((5, 55), green_3), ((6, 55), green_3), ((7, 55), green_1),
    ((8, 55), green_2),
    ((9, 55), green_1), ((10, 55), green_3), ((11, 55), green_1), ((12, 55), green_3), ((13, 55), green_3),
    ((14, 55), green_3), ((15, 55), green_3), ((16, 55), green_2), ((17, 55), green_1), ((18, 55), green_2),
    ((19, 55), black),

    ((3, 56), black), ((4, 56), green_2), ((5, 56), green_3), ((6, 56), green_3), ((7, 56), green_2),
    ((8, 56), green_1),
    ((9, 56), green_2), ((10, 56), green_3), ((11, 56), green_1), ((12, 56), green_3), ((13, 56), green_3),
    ((14, 56), green_3), ((15, 56), green_2), ((16, 56), green_3), ((17, 56), green_2), ((18, 56), green_2),
    ((19, 56), black),

    ((3, 57), black), ((4, 57), green_1), ((5, 57), green_3), ((6, 57), green_3), ((7, 57), green_1),
    ((8, 57), green_2),
    ((9, 57), green_1), ((10, 57), green_3), ((11, 57), green_1), ((12, 57), green_3), ((13, 57), green_3),
    ((14, 57), green_3), ((15, 57), green_3), ((16, 57), green_2), ((17, 57), green_1), ((18, 57), green_2),
    ((19, 57), black),

    ((3, 58), black), ((4, 58), green_2), ((5, 58), green_3), ((6, 58), green_3), ((7, 58), green_2),
    ((8, 58), green_1),
    ((9, 58), green_2), ((10, 58), green_3), ((11, 58), green_1), ((12, 58), green_3), ((13, 58), green_3),
    ((14, 58), green_3), ((15, 58), green_2), ((16, 58), green_3), ((17, 58), green_2), ((18, 58), green_2),
    ((19, 58), black),

    ((3, 59), black), ((4, 59), green_1), ((5, 59), green_3), ((6, 59), green_3), ((7, 59), green_1),
    ((8, 59), green_2),
    ((9, 59), green_1), ((10, 59), green_3), ((11, 59), green_1), ((12, 59), green_3), ((13, 59), green_3),
    ((14, 59), green_3), ((15, 59), green_3), ((16, 59), green_2), ((17, 59), green_1), ((18, 59), green_2),
    ((19, 59), black),

    ((3, 60), black), ((4, 60), green_2), ((5, 60), green_3), ((6, 60), green_3), ((7, 60), green_2),
    ((8, 60), green_1),
    ((9, 60), green_2), ((10, 60), green_3), ((11, 60), green_1), ((12, 60), green_3), ((13, 60), green_3),
    ((14, 60), green_3), ((15, 60), green_2), ((16, 60), green_3), ((17, 60), green_2), ((18, 60), green_2),
    ((19, 60), black),

    ((3, 61), black), ((4, 61), green_1), ((5, 61), green_3), ((6, 61), green_3), ((7, 61), green_1),
    ((8, 61), green_2),
    ((9, 61), green_1), ((10, 61), green_3), ((11, 61), green_1), ((12, 61), green_3), ((13, 61), green_3),
    ((14, 61), green_3), ((15, 61), green_3), ((16, 61), green_2), ((17, 61), green_1), ((18, 61), green_2),
    ((19, 61), black),

    ((3, 62), black), ((4, 62), green_2), ((5, 62), green_3), ((6, 62), green_3), ((7, 62), green_2),
    ((8, 62), green_1),
    ((9, 62), green_2), ((10, 62), green_3), ((11, 62), green_1), ((12, 62), green_3), ((13, 62), green_3),
    ((14, 62), green_3), ((15, 62), green_2), ((16, 62), green_3), ((17, 62), green_2), ((18, 62), green_2),
    ((19, 62), black),

    ((3, 63), black), ((4, 63), green_1), ((5, 63), green_3), ((6, 63), green_3), ((7, 63), green_1),
    ((8, 63), green_2),
    ((9, 63), green_1), ((10, 63), green_3), ((11, 63), green_1), ((12, 63), green_3), ((13, 63), green_3),
    ((14, 63), green_3), ((15, 63), green_3), ((16, 63), green_2), ((17, 63), green_1), ((18, 63), green_2),
    ((19, 63), black),

    ((3, 64), black), ((4, 64), green_2), ((5, 64), green_3), ((6, 64), green_3), ((7, 64), green_2),
    ((8, 64), green_1),
    ((9, 64), green_2), ((10, 64), green_3), ((11, 64), green_1), ((12, 64), green_3), ((13, 64), green_3),
    ((14, 64), green_3), ((15, 64), green_2), ((16, 64), green_3), ((17, 64), green_2), ((18, 64), green_2),
    ((19, 64), black),

    ((3, 65), black), ((4, 65), green_1), ((5, 65), green_3), ((6, 65), green_3), ((7, 65), green_1),
    ((8, 65), green_2),
    ((9, 65), green_1), ((10, 65), green_3), ((11, 65), green_1), ((12, 65), green_3), ((13, 65), green_3),
    ((14, 65), green_3), ((15, 65), green_3), ((16, 65), green_2), ((17, 65), green_1), ((18, 65), green_2),
    ((19, 65), black),

    ((3, 66), black), ((4, 66), green_2), ((5, 66), green_3), ((6, 66), green_3), ((7, 66), green_2),
    ((8, 66), green_1),
    ((9, 66), green_2), ((10, 66), green_3), ((11, 66), green_1), ((12, 66), green_3), ((13, 66), green_3),
    ((14, 66), green_3), ((15, 66), green_2), ((16, 66), green_3), ((17, 66), green_2), ((18, 66), green_2),
    ((19, 66), black),

    ((3, 67), black), ((4, 67), green_1), ((5, 67), green_3), ((6, 67), green_3), ((7, 67), green_1),
    ((8, 67), green_2),
    ((9, 67), green_1), ((10, 67), green_3), ((11, 67), green_1), ((12, 67), green_3), ((13, 67), green_3),
    ((14, 67), green_3), ((15, 67), green_3), ((16, 67), green_2), ((17, 67), green_1), ((18, 67), green_2),
    ((19, 67), black),

    ((3, 68), black), ((4, 68), green_2), ((5, 68), green_3), ((6, 68), green_3), ((7, 68), green_2),
    ((8, 68), green_1),
    ((9, 68), green_2), ((10, 68), green_3), ((11, 68), green_1), ((12, 68), green_3), ((13, 68), green_3),
    ((14, 68), green_3), ((15, 68), green_2), ((16, 68), green_3), ((17, 68), green_2), ((18, 68), green_2),
    ((19, 68), black),

    ((1, 69), black), ((2, 69), black), ((3, 69), black), ((4, 69), black), ((5, 69), black), ((6, 69), black),
    ((7, 69), black),
    ((8, 69), black), ((9, 69), black), ((10, 69), black), ((11, 69), black), ((12, 69), black), ((13, 69), black),
    ((14, 69), black), ((15, 69), black), ((16, 69), black), ((17, 69), black), ((18, 69), black), ((19, 69), black),
    ((20, 69), black), ((21, 69), black),

    ((1, 70), black), ((2, 70), green_1), ((3, 70), green_2), ((4, 70), green_3), ((5, 70), green_3), ((6, 70), green_1),
    ((7, 70), green_2), ((8, 70), green_1), ((9, 70), green_3), ((10, 70), green_1), ((11, 70), green_3),
    ((12, 70), green_3),((13, 70), green_3), ((14, 70), green_2), ((15, 70), green_3), ((16, 70), green_2),
    ((17, 70), green_3),((18, 70), green_2), ((19, 70), green_1), ((20, 70), green_2), ((21, 70), black),

    ((1, 71), black), ((2, 71), green_2), ((3, 71), green_1), ((4, 71), green_3), ((5, 71), green_3), ((6, 71), green_2),
    ((7, 71), green_1), ((8, 71), green_2), ((9, 71), green_3), ((10, 71), green_1), ((11, 71), green_3),
    ((12, 71), green_3),((13, 71), green_3), ((14, 71), green_3), ((15, 71), green_2), ((16, 71), green_3),
    ((17, 71), green_2), ((18, 71), green_3), ((19, 71), green_2), ((20, 71), green_2), ((21, 71), black),

    ((1, 72), black), ((2, 72), green_1), ((3, 72), green_2), ((4, 72), green_3), ((5, 72), green_3),
    ((6, 72), green_1),((7, 72), green_2), ((8, 72), green_1), ((9, 72), green_3), ((10, 72), green_1),
    ((11, 72), green_3), ((12, 72), green_3),((13, 72), green_3), ((14, 72), green_2), ((15, 72), green_3),
    ((16, 72), green_2), ((17, 72), green_3),((18, 72), green_2), ((19, 72), green_1), ((20, 72), green_2),
    ((21, 72), black),

    ((1, 73), black), ((2, 73), green_3), ((3, 73), green_3), ((4, 73), green_3), ((5, 73), green_3),
    ((6, 73), green_2),((7, 73), green_1), ((8, 73), green_2), ((9, 73), green_3), ((10, 73), green_3),
    ((11, 73), green_3), ((12, 73), green_3),((13, 73), green_3), ((14, 73), green_3), ((15, 73), green_3),
    ((16, 73), green_3), ((17, 73), green_3),((18, 73), green_3),((19, 73), green_3), ((20, 73), green_3),
    ((21, 73), black),

    ((1, 74), black), ((2, 74), green_2), ((3, 74), green_2), ((4, 74), green_2), ((5, 74), green_2),
    ((6, 74), green_2),((7, 74), green_2), ((8, 74), green_2), ((9, 74), green_2), ((10, 74), green_2),
    ((11, 74), green_2), ((12, 74), green_2),((13, 74), green_2), ((14, 74), green_2), ((15, 74), green_2),
    ((16, 74), green_2), ((17, 74), green_2),((18, 74), green_2),((19, 74), green_2), ((20, 74), green_2),
    ((21, 74), black),

    ((1, 75), black), ((2, 75), black), ((3, 75), black), ((4, 75), black), ((5, 75), black), ((6, 75), black),
    ((7, 75), black),((8, 75), black), ((9, 75), black), ((10, 75), black), ((11, 75), black), ((12, 75), black),
    ((13, 75), black),((14, 75), black), ((15, 75), black), ((16, 75), black), ((17, 75), black), ((18, 75), black),
    ((19, 75), black),((20, 75), black), ((21, 75), black),
]
pygame.init()

size = width, height = 600,600    #窗口大小

screen = pygame.display.set_mode(size)

pygame.display.set_caption("flybird")

score = 0
#读取最高纪录
# try:
#     f = open("record.txt")
#     score = int(f.read())
#     f.close()
# except IOError:
#     with open("record.txt", mode='a', encoding='utf-8') as write:
#         write.write("0")

#开关
switch = Element((10, 10),(13, 18), build_SWITCH)
switch.move((width / 2 - 90,height / 2 - 80))

#云的动画
def cloud_animation(cloud):
    if cloud.shifting[0] < - (cloud.scale[1] * cloud.pixelScale[1]):
        cloud.move((size[0], cloud.shifting[1]))
    cloud.move(( cloud.shifting[0] + cloud.speed[0], cloud.shifting[1] ))
    cloud.draw(screen)

#障碍物的动画
def obstacle_animation(obstacle,ran,bird_height):
    if obstacle.shifting[0] < - (obstacle.scale[1] * obstacle.pixelScale[1]):
        obstacle.move((size[0], obstacle.shifting[1] + ran * (obstacle.scale[1] * obstacle.pixelScale[1]) ))
    obstacle.move(( obstacle.shifting[0] - 1, obstacle.shifting[1] ))
    obstacle.draw(screen)
    if (obstacle.shifting[0] < size[0] / 2) and (obstacle.shifting[0] > size[0] / 2 - 60):   #可能发生碰撞的矩形区域
        if obstacle.shifting[1] < 0:  #和上管道相撞的区域
            if obstacle.shifting[1] + 375 >= bird_height: #和上管道右侧相撞的区域
                if obstacle.shifting[0] < size[0] / 2:
                    return True
                else: return False
            elif obstacle.shifting[0] < size[0] / 2:
                if obstacle.shifting[1] + 375 >=bird_height:
                    return  True
                else: return False
        elif obstacle.shifting[1] < bird_height:
            if obstacle.shifting[0] < size[0] / 2:
                return True
            else: return False
        elif obstacle.shifting[0] < size[0] / 2:
            if obstacle.shifting[1] < bird_height:
                return True
            else: return False

#主循环帧数
fps = 500
fclock = pygame.time.Clock()

#游戏开始之后的循环
def start_fly(screen):
    pygame.mouse.set_cursor(*pygame.cursors.ball)
    score = 0

    # 鸟
    bird = Element((3, 3), (11, 17), build_BIRD)
    bird.move((size[0] / 2 - 60, size[1] / 4))
    bird.draw(screen)
    bird.speed = [0,0]

    # 云
    cloud_1 = Element((5, 5), (15, 19), build_CLOUD)
    cloud_1.move((size[0] / 6, size[1] / 5))
    cloud_1.setSpeed((-0.7, 0))

    cloud_2 = Element((7, 7), (15, 19), build_CLOUD)
    cloud_2.move((size[0] / 1.2, size[1] / 3))
    cloud_2.setSpeed((-1.5, 0))

    cloud_3 = Element((10, 10), (15, 19), build_CLOUD)
    cloud_3.move((size[0] / 2, size[1] / 1.5))
    cloud_3.setSpeed((-2, 0))

    #障碍管道
    obstacle_1_1 = Element((5, 5), (75, 21), build_OBSTACLE)
    obstacle_1_1.move((size[0], -size[1] / 3.5))
    obstacle_1_2 = Element((5, 5), (75, 21), build_OBSTACLE)
    obstacle_1_2.move((size[0], 1.3*size[1] - obstacle_1_2.scale[0]*obstacle_1_2.pixelScale[0]))

    obstacle_2_1 = Element((5, 5), (75, 21), build_OBSTACLE)
    obstacle_2_1.move((size[0] *1.4 , -size[1] / 3.5))
    obstacle_2_2 = Element((5, 5), (75, 21), build_OBSTACLE)
    obstacle_2_2.move((size[0] *1.4, 1.3*size[1] - obstacle_2_2.scale[0]*obstacle_2_2.pixelScale[0]))

    obstacle_3_1 = Element((5, 5), (75, 21), build_OBSTACLE)
    obstacle_3_1.move((size[0] *1.7 , -size[1] / 3.5))
    obstacle_3_2 = Element((5, 5), (75, 21), build_OBSTACLE)
    obstacle_3_2.move((size[0] *1.7, 1.3*size[1] - obstacle_3_2.scale[0]*obstacle_3_2.pixelScale[0]))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
#鼠标点击能够对鸟产生瞬时向上的大的加速度使速度反向减少
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pressed()
                if mouse[2]:
                    bird.speed[1] -= 25

        cloud_animation(cloud_1)
        cloud_animation(cloud_2)

        if bird.shifting[1] <= 0 or bird.shifting[1] >= size[1] - 55:
                return score

#给鸟提供始终向下的加速度
        bird.move((bird.shifting[0], bird.shifting[1] + bird.speed[1]))
        bird.speed[1] += 1
        bird.draw(screen)

#产生随机数使障碍物的高度范围内随机
        ran = random.random() * 1.6 - 0.8
        if obstacle_animation(obstacle_1_1,ran,bird.shifting[1]): return score
        if obstacle_animation(obstacle_1_2,ran,bird.shifting[1]): return score


        ran = random.random() * 1.6 - 0.8
        if obstacle_animation(obstacle_2_1,ran,bird.shifting[1]): return score
        if obstacle_animation(obstacle_2_2,ran,bird.shifting[1]): return score

        ran = random.random() * 1.6 - 0.8
        if obstacle_animation(obstacle_3_1,ran,bird.shifting[1]): return score
        if obstacle_animation(obstacle_3_2,ran,bird.shifting[1]): return score

        if (obstacle_1_1.shifting[0] + 105 == width / 2) or (obstacle_2_1.shifting[0] + 105 == width / 2) or (obstacle_3_1.shifting[0] + 105 == width / 2):
            score+=1

#每过一个障碍物加一分，显示分数
        score_ten = Element( (10,10),(5,5), LETTER[ int (score / 10) ] )
        score_one = Element( (10,10),(5,5), LETTER[ score % 10] )
        score_ten.move((10,0))
        score_one.move((60,0))
        score_ten.draw(screen)
        score_one.draw(screen)

        cloud_animation(cloud_3)
        pygame.display.update()
        screen.fill((225, 255, 255))
        fclock.tick(fps)

def dead(screen,score):
    # 死
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    loc = pygame.mouse.get_pos()
                    #开始新游戏
                    if (loc[0] > width / 2 - 90) and (loc[0] < width / 2 + 90) and (loc[1] > height / 2 - 80) and (loc[1] < height / 2 + 80):
                        score = start_fly(screen)
                        # #保存最高纪录
                        # read = open("record.txt","r")
                        # string = int(read.read(2))
                        # read.close()
                        # if  string < score:
                        #     write = open("record.txt","w")
                        #     write.write(str(score))
                        #     write.close()
#显示上一次游戏分数
        score_ten = Element( (10,10),(5,5), LETTER[ int (score / 10) ] )
        score_one = Element( (10,10),(5,5), LETTER[ score % 10] )
        score_ten.move((10,0))
        score_one.move((60,0))
        score_ten.draw(screen)
        score_one.draw(screen)

        switch.draw(screen)

        loc = pygame.mouse.get_pos()
#更换鼠标样式
        if (loc[0] > width / 2 - 90) and (loc[0] < width / 2 + 90) and (loc[1] > height / 2 - 80) and (
                loc[1] < height / 2 + 80):
            pygame.mouse.set_cursor(*pygame.cursors.broken_x)
        else:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
        pygame.display.update()
        screen.fill((225,255,255))
        fclock.tick(10)




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                loc = pygame.mouse.get_pos()
                if (loc[0] > width / 2 -90) and (loc[0] < width / 2 +90) and (loc[1] > height / 2 -80) and (loc [1] < height / 2 +80):
                    dead(screen,start_fly(screen))

    loc = pygame.mouse.get_pos()
    if (loc[0] > width / 2 -90) and (loc[0] < width / 2 +90) and (loc[1] > height / 2 -80) and (loc [1] < height / 2 +80):
        pygame.mouse.set_cursor(*pygame.cursors.broken_x)
    else:
        pygame.mouse.set_cursor(*pygame.cursors.arrow)
    switch.draw(screen)
#显示历史最高记录
    score_ten = Element((10, 10), (5, 5), LETTER[int(score / 10)])
    score_one = Element((10, 10), (5, 5), LETTER[score % 10])
    score_ten.move((10, 0))
    score_one.move((60, 0))
    score_ten.draw(screen)
    score_one.draw(screen)

    pygame.display.update()
    screen.fill((225,255,255))
    fclock.tick(fps)
