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
