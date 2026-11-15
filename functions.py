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

def reverse_complement(filename):
    sequence = read_sequence(filename)
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

    print("Reverse complement:", result)
    return result
