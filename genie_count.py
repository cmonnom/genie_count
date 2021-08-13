# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 17:05:40 2021

@author: Guillaume

A quick script (thanks Jeff) to evaluate the number of
specific mutation entries in a particular version of Genie.

Place genie data directories next to this script
Update directories, versions and genes arraya to parse
each genie directory and the list of genes you want to count

The output would be something like this:
count for 9.0:
 - JAK2 4
 - TET2 33
count for 9.1:
 - JAK2 136
 - TET2 31
count for 10.0:
 - JAK2 166
 - TET2 40

"""

import pandas as pd
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--paths-to-genie', nargs='+', default=['C:/Users/Guillaume/Documents/scripts/genie/genie10.0'], help='a list of paths to genie directories')
parser.add_argument('--genes', nargs='+', default=['JAK2', 'TET2'], help='a list of genes to count')
parser.add_argument('--oncotrees', nargs='+', default=['PV'], help='a list of oncotree codes')
args = parser.parse_args()
directories = args.paths_to_genie
genes = args.genes
oncotrees = args.oncotrees

#directories = ['genie9.0', 'genie9.1','genie10.0']
#versions = ['9.0', '9.1','10.0']
#genes = ['JAK2', 'TET2']
for directory in directories:
    mutations = pd.read_table(directory + '/data_mutations_extended.txt',  low_memory=False)
    clinical_data = pd.read_table(directory + '/data_clinical_sample.txt',  low_memory=False)
    print('Count for ' + directory + ':')
    for oncotree in oncotrees:
        print(' - Oncotree Code ' + oncotree + ':')
        oncotree_samples = clinical_data[clinical_data['Oncotree Code']== oncotree]
        for gene in genes:
            current_gene = mutations[mutations.Hugo_Symbol == gene].reset_index(drop=True)
            current_gene_oncotree = pd.merge(oncotree_samples, current_gene, left_on='Sample Identifier', right_on='Tumor_Sample_Barcode')
            print('  - ' + gene + ' ' + str(len(current_gene_oncotree)))
    
