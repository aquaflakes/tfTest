from pyensembl import EnsemblRelease

# release 77 uses human reference genome GRCh38
data = EnsemblRelease(77)

# will return ['HLA-A']



# get all exons associated with HLA-A
# exon_ids  = data .exon_ids_of_gene_name('HLA-A')ct.download()
data.download()
data.index()
gene_names = data.gene_names_at_locus(contig=6, position=29945884)

print (2)