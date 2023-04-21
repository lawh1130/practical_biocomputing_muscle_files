#here is where I will test out the request package in combo with the embl api code



if __name__ == '__main__':
    window = 20
    fastafile = 'fancy_fungi_its.fa'
    try:
        fasta = open(fastafile, 'r')
    except OSError:
        print(f'unable to open fasta file ({fastafile})')
# read and store sequences
    sequence = {}
    id = ''
    seq_n = 0
    for line in fasta:
        line = line.rstrip()
        if line.startswith('>'):
            # beginning of sequence
            seq_n += 1
            docline = line.lstrip('>').split(' ', maxsplit=1)
            id = docline[0]
            sequence[id] = ''

        else:
            sequence[id] += line

    print(f'{seq_n} sequences read from {fastafile}')
    print(sequence)

import requests
api_url = "https://www.ebi.ac.uk/Tools/services/rest/muscle/run"
version = u'2023-03-22 10:54'
todo = {"email": "lawh@purdue.edu", "title": "", "params" : dict(sequence = sequence, format = fasta)}
response = requests.post(api_url, params =todo)
print(response)

#api_url = "https://jsonplaceholder.typicode.com/todos"
#todo = {"userId": 1, "title": "Buy milk", "completed": False}
#response = requests.post(api_url, json=todo)
#print(response.json())

#Synchronous job:
#  The results/errors are returned as soon as the job is finished.
 # Usage: python muscle.py --email <your@email.com> [options...] <SeqFile|SeqID(s)>
 # Returns: results as an attachment

#[Required (for job submission)]
 # --email               E-mail address.
 # --sequence            Three or more sequences to be aligned can be entered
 #                       directly into this form. Sequences can be in GCG, FASTA,
 #                       EMBL (Nucleotide only), GenBank, PIR, NBRF, PHYLIP or
 #                       UniProtKB/Swiss-Prot (Protein only) format. Partially
 #                       formatted sequences are not accepted. Adding a return to the
 #                       end of the sequence may help certain applications understand
 #                       the input. Note that directly using data from word
 #                       processors may yield unpredictable results as hidden/control
 #                       characters may be present. There is currently a sequence
 #                       input limit of 500 sequences and 1MB of data.

#python muscle.py --email lawh@purdue.edu 'fancy_fungi_its.fa'>


#import ncbiblast.py as ncbi
#ncbi --help