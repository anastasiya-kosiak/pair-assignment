def seq_length(path):   
    sequences = read_fasta(path)
    length = {}
    for name in sequences:
        seq = sequences[name]
        length[name] = len(seq)
    return length
  
def count_codons_by_header(sequences):
    counts = {}
    header = None
    for line in sequences:
        line = line.strip()
        if not line:
            print("empty file")
            continue
        if line.startswith(">"):
            header = line[1:]
            counts[header] = 0
        else:
            counts[header] += len(line)
    for header in counts:
        counts[header] = counts[header] // 3
    return counts

STOP_CODONS = ["TAA", "TAG", "TGA"]

def find_possible_orfs(lines, min_len=30):
    counts = {}
    header = None
    for line in lines:
        line = line.strip()
        if not line:
            print("empty file")
            continue
        if line.startswith(">"):
            header = line[1:]
            counts[header] = ""
        else:
            counts[header] += line.upper()
    orfs = {}
    for header, seq in counts.items():
        if len(seq) < min_len:
            print(f"{header} is too short")
            continue
        elif "N" in seq:
            print(f"{header}. Contains unknown bases")
            continue
        elif not seq.startswith("ATG"):
            print(f"{header}. Does not start with start codon")
            continue
        elif len(seq) % 3 != 0:
            print(f"{header}. Is not a multiple of 3")
            continue
        for i in range(0, len(seq), 3):
            if seq[i:i + 3] in STOP_CODONS:
                if i + 3 == len(seq):
                    orfs[header] = seq
                else:
                    print(f"{header}. Stop codon in the middle of the sequence")
                break
    return orfs

def nucleotide_percentage(sequences):
    for sequence in sequences:
        sequence = sequence.upper()
        length = len(sequence)

        a = sequence.count("A") / length * 100
        t = sequence.count("T") / length * 100
        g = sequence.count("G") / length * 100
        c = sequence.count("C") / length * 100

        print("Sequence:", sequence)
        print("A:", round(a, 2), "%")
        print("T:", round(t, 2), "%")
        print("G:", round(g, 2), "%")
        print("C:", round(c, 2), "%")
        print()

def reverse_complement(sequences):
    results = []

    for sequence in sequences:
        sequence = sequence.upper()
        result = ""

        for letter in sequence:
            if letter == "A":
                result = "T" + result
            elif letter == "T":
                result = "A" + result
            elif letter == "G":
                result = "C" + result
            elif letter == "C":
                result = "G" + result

        print("Sequence:          ", sequence)
        print("Reverse complement:", result)
        print()
        results.append(result)

    return results
