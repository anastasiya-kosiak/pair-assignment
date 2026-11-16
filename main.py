from functions import reverse_complement, nucleotide_percentage, read_fasta, seq_length, fasta_total, count_codons_by_header, find_possible_orfs

sequences = read_fasta("sequences.fasta")
print("The fasta file contains", fasta_total(sequences), "sequences.")
print("The lengths of the sequences are:", "\n", seq_length(sequences))

print(count_codons_by_header(sequences))
print(find_possible_orfs(sequences))
print(nucleotide_percentage(sequences))
print(reverse_complement(sequences))