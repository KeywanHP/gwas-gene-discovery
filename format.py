'''
Created on 5 May 2015

@author: keywan hassani-pak

Format GWAS file to include both p-value and logP-value

'''

import os, math

for file in os.listdir("."):
    if file.endswith(".logP.txt"):
        print(file)
        out_file = file.replace("logP","logP_modified")
        gwas_new_file = open(out_file, 'w')
        snp = 0
        with open(file) as f:
            next(f)
            print('{}\t{}\t{}\t{}\t{}'.format("SNP","CHR","BP","P","logP"), file=gwas_new_file)
            for line in f:
                snp += 1
                col = line.split(" ")
                chro = col[0]
                bp = col[1]
                logP = float(col[2])
                pval = pow(10,-1*logP)
                #print('{}\t{}\t{}\t{}\t{}'.format(snp,chro,bp,pval,logP))
                print('{}\t{}\t{}\t{}\t{}'.format(snp,chro,bp,pval,logP), file=gwas_new_file)
        
        gwas_new_file.close()
