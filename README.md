Hi! Our team for this assignment is Olha, Yelyzaveta, and Anastasiia.
 
## Files in this repository
 
- **functions.py** contains all the functions for working with FASTA files (see the list below).
- **main.py** is the whole pipeline in one script. It reads `sequences.fasta` and runs every function on it, one after another: it prints the number of sequences, their lengths, the number of codons, the valid ORFs, the percentage of A, T, G and C, and the reverse complements.
- **sequences.fasta** is a test file in FASTA format with 6 made-up DNA sequences. In a FASTA file, each sequence starts with a header line beginning with `>`, followed by one or more lines of the sequence itself. The test sequences cover different cases: a complete gene, a short protein-coding sequence, a GC-rich fragment, and a low-quality read with unknown bases (`N`).
- **hello_anastasiia_kosiak.py**, **hello_liza.py**, **hello_olha.py** and **gc_tools.py** are practice files. We used them to learn how to work with branches and resolve merge conflicts, so you can ignore them.
## How to run
 
```bash
python3 main.py
```
 
## How to use the functions
 
First read the FASTA file once with `read_fasta`, then pass the result to the other functions.
 
### Example
 
```python
from functions import *
 
seqs = read_fasta("sequences.fasta")
 
seq_length(seqs)                       # {name: length}
fasta_total(seqs)                      # number of sequences
count_codons_by_header(seqs)           # {name: number of codons}
find_possible_orfs(seqs)               # {name: seq} for valid ORFs
nucleotide_percentage(seqs.values())
reverse_complement(seqs.values())
```
 
Note: the last two functions take `seqs.values()` (sequences only, without headers).
 
## Functions
 
1. **read_fasta(path)** reads a FASTA file and returns a dictionary `{name: seq}`.
   - `path` is the path to the FASTA file.
   - The key is the header (without `>`), and the value is the full sequence (multi-line sequences are joined).
2. **seq_length(sequences)** takes the dictionary from `read_fasta` and returns `{name: length}`.
3. **fasta_total(sequences)** takes the dictionary from `read_fasta` and returns the number of sequences.
4. **count_codons_by_header(sequences)** takes the dictionary from `read_fasta` and returns `{name: number of codons}` (length // 3).
5. **find_possible_orfs(sequences, min_len=30)** takes the dictionary from `read_fasta` and returns `{name: seq}` for sequences that are valid ORFs: at least `min_len` long, no `N`, start with ATG, length is a multiple of 3, and the only stop codon is at the end. It prints the reason for each rejected sequence.
6. **nucleotide_percentage(sequences)** takes a list of sequences (`seqs.values()`) and prints the percentage of A, T, G and C in each one.
7. **reverse_complement(sequences)** takes a list of sequences (`seqs.values()`), prints each sequence with its reverse complement, and returns a list of reverse complements.
 