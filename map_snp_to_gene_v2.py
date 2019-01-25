'''
Created on 5 May 2015

@author: keywan hassani-pak

Script to filter significant SNPs in GWAS output and identify close genes

'''
import math, os

def findCloseGene(chr_snp, bp_snp):
	#input file - contains gene id and position [id,chr,beg,end]
	gene_file = 'H:\\workspace_python\\MAGIC\\ARALIP_genes.txt'
	score_threshold = 1.0
	max_distance = 1000
	with open(gene_file) as f:
		next(f)
		for line in f:
			col = line.split("\t")
			acc = col[0]
			chr_gene = int(col[1])
			beg_gene = int(col[2])
			end_gene = int(col[3])
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


if __name__ == '__main__':

        logP_threshold = 6

		#for any gwas file found in directory
        for file in os.listdir("A://MAGIC//out_05052015//default"):
                if file.endswith(".logP_modified.txt"):
                        print(file)
						#output 1: same as gwas file, but replaces snp name with gene name if conditions are met
                        out_file_gwas = file.replace("logP_modified","logP_modified_highlight")
						#output 2: file with all gene names
                        out_file_gene = file.replace("logP_modified","logP_modified_gene")
                        gwas_new_file = open(out_file_gwas, 'w')
                        print("SNP\tCHR\tBP\tP\tlogP", file=gwas_new_file)

                        highlight = []
                        with open(file) as f: #was gwas_file
                                next(f)
                                for line in f:
                                        col = line.split("\t")
                                        snp = col[0]
                                        chr_snp = int(col[1])
                                        bp_snp = int(col[2])
                                        pval = float(col[3])
                                        logP = float(col[4])
                                        gene = findCloseGene(chr_snp, bp_snp)
                                        if gene == "FooBar":
                                                print('{}\t{}\t{}\t{}\t{}'.format(snp,chr_snp,bp_snp,pval,logP), file=gwas_new_file)
                                        else:
                                                print('{}\t{}\t{}\t{}\t{}'.format(gene,chr_snp,bp_snp,pval,logP))
                                                if abs(math.log10(pval)) > logP_threshold:
                                                        highlight.append(gene)
                                                        print('{}\t{}\t{}\t{}\t{}'.format(gene,chr_snp,bp_snp,pval,logP), file=gwas_new_file)
                                                else:
                                                        print('{}\t{}\t{}\t{}\t{}'.format(snp,chr_snp,bp_snp,pval,logP), file=gwas_new_file)
                                                
                        gwas_new_file.close()
                        
                        highlight_file = open(out_file_gene, 'w')


                        for gene in set(highlight):
                                print(gene, file=highlight_file)
                                
                                
                        highlight_file.close()
