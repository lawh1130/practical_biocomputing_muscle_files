from Bio.Align.Applications import MuscleCommandline
cline = MuscleCommandline(input="opuntia.fasta", out="opuntia.txt")
print(cline)

#above prints out a command

#from Bio.Align.Applications import MuscleCommandline
#muscle_cline = MuscleCommandline(input="opuntia.fasta")
#stdout, stderr = muscle_cline()
#from io import StringIO
#from Bio import AlignIO
#align = AlignIO.read(StringIO(stdout), "fasta")
#print(align)