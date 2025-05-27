import re
import os

# Set the path to the input FASTA file
INPUT_FASTA = r"C:\IBI\IBI1_2024-25\practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"

def read_fasta(file_path):
    """Read a FASTA file and return a dictionary of gene sequences"""
    genes = {}
    current_name = ''
    
    try:
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith('>'):
                    # If line starts with '>', it's a new gene
                    # Extract the gene name and initialize sequence storage
                    current_name = line[1:].split()[0]
                    genes[current_name] = ""
                elif current_name:
                    # Append sequence lines to the current gene
                    genes[current_name] += line
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        return {}
    
    return genes

def count_tata(seq):
    """Count the occurrences of the TATA[AT][AT] motif"""
    # find all matches of TATA
    return len(re.findall(r'TATA[AT][AT]', seq))

def main():
    # Check if the input file exists
    if not os.path.exists(INPUT_FASTA):
        print(f"Error: {INPUT_FASTA} does not exist")
        return
    
    # Read all gene sequences from the FASTA file
    genes = read_fasta(INPUT_FASTA)
    if not genes:
        return
    
    # Define acceptable splice patterns
    splice_patterns = ["GTAG", "GCAG", "ATAC"]
    
    # Ask the user to input a splice pattern
    splice = input(f"Enter a splice pattern ({'/'.join(splice_patterns)}): ").strip().upper()
    if splice not in splice_patterns:
        print(f"Error: Invalid pattern. Please use {', '.join(splice_patterns)}")
        return

    # Set output directory
    output_dir = r"C:\IBI\IBI1_2024-25\practical7"
    output_file = os.path.join(output_dir, f"{splice}_spliced_genes.fa")
    filtered = {}

    # For each gene, check if it contains the splice site and at least one TATA box
    for name, seq in genes.items():
        if splice in seq and count_tata(seq) > 0:
            filtered[name] = count_tata(seq)
    
    with open(output_file, 'w') as f:
        for name, tata_count in filtered.items():
            f.write(f">{name}|TATA:{tata_count}\n{genes[name]}\n")
    
    # Report how many genes were found and where results were saved
    print(f"Found {len(filtered)} genes matching the criteria. Results saved to {output_file}")

if __name__ == "__main__":
    main()
