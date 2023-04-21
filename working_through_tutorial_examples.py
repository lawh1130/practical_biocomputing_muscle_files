####Here is where I will work through various examples in the biopython tutorial

#link to tutorial:

#http://biopython.org/DIST/docs/tutorial/Tutorial.html


from Bio import SeqIO

for seq_record in SeqIO.parse("ls_orchid.fasta", "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))

#excellent, on to ch 3

from Bio.Seq import Seq
my_seq = Seq("GATCG")
for index, letter in enumerate(my_seq):
    print("%i %s" % (index, letter))

Seq("AAAA").count("AA")

#now skipping to ch 6.5

#copies and pasted notes

#Internally this uses the subprocess module which is now the recommended way to run another program in Python. This replaces older options like the os.system() and the os.popen* functions.

#Now, at this point it helps to know about how command line tools “work”. When you run a tool at the command line, it will often print text output directly to screen. This text can be captured or redirected, via two “pipes”, called standard output (the normal results) and standard error (for error messages and debug messages). There is also standard input, which is any text fed into the tool. These names get shortened to stdin, stdout and stderr. When the tool finishes, it has a return code (an integer), which by convention is zero for success.

#When you run the command line tool like this via the Biopython wrapper, it will wait for it to finish, and check the return code. If this is non zero (indicating an error), an exception is raised. The wrapper then returns two strings, stdout and stderr.

#In the case of ClustalW, when run at the command line all the important output is written directly to the output files. Everything normally printed to screen while you wait (via stdout or stderr) is boring and can be ignored (assuming it worked).


#from Bio.Align.Applications import ClustalwCommandline

#cline = ClustalwCommandline("clustalx", infile="opuntia.fasta")
#print(cline)

#from Bio import AlignIO
#align = AlignIO.read("opuntia.asl", "clustal")
#print(align)

#I'm gonna move on to the muscle stuff since the clustal file formatting is a huge pain

#from Bio.Align.Applications import MuscleCommandline

#help(MuscleCommandline)

#muscle_cline = MuscleCommandline(input="opuntia.fasta")
#stdout, stderr = muscle_cline()
#from io import StringIO
#from Bio import AlignIO
#align = AlignIO.read(StringIO(stdout), "fasta")
#print(align)

#from Bio.Align.Applications import MuscleCommandline
#muscle_cline = MuscleCommandline(input="opuntia.fasta")
#stdout, stderr = muscle_cline()
#from io import StringIO
#from Bio import AlignIO
#align = AlignIO.read(StringIO(stdout), "fasta")
#print(align)


#import subprocess
#from Bio.Align.Applications import MuscleCommandline
#muscle_cline = MuscleCommandline(input="opuntia.fasta")
#child = subprocess.Popen(
   # str(muscle_cline),
   # stdout=subprocess.PIPE,
   # stderr=subprocess.PIPE,
   # text=True,
   # shell=(sys.platform != "win64"),)
#from Bio import AlignIO
#align = AlignIO.read(child.stdout, "fasta")
#print(align)

#this straight up did not work either