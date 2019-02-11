#!/bin/usr
import json
#json is quite messy when viewed in browser. Use these to make json neater.

#parse string content of json use loads s for str. #parse file use load.
with open("genes_only.json", "r") as f:
    content=json.load(f) #deserialise content into neat
    neat = json.dumps(content, indent=4, sort_keys=True) #re-serialize neat and indent by 4.
    #you will need the sort_keys parameter if you want the content to be displayed by their dictionary keys.
    with open("gene_only_copy.json", "w") as f2:
        f2.write(neat)
    f2.close()
f.close()

#this script was then supplemented by notepad replace \\t with \t and \\n with \n