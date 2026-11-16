def seq_length(path):   
    sequences = read_fasta(path)
    length = {}
    for name in sequences:
        seq = sequences[name]
        length[name] = len(seq)
    return length