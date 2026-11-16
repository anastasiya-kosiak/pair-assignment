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


