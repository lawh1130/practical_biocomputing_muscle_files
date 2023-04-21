#subprocess commands
#did not work
import subprocess
import sys
from Bio.Align.Applications import MuscleCommandline
muscle_cline = MuscleCommandline(input="opuntia.fas")
child = subprocess.Popen(
     str(muscle_cline),
     stdout=subprocess.PIPE,
     stderr=subprocess.PIPE,
     text=True,
     shell=(sys.platform != "win64"),
 )

from Bio import AlignIO
align = AlignIO.read(child.stdout, "fasta")
print(align)