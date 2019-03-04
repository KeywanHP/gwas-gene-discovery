#!/usr/bin/env/python
from __future__ import print_function
import os, urllib2

def getgs():
    '''Open gene list and use them to search Knetminer along with keywords'''
    with open("Results_formated_gene_and_designation.txt", "r") as gk:
        with open("genome.json", "w") as gf:
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
            r = urllib2.Request(url)
            Request.get_data(r)
            print(r, file=gf)
        gf.close()
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

def gene_score():
    '''Extract the scores only.'''
    with open("genetable.txt", "r") as f:
        next(f)
        with open(scores, "w") as sf:
            for line in f:
                col = line.split("\t")
                score=str(col[6]) 
                genes=col[1]
                pheno = ['coleoptile length','mesocotyl length','root length','seminal root length','Germination rate. Seedling growth.']
                #use str.join() to convert multiple elments in a list into one string.
                keyw = "+OR+".join(pheno)
                parameters = {"keyword":keyw, "list":genes}
                data = urllib.urlencode(parameters)
                link="http://knetminer.rothamsted.ac.uk/riceknet/genepage?"
                r=urllib2.Request(link, params=data)
                print("{}\t{}\t{}".format(genes, score, r.url), file=sf)
        sf.close()
    f.close()

def print_links():
    with open("document.txt", "w") as f:
        parameters = {"key1": value1, "key2": value2}
        url = <a website with http protocol>
        r = Request.get(url, params=parameters)
        print(r.url, file=f)
    f.close()

if __name__ == "__main__":
    getgs()
    parsejs()