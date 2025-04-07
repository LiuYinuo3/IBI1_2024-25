import re
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA' 
y = re.findall(r'GT.+AG',seq)
print(len(y))