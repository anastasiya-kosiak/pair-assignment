def read_sequence(filename):
    sequence = ""
    file = open(filename)
    for line in file:
        line = line.strip()
        if line.startswith(">"):
            continue
        sequence = sequence + line.upper()
    file.close()
    return sequence

def nucleotide_percentage(filename):
    sequence = read_sequence(filename)
    length = len(sequence)

    a = sequence.count("A") / length * 100
    t = sequence.count("T") / length * 100
    g = sequence.count("G") / length * 100
    c = sequence.count("C") / length * 100

    print("A:", round(a, 2), "%")
    print("T:", round(t, 2), "%")
    print("G:", round(g, 2), "%")
    print("C:", round(c, 2), "%")

