def fasta_total(path):  
    sequences = read_fasta(path)
    count = len(sequences)
    return count