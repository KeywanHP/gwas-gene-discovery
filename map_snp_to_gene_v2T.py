#!/usr/bin/python

#bring python3 print() into python2
from __future__ import print_function
import os, math, traceback, datetime

def resformat(res, filter):
    with open(res) as fres:
        next(fres)
        with open(filter, "w") as flt:
            snp = 0
            print("{}\t{}\t{}\t{}\t{}".format("SNPnum","CHR","snpBP","P","logP"), file=flt)
            for line in fres:
                snp += 1
                col = line.split(",")
                chro = col[1]
                bp = col[2]
                pval = float(col[3])
                logP = -math.log10(pval)
                print('{}\t{}\t{}\t{}\t{}'.format(snp,chro,bp,pval,logP), file=flt)
        flt.close()
    fres.close()
    return
#End of block1

def getsnps(filter, threshfile):
    with open(filter) as flt:
        next(flt)
        logP_threshold = 6
        with open(threshfile, "w") as fthresh:
            print("SNPnum\tCHR\tsnpBP\tP\tlogP", file=fthresh)
            for line in flt:
                col = line.split("\t")
                snp = col[0]
                chr_snp = int(col[1])
                bp_snp = int(col[2])
                pval = float(col[3])
                logP = float(col[4])
                if logP > logP_threshold:
                    print('{}\t{}\t{}\t{}\t{}'.format(snp,chr_snp,bp_snp,pval,logP), file=fthresh)
        fthresh.close()
    flt.close()
    return
#End of block2
  
def findCloseGene(chr_snp, bp_snp):
    score_threshold = 1.0
    max_distance = 1000
    with open(annotation) as f:
        next(f)
        for line in f:
            col = line.split("\t")
            acc = col[0]
            chr_gene = int(col[1])
            beg_gene = int(col[2])
            end_gene = int(col[3])
            design = col[4]
            #score = float(col[6])
            #SNP is within gene
            if (chr_snp == chr_gene) & (bp_snp > beg_gene) & (bp_snp < end_gene):
                #print('Found SNP within gene {}'.format(acc)) 
                return acc
            #SNP is down stream of gene with < max_distance 
            elif (chr_snp == chr_gene) & (abs(bp_snp - beg_gene) < max_distance):
                #print('Found SNP downstream of {}'.format(acc)) 
                return acc
            #SNP is up stream of gene with < max_distance 
            elif (chr_snp == chr_gene) & (abs(bp_snp - end_gene) < max_distance):
                #print('Found SNP upstream of {}'.format(acc)) 
                return acc
        return "FooBar"
    f.close()
#End of block3 to find the genes associated with snps.


def findCloseGeneDesign(chr_snp, bp_snp):
    print(os.listdir("."))
    score_threshold = 1.0
    max_distance = 1000
    with open(annotation) as f2:
        next(f2)
        for line in f2:
            col = line.split("\t")
            acc = col[0]
            chr_gene = int(col[1])
            beg_gene = int(col[2])
            end_gene = int(col[3])
            design = col[4]
            #score = float(col[6])
            #SNP is within gene
            if (chr_snp == chr_gene) & (bp_snp > beg_gene) & (bp_snp < end_gene):
                #print('Found SNP within gene {}'.format(design)) 
                return design
            #SNP is down stream of gene with < max_distance 
            elif (chr_snp == chr_gene) & (abs(bp_snp - beg_gene) < max_distance):
                #print('Found SNP downstream of {}'.format(design)) 
                return design
            #SNP is up stream of gene with < max_distance 
            elif (chr_snp == chr_gene) & (abs(bp_snp - end_gene) < max_distance):
                #print('Found SNP upstream of {}'.format(design)) 
                return design
        return "FooBar2"
    f2.close()
#End of block3.5 to find the annotation of the genes associated with snps.

def getgdp(threshfile, gdp, genedesign):
    with open(threshfile) as fthresh:
        next(fthresh)
        with open(gdp, "w") as fgdp:
            print("GENE\tCHR\tSNPnum\tsnpBP\tP\tlogP\tdesignation.txt", file=fgdp)
            highlight = []
            highlightdesign = []
            for line in fthresh:
                logP_threshold = 6
                col = line.split("\t")
                snp = col[0]
                snpnum = col[0]
                chr_snp = int(col[1])
                bp_snp = int(col[2])
                pval = float(col[3])
                logP = float(col[4])
                gene = findCloseGene(chr_snp, bp_snp)
                design = findCloseGeneDesign(chr_snp, bp_snp)
                blank = "-"
                if gene == "FooBar":
                    print('{}\t{}\t{}\t{}\t{}\t{}'.format(blank,blank,blank,blank,blank,blank), file=fgdp)
                else:
                    print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(gene,chr_snp,snpnum,bp_snp,pval,logP,design))
                    if logP > logP_threshold:
                        highlight.append(gene)
                        highlightdesign.append(design)
                        print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(gene,chr_snp,snpnum,bp_snp,pval,logP,design), file=fgdp)
                    else:
                        print('{}\t{}\t{}\t{}\t{}\t{}'.format(snp,chr_snp,snpnum,bp_snp,pval,logP), file=fgdp)
            with open(genedesign, "w") as gd:
                for design in set(highlightdesign):
                    print(design, file=gd)
            gd.close()        
        fgdp.close()
    fthresh.close()
    return
#End of block4 to produce the summary.

if __name__=="__main__":
    #1) Truncate results file and order by snps.
    res="GAPIT.MLM.DTF.GWAS.Results.csv"
    filter="GAPIT.MLM.DTF.GWAS.Results_filtered.txt"
    print("taking inputs from:{}".format(res))
    print("writing outputs to:{}".format(filter))      
    try:
        resformat(res, filter)
        print("finished extracting from: {}".format(res))
    except Exception:
        traceback.print_exc()

    #2) Obtain SNPs less than e-6 in p-value
    threshfile="Results_filtered_threshold.txt"
    print("reading from: {}".format(filter))
    print("extracting SNPS above threshold into: {}".format(threshfile))
    try:
        getsnps(filter, threshfile)
        print("finished extracting snps from: {}".format(threshfile))
    except Exception:
        traceback.print_exc()

    
    #3) define annotation file for findCloseGenes(genes) and findCloseGeneDesign(annotation)
    annotation="Os_Nipponbare_IRGSP_1_gene_Loci_and_designation.txt"

    
    #4) Obtain a file summarising the information.
    gdp="Results_filtered_gdp_FINAL.txt"
    genedesign="Results_formated_gene_and_designation.txt"
    print("producing summary of genes associated with significant SNPs")
    print("producing a file of genes associated with significant SNPs and annotations")
    try:
        getgdp(threshfile, gdp, genedesign)
        print("files produced")
    except Exception:
        traceback.print_exc()

print("The entire pipeline completed without errors")
print(datetime.datetime.now())