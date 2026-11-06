sequence = "ATGAATTGCGCGTAGCTAGCTAG"

def count_gc_content(seq):
    count_c = seq.count("C")
    count_g = seq.count("G")
    count_gc = count_c + count_g
    gc_percent = count_gc/len(seq) * 100
    return round(gc_percent, 2)

print(count_gc_content(sequence))
