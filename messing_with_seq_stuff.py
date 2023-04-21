

#messing around with seq functions to get familiar

from Bio.Seq import Seq

my_seq = Seq("AGTACACTGGT")

print(my_seq)

#translate RNA

coding_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")

print(coding_dna.translate())

from Bio import SeqIO

for record in SeqIO.parse("fancy_fungi_its.fasta", "fasta"):
    print(record.id)

#excellent so far
