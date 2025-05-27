import re
# path
INPUT_FASTA = r"C:\IBI\IBI1_2024-25\practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
OUTPUT_FILE = r"C:\IBI\IBI1_2024-25\practical7\tata_genes.fa"

def read_fasta(file_path):
    gene_dict = {}
    current_header = None
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            # conduct a new gene and get the name of the gene
            if line.startswith('>'): #get the starting point
                current_header = line[1:].split()[0]
                gene_dict[current_header] = ""
            elif current_header:
                gene_dict[current_header] += line
    return gene_dict
#check if the gene contains TATA box
def has_tata_box(seq):
    pattern = r'TATA[AT][AT]'
    return bool(re.search(pattern, seq))

def main():
    try:
        print(f"reading {INPUT_FASTA}...")
        gene_sequences = read_fasta(INPUT_FASTA)
        print(f"there are {len(gene_sequences)} gene sequences in the file")

        tata_genes = {name: seq for name, seq in gene_sequences.items() 
                     if has_tata_box(seq)} #dictionary with the imformation for TATA gene

        with open(OUTPUT_FILE, 'w') as f:
            for gene_name, sequence in tata_genes.items():# write the imformation into the file
                f.write(f">{gene_name}\n{sequence}\n")
        #print the results
        print(f"there are {len(tata_genes)} genes containing TATA box")
        print(f"the results is at {OUTPUT_FILE}")
    #errors    
    except FileNotFoundError:
        print(f"error: {INPUT_FASTA} cannot be found, please check the path")
    except Exception as e:
        print(f"error: {e}")

if __name__ == "__main__":
    main()