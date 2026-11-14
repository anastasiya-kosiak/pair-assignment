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

test = [">seq1 desc", "ATTATAATT", ">seq2", "ATGATG"]
print(count_codons_by_header(test))

with open("C:/KSE/programming_term_1/programming-basics/data/sequences.fasta") as f:
    count_codons_by_header
    print(count_codons_by_header(f))

    