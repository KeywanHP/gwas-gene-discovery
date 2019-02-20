#!/usr/bin/python

#!/bin/usr
from __future__ import print_function
import json, requests

def getjson():
    with open("keywords.txt","r") as kw:
        kw.readline()
        r=requests.get("http://babvs67.rothamsted.ac.uk:8081/ws/rice/genome?keyword={}+OR+{}&list={}".format("moisture", "length"))
        r.json()
    kw.close()

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

def get_genetable():
    '''extract gene table from json'''
    with open("genes_only_one.json", "r") as f:
        content=json.load(f) #deserialise content into neat
        #print(type(content))
        with open("genetable.txt", "w") as g:
            g.write(content[u'geneTable']) #for some reason the json keys have to have a u in front.
        g.close()
    f.close()

def same_genes():
    '''extract common genes when comaring gene column of both files.'''
    with open("genetable.txt", "r") as f:
        with open("Results_formated_gene_and_designation.txt", "r") as g:
            for line in f:
                col=line.split("\t")
                genes=col[1]
                score=col[6]
                list(genes)
            for line in g:
                col=line.split("\t")
                gen=col[0]
                list(gen)              
        g.close()
    f.close()

if __name__=='__main__':
    get_json #will extract json based on string formatting of url
    print_json #makes json look nicer.
    get_genetable() #will extract the genetable from url
    same_genes()# will comopare gene table genes with the genes in results_formated_designation and get the identical ones.
    #need to look at whether you will need to extract gene table without downloading entire json.