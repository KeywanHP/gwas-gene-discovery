#!/usr/bin/env/python
from __future__ import print
import os, urllib2, 

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
        r = urllib2.Request(url, json.dump(<need to alter this into a dictionary>))
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