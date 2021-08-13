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

directories = ['genie9.0', 'genie9.1','genie10.0']
versions = ['9.0', '9.1','10.0']
genes = ['JAK2', 'TET2']
for directory, version in zip(directories, versions):
    clinical_data = pd.read_table(directory + '/data_clinical_sample.txt',  low_memory=False)
    PV_samples = clinical_data[clinical_data['Oncotree Code']=='PV']
    print('count for ' + version + ':')
    mutations = pd.read_table(directory + '/data_mutations_extended.txt',  low_memory=False)
    for gene in genes:
        current_gene = mutations[mutations.Hugo_Symbol == gene].reset_index(drop=True)
        current_gene_PV = pd.merge(PV_samples, current_gene, left_on='Sample Identifier', right_on='Tumor_Sample_Barcode')
        print(' - ' + gene + ' ' + str(len(current_gene_PV)))
    
