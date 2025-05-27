def find_restriction_sites(dna_sequence, enzyme_sequence):
    # check the sequence
    def _check_sequence(seq):
        for base in seq:
            if base not in ['A', 'C', 'G', 'T']:
                return False
        return True
    if not _check_sequence(dna_sequence) or not _check_sequence(enzyme_sequence):
        raise ValueError("DNA sequence can only contain A, T, C, G")
    
# name the lists
    cut_sites = []
    dna_len = len(dna_sequence)
    enzyme_len = len(enzyme_sequence)
    
    # tranverse the sequence to find the site
    for i in range(dna_len - enzyme_len + 1):
        if dna_sequence[i:i+enzyme_len] == enzyme_sequence:
            cut_sites.append(i)
    
    return cut_sites

# example
try:
    dna = "ACGTGAAATTCGCTGAAATTCAGCT"
    enzyme = "GAAATTC"
    sites = find_restriction_sites(dna, enzyme)
    print(f"DNA sequence: {dna}")
    print(f"recognision site: {enzyme}")
    print(f"cutting site: {sites}")
# if error esists
except ValueError as e:
    print(f"there are errors in the DNA sequence: {e}")