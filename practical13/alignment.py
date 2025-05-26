from Bio import SeqIO
from Bio.Align import substitution_matrices
blosum62 = substitution_matrices.load("BLOSUM62")
import random
import os

# get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# transfer to  the right dir
os.chdir(script_dir)
#files are under the same dir
def read_fasta(file_path):
    """Read a FASTA file and return the sequence"""
    with open(file_path) as handle:
        return str(next(SeqIO.parse(handle, "fasta")).seq)

def generate_random_sequence(length):
    """Generate a random protein sequence of given length"""
    amino_acids = 'ACDEFGHIKLMNPQRSTVWY'
    return ''.join(random.choice(amino_acids) for _ in range(length))

def calculate_alignment(seq1, seq2):
    """Calculate alignment score and percent identity"""
    if len(seq1) != len(seq2):
        raise ValueError("Sequences must be equal length for non-gapped alignment")
    
    score = 0
    identical = 0
    
    for aa1, aa2 in zip(seq1, seq2):
        # Get substitution score (handle reverse order in matrix)
        pair = (aa1, aa2) if (aa1, aa2) in blosum62 else (aa2, aa1)
        score += blosum62.get(pair, -4)  # Default penalty for unlikely substitutions
        
        if aa1 == aa2:
            identical += 1
    
    percent_identity = (identical / len(seq1)) * 100
    return score, percent_identity

def main():
    # Load sequences 
    human_seq = read_fasta("human_sod2.fasta")
    mouse_seq = read_fasta("mouse_sod2.fasta")
    
    # Generate random sequence of same length
    random_seq = generate_random_sequence(len(human_seq))
    with open("random_seq.fasta", "w") as f:
        f.write(f">Random\n{random_seq}")
    
    # Perform comparisons
    print("Pairwise Sequence Comparisons:")
    print("-" * 50)
    
    # Human vs Mouse
    score_hm, identity_hm = calculate_alignment(human_seq, mouse_seq)
    print(f"Human vs Mouse\nScore: {score_hm}\nIdentity: {identity_hm:.2f}%\n")
    
    # Human vs Random
    score_hr, identity_hr = calculate_alignment(human_seq, random_seq)
    print(f"Human vs Random\nScore: {score_hr}\nIdentity: {identity_hr:.2f}%\n")
    
    # Mouse vs Random
    score_mr, identity_mr = calculate_alignment(mouse_seq, random_seq)
    print(f"Mouse vs Random\nScore: {score_mr}\nIdentity: {identity_mr:.2f}%")

if __name__ == "__main__":
    main()