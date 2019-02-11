#!/usr/bin/python
import requests

#r=requests.get("http://babvs67.rothamsted.ac.uk:8081/ws/rice/genome?keyword=drought+OR+tolerance&list=ASR3,BADH1")
#you would need to modify the way the url is made. i.e. a list of keywords as iterables added to the list.
r=requests.get("http://babvs67:8081/ws/rice/genome")


