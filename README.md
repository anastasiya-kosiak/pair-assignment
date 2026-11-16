Hi! The team for this assignment is Olha, Yelyzaveta, and Anastasiia.
test commit
test commit 2
test

Liza's functions:
1. read_fasta (path) writes all sequances into the dictionary {name:seq}.
    key = name is the header of sequance 
    value = seq (assigned variable) is the sequance 
    returns the dictiomnary "sequance"
    "sequances" can be reused in other functions

    path - the path to sequance file

2. seq_length (path) writes the dictionary with the lenghes of sequances {name: length}.
    it uses "sequances" dictionary from read_fasta
    returns the dictionary "length"

3. total_fasta (path) returns the number of sequances in the file.
    also uses "sequances" dictionary from read_fasta