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