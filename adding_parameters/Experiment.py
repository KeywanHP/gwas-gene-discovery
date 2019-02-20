#!/usr/bin/python

'''use python argparse_intro.py --help to activate parameters'''

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("g", help="a gwas output ending in .csv (preferably from gapit)")
parser.add_argument("a", help="annotation file ending in .txt from a database")
parser.parse_args()
print(args.g)
print(args.a)