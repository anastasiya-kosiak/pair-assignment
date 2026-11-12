def read_fasta(path):
    sequences = {}
    name = None
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                name = line[1:]
                sequences[name] = ""
            else:
                sequences[name] += line
    return sequences

#to check if works on file:
#print(read_fasta("sequences.fasta"))

def seq_length(path):
    sequences = read_fasta(path)
    length = {}
    for name in sequences:
        seq = sequences[name]
        length[name] = len(seq)
    return length

#to check if works on file:
#print (seq_length("sequences.fasta"))

def fasta_total(path):
    sequences = read_fasta(path)
    count = len(sequences)
    return count

#to check if works on file:
print (fasta_total("sequences.fasta"))
