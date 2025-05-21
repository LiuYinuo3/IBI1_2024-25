import matplotlib.pyplot as plt

#mRNA_sequence = input("Enter the mRNA sequence: ")
mRNA_sequence = "AUUCUGCCCUCGAGCCCACCGGGAACGAAAGAGAAGCUCUAUCUCCCCUCCAGGAGCCCAGCUAUGAACUCCUUCUCCACAAGCGCCUUCGGUCCAGUUGCCUUCUCCCUGGGGCUGCUCCUGGUGUUGCCUGCUGCCUUCCCUGCCCCAGUACCCCCAGGAGAAGAUUCCAAAGAUGUAGCCGCCCCACACAGACAGCCACUCACCUCUUCAGAACGAAUUGACAAACAAAUUCGGUACAUCCUCGACGGCAUCUCAGCCCUGAGAAAGGAGACAUGUAACAAGAGUAACAUGUGUGAAAGCAGCAAAGAGGCACUGGCAGAAAACAACCUGAACCUUCCAAAGAUGGCUGAAAAAGAUGGAUGCUUCCAAUCUGGAUUCAAUGAGGAGACUUGCCUGGUGAAAAUCAUCACUGGUCUUUUGGAGUUUGAGGUAUACCUAGAGUACCUCCAGAACAGAUUUGAGAGUAGUGAGGAACAAGCCAGAGCUGUGCAGAUGAGUACAAAAGUCCUGAUCCAGUUCCUGCAGAAAAAGGCAAAGAAUCUAGAUGCAAUAACCACCCCUGACCCAACCACAAAUGCCAGCCUGCUGACGAAGCUGCAGGCACAGAACCAGUGGCUGCAGGACAUGACAACUCAUCUCAUUCUGCGCAGCUUUAAGGAGUUCCUGCAGUCCAGCCUGAGGGCUCUUCGGCAAAUGUAGCAUGGGCACCUCAGAUUGUUGUUGUUAAUGGGCAUUCCUUCUUCUGGUCAGAAACCUGUCCACUGGGCACAGAACUUAUGUUGUUCUCUAUGGAGAACUAAAAGUAUGAGCGUUAGGACACUAUUUUAAUUAUUUUUAAUUUAUUAAUAUUUAAAUAUGUGAAGCUGAGUUAAUUUAUGUAAGUCAUAUUUAUAUUUUUAAGAAGUACCACUUGAAACAUUUUAUGUAUUAGUUUUGAAAUAAUAAUGGAAAGUGGCUAUGCAGUUUGAAUAUCCUUUGUUUCAGAGCCAGAUCAUUUCUUGGAAAGUGUAGGCUUACCUCAAAUAAAUGGCUAACUUAUACAUAUUUUUAAAGAAAUAUUUAUAUUGUAUUUAUAUAAUGUAUAAAUGGUUUUUAUACCAAUAAAUGGCAUUUUAAAAAAUUCA"
# 定义密码子表
codon_table = {
        'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu',
        'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
        'UAU': 'Tyr', 'UAC': 'Tyr', 'UAA': 'Stop', 'UAG': 'Stop',
        'UGU': 'Cys', 'UGC': 'Cys', 'UGA': 'Stop', 'UGG': 'Trp',
        'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
        'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
        'CAU': 'His', 'CAC': 'His', 'CAA': 'Gln', 'CAG': 'Gln',
        'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
        'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile', 'AUG': 'Met',
        'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
        'AAU': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys',
        'AGU': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg',
        'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
        'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
        'GAU': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu',
        'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly'
    }  


# 找到起始密码子
# 定义起始密码子，通常是AUG
start_codon = "AUG"
# 在mRNA序列中查找起始密码子
# find()方法返回子字符串的最低索引，如果没有找到，则返回-1
start_index = mRNA_sequence.find(start_codon)
# 如果不等于-1，表示找到了起始密码子
if start_index != -1:
    print(f"The start codon is at position {start_index + 1} and ends at position {start_index + 3}")
    start = True
else:
    print("Start codon not found")
    start = False

# 找到终止密码子
stop_codons = ["UAA", "UAG", "UGA"]
# 从起始密码子后开始查找
# 创建一个列表来存储终止密码子的位置，便于后续挑选最大值
stop_order = []
# 初始化终止密码子的位置
stop_index = -1
# 从起始密码子后开始查找终止密码子, 确保以3的倍数为单位
for j in range(start_index + 3, len(mRNA_sequence) - 2, 3):
    codon = mRNA_sequence[j:j+3]
    if codon in stop_codons:
        stop_index = j
        break
if stop_index != -1:
    print(f"The stop codon is at position {stop_index + 1} and ends at position {stop_index + 3}")
    stop = True
else:
    print("Stop codon not found")
    stop = False


# 切割出mRNA完整地编码序列
if start and stop:
    # 切割出mRNA完整地编码序列
    coding_sequence = mRNA_sequence[start_index:stop_index + 3]
    print(f"The coding sequence is {coding_sequence}")
else:
    print("The coding sequence is not found")

# 切割密码子并存储
# 将mRNA序列切割成密码子
codons = [coding_sequence[i:i + 3] for i in range(0, len(coding_sequence), 3)]


def most_common_codon(codons):
    # count the frequency of codons
    codon_counts = {}
    for codon in codons:
        codon_counts[codon] = codon_counts.get(codon, 0) + 1
    
    # find the most frequent codon（may be more than 1）
    max_count = max(codon_counts.values())
    most_common = [c for c, cnt in codon_counts.items() if cnt == max_count]

    # print the result
    if len(most_common) > 1:
        print(f"The most common codons are {', '.join(most_common)} and they appear {max_count} times")
    else:
        print(f"The most common codon is {most_common[0]} and it appears {max_count} times")
    
    return most_common  


def most_common_amino_acid(codons):
    """统计并返回出现频率最高的氨基酸"""
    # 先找出最常见的密码子
    common_codons = most_common_codon(codons)
    
    # 获取对应的氨基酸
    amino_acids = [codon_table.get(codon, 'Unknown') for codon in common_codons]
    
    # 打印结果
    if len(amino_acids) > 1:
        print(f"The most common amino acids are {', '.join(amino_acids)}")
    else:
        print(f"The most common amino acid is {amino_acids[0]}")
    
    return amino_acids
        

def amino_acid_frequency(codons):
    # 绘制氨基酸频率图
    # 计算氨基酸频率
    amino_acid_frequency = {}
    for codon in codons:
        if codon not in stop_codons:
            # 找到密码子对应的氨基酸
            amino_acid = codon_table[codon]
            if amino_acid not in amino_acid_frequency:
                amino_acid_frequency[amino_acid] = 1
            else:
                amino_acid_frequency[amino_acid] += 1
    # 计算频率
    for amino_acid in amino_acid_frequency:
        amino_acid_frequency[amino_acid] = amino_acid_frequency[amino_acid] / (len(codons) - 1)
    # 对字典进行排序
    amino_acid_frequency = dict(sorted(amino_acid_frequency.items(), key=lambda item: item[1], reverse=True))
    # 绘制密码子饼状图
    plt.figure(figsize=(10, 10))
    wedges, _ = plt.pie(amino_acid_frequency.values(), labels=None, radius=0.9, colors = plt.cm.tab20.colors + plt.cm.tab20b.colors + plt.cm.tab20c.colors)
    # 添加图例
    plt.legend(
        wedges,

        [f"{codon} {freq*100:.2f}%" for codon, freq in amino_acid_frequency.items()],
        title="Codons",
        loc="center left", 
        bbox_to_anchor = (1, 0, 0.5, 1),  # 将图例放置在饼图右侧
        ncol=3
    )
    plt.tight_layout()
    plt.title("Amino Acid Frequency", fontweight='bold', fontsize=20, pad = 0)
    plt.show()

def degeneracy(codons):
    # 第四个任务，找到编码同一氨基酸的不同密码子，并绘制频率图
    # 创建一个字典用来存储氨基酸
    amino_acids = {}
    for codon in codons:

        # 找到密码子对应的氨基酸
        amino_acid = codon_table[codon]
        if amino_acid not in amino_acids:
            amino_acids[amino_acid] = [codon]
        else:
            amino_acids[amino_acid].append(codon)
    cols = 4
    raws = len(amino_acids) // cols + 1 
    # 确定图表的大小
    plt.figure(figsize=(10, 3.5 * raws))
    # 找到每种氨基酸对应的出现频率最高的密码子
    i = 0
    for amino_acid, codon_list in amino_acids.items():
        # 计算密码子出现的次数
        codon_counts = {}
        for codon in codon_list:
            if codon in codon_counts:
                codon_counts[codon] += 1
            else:
                codon_counts[codon] = 1
        i += 1
        # 找到密码子出现的频率
        codon_frequency = {}
        for codon in codon_counts:
            codon_frequency[codon] = codon_counts[codon] / len(codons)
        codon_frequency = dict(sorted(codon_frequency.items(), key=lambda item: item[1], reverse=True))
        # 创建子图
        plt.subplot(raws, cols, i)
        wedges, *_ = plt.pie(codon_frequency.values(), labels = None, colors = plt.cm.tab20.colors, radius = 0.9)
        plt.legend(
            wedges,
            [f"{codon} {freq*100:.2f}%" for codon, freq in codon_frequency.items()],
            title = "Codon(s)",
            # loc=(1,0.001), 
            loc="upper left",  # 统一图例位置
            bbox_to_anchor=(1.05, 1),  # 统一锚点位置
            )
        plt.title(amino_acid, fontweight='bold')
        plt.axis('equal')

    plt.subplots_adjust(hspace=0.8, wspace=0.4)  # 先调整子图间距
    plt.tight_layout(pad=3.0, h_pad=2.5, w_pad=2.0)  # 再微调整体布局
    plt.show()


    
most_common_codon(codons)
most_common_amino_acid(codons)
amino_acid_frequency(codons) 
degeneracy(codons)