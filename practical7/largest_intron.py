import re
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA' 
y = re.findall(r'GT.+AG',seq)
for i in y:
    print(len(i))