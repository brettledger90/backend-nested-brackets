#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "Your Github Username"

import sys
opener = ['(','[','{','<','(*' ]
closer = [')', ']','}','>','*)']

def my_function(line):
    current_bracket = []
    temp_index = []
    index = 0

    while line:
        if len(line) > 1:
            if line[0] + line[1] in opener:
                current_bracket.append(line[0] + line[1])
                temp_index.append(opener.index(line[0] + line[1]))
                index += 1
                line = line[2:]
            elif line[0] in opener:
                current_bracket.append(line[0])
                temp_index.append(opener.index(line[0]))
                index += 1
                line = line[1:]
            elif line[0] + line[1] in closer:
                if temp_index[-1] == closer.index(line[0] + line[1]):
                    current_bracket.pop()
                    temp_index.pop()
                    index += 1
                    line = line[2:]
                else:
                    break
            elif line[0] in closer:
                if temp_index[-1] == closer.index(line[0]):
                    current_bracket.pop()
                    temp_index.pop()
                    index += 1
                    line = line[1:]
                else:
                    break
            elif line[0] not in opener and line[0] not in closer:
                line = line[1:]
                index += 1
        elif len(line) == 1:
            if line[0] in opener:
                current_bracket.append(line[0])
                temp_index.append(opener.index(line[0]))
                index += 1
            elif line[0] in closer:
                if temp_index[-1] == closer.index(line[0]):
                    current_bracket.pop()
                    temp_index.pop()
                    index += 1
                    line = line[1:]
                else:
                    break
            elif line[0] not in closer and line[0] not in opener:
                line = line[1:]
                index += 1

    if len(current_bracket) == 0:
        print('YES')
    else:
        print('No' + str(index + 1))
            



def read_file(filename):
    with open(filename) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        for i in content:
            my_function(i)

def main(args):
    read_file(args[1])
    
    


    

if __name__ == '__main__':
    main(sys.argv)
