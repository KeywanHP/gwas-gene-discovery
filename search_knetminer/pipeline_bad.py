#!/usr/bin/env/python

from __future__ import print_function
import json, requests

def getgk():
    with open("Results_formated_gene_and_designation.txt", "r") as gk:
        #do not use .readline() here for it seems to skip the header.
        for line in gk:
            col=line.split(" :: ")
            print(list(col[0]))
            with open("genes.txt", "w") as gf:
                print(genes, file=gf)
            gf.close()
    gk.close()
    return
#This way doesn't work because col[0] has the list of genes as distinct strings.
#Line 11 relies on the iteration in for line in gk to go through every gene.
#assigning it to something else will not work.

if __name__ == "__main__":
    getgk()