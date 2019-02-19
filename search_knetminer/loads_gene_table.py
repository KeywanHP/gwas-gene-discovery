#!/bin/usr
from __future__ import print_function
import json
#json is quite messy when viewed in browser. Use these to make json neater.

#parse string content of json use loads s for str. #parse file use load.
def print_json():
    with open("genes_only_one.json", "r") as f:
        content=json.load(f) #deserialise content into neat
        neat = json.dumps(content, indent=4, sort_keys=True) #re-serialize neat and indent by 4.
        #you will need the sort_keys parameter if you want the content to be displayed by their dictionary keys.
        with open("gene_only_copy.json", "w") as f2:
            f2.write(neat)
        f2.close()
    f.close()

def print_extract():
    '''extract gene table from json'''
    with open("genes_only_one.json", "r") as f:
        content=json.load(f) #deserialise content into neat
        #print(type(content))
        with open("genetable.txt", "w") as g:
            g.write(content[u'geneTable']) #for some reason the json keys have to have a u in front.
        g.close()
    f.close()

def genesco():
    '''extract genes and scores from gene table'''
    with open("genetable.txt", "r") as f:
        next(f)
        with open("genes.txt", "w") as g:
            for line in f:
                col=line.split("\t")
                genes=col[1]
                score=col[6]
                print(type(genes))
                print(genes)
                print(score)
                print('{}\t{}'.format(genes, score), file=g)
        g.close()
    f.close()

if __name__=='__main__':
    #print_json
    print_extract()
    genesco()