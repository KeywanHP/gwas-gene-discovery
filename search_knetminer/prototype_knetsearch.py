#!/usr/bin/env/python

from __future__ import print_function
import json, os, requests

#The .join() method concatenates each string element of an iterable into one single string.
#string.join(iterable)
#https://www.tutorialspoint.com/python/string_join.htm 
# you would hae to make col[0] into a list
#use .join() to add comma.

def getgs():
    '''Open gene list and use them to search Knetminer along with keywords'''
    with open("Results_formated_gene_and_designation.txt", "r") as gk:
        genes=[]
        for line in gk:
            col = line.split(" :: ")
            genes.append(col[0])
        genelist = (",").join(genes) #join all iterative elements by ,
        print(genelist)
        pheno = ["coleoptile length", "mesocotyl length", "root length", "seminal root length", "Germination rate. Seedling growth."]
        #use str.join() to convert multiple elments in a list into one string.
        keyw ="+OR+".join(pheno)
        url = "http://babvs67.rothamsted.ac.uk:8081/ws/rice/genome?keyword={}&list={}".format(keyw, genelist)
        print(url)
        r = requests.get(url)
        r.json()
    gk.close()
    return

def parsejs():
    ''' deserialise json into dictionary and extract the genetable which hopefully provide right genes and score given right url'''
    for file in os.listdir("."):
        if file.endswith(".json"):
            with open(file, "r") as jf:
                content=json.load(jf) #deserialise content of json, which will be dictionary object.
                #print(type(content))
                with open("genetable.txt", "w") as g:
                    g.write(content[u'geneTable']) #for some reason the json keys have to have a u in front.
                g.close()
    jf.close()
    return

def same_genes():
    '''compare with the designation file to check if genes are the same. If so, extract the scores only.'''
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

if __name__ == "__main__":
    getgs()
    parsejs()
    #same_genes() #might be unnecessary.