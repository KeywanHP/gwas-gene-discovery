# gwas-gene-discovery


#28.01.2019
#The script, map_snp_to_gene_v5.py was edited and now takes gwas results outputted from GAPIT to return genes associated with significant snps and functional annotation.



#A virtual environment in python2.7 must be set up first.
virtualenv-2.7 py27virtual
export PYTHONPATH="/home/apps/python/lib64/python2.7/site-manager/"
source py27virtual/bin/activate



#The following must be installed in python (readings shown below):

pip install traceback 
#https://docs.python.org/2/library/traceback.html

pip install requests 
#http://docs.python-requests.org/en/master/

pip install datetime
#https://docs.python.org/2/library/datetime.html


pip install json 
#https://docs.python.org/2/library/json.html


#The script requires the following to be in the same directory as the script:
gapit in .csv
annotation (in this case Os_Nipponbare_IRGSP_1_gene_Loci_and_designation.txt)
