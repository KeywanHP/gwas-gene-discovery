#!/usr/bin/python
import argparse

parser =argparse.ArgumentParser()
parser.add_argument("square", help="square a number", type=int)

args = parser.parse_args()

def square():
    print(args.square**2)

if __name__ == "__main__":
    square()