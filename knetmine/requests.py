#!/usr/bin/python
import requests

#you would need to modify the way the url is made. i.e. a list of keywords as iterables added to the list.
def getjson():
    with open("keywords","r") as kw:
        kw.readline()
        r=requests.get("http://babvs67.rothamsted.ac.uk:8081/ws/rice/genome?keyword={}+OR+{}&list={}".format(<keywords>))
    kw.close()

def get_genetable():
    for file in os.listdir("."):
        if file.endswith(".json")
        with open(file) as data:
            json.load(data)
            print(data[u'"geneTable'], file=somethin)



