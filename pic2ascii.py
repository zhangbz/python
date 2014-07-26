#!/usr/bin/env python
# coding=utf-8

'''
  ┏ ┓     ┏ ┓
┏ ┛ ┗ ━ ━ ┛ ┗ ┓
┃             ┃
┃      ━      ┃
┃  ┳ ┛   ┗ ┳  ┃
┃             ┃
┃  ``` ┻  ``` ┃
┃             ┃
┗ ━ ┓     ┏ ━ ┛
    ┃     ┃       Code is far away from bug with the animal protecting.
    ┃     ┃                      神兽护佑，代码无bug.
    ┃     ┗ ━ ━ ━ ━ ┓
    ┃               ┣ ┓ 
    ┃               ┏ ┛
    ┗ ┓ ┓ ┏ ━ ┳ ┓ ┏ ┛
      ┃ ┫ ┫   ┃ ┫ ┫
      ┗ ┻ ┛   ┗ ┻ ┛
'''

import sys
import Image

HEIGHT = 50
chars = "    ...',;:clodxkO0KXNWMMM"

def pic2ascii(filename):

    
    output = ''
    image = Image.open(filename)
    size = getsize(image)
    image = image.resize(size)
    image = image.convert('L')
    pixs = image.load()

    for y in range(size[1]):
        for x in range(size[0]):
            output += chars[pixs[x,y]/10]
        output += '\n'

    print output

def getsize(image):
    '''
    Calculate the target picture size
    '''
    s_width = image.size[0]
    print s_width
    s_height = image.size[1]
    print s_height
    t_height = HEIGHT
    print t_height
    t_width = (t_height * s_width) / s_height
    print t_width
    t_width = int(t_width * 2.3)
    print t_width
    t_size = (t_width, t_height)
    return t_size

if __name__ == '__main__':
    #print sys.argv
    if len(sys.argv) < 2:
        print "Useage: pic2ascii.py filename"
        sys.exit(1)
    filename = sys.argv[1]
    pic2ascii(filename)
