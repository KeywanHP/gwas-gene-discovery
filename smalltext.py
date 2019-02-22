#!/usr/bin/python
import argparse

def jiatwo():
    args = args+2    

def jiasan():
    args = args+3

def mulsan():
    args = arg*3

def square():
    print(args.square**2)

if __name__ == "__main__":
    parser =argparse.ArgumentParser()
    parser.add_argument("square", help="square a number", type=int)
    args = parser.parse_args()
    square()

