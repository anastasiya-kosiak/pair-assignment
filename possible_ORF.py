STOP_CODONS = ["TAA", "TAG", "TGA"]

def check_sequence(seq, min_len = 30):
    seq = seq.strip().upper()
    if len(seq) < min_len:
        return "too short"
    if "N" in seq:
        return "contains unknown bases"
    if not seq.startswith("ATG"):
        return "no start codon ATG"
    if len(seq) % 3 != 0:
        return "length is not a multiple of 3"
    for i in range(0, len(seq), 3):
        if seq[i:i + 3] in STOP_CODONS:
            if i + 3 == len(seq):
                return "possible ORF"
            return "in-frame stop codon before end"
    return "no in-frame stop codon (incomplete ORF)"