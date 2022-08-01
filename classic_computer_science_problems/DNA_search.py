
from enum import IntEnum
from typing import Tuple, List

nucleotide = IntEnum('Nucleotide', ('A','C','G','T')) # A는 1, C는 2, G는 3, T는 4가 됨.
# for i in nucleotide:
#     print(i)

codon = Tuple[nucleotide, nucleotide, nucleotide] # 코돈은 세 개의 뉴클레오티드로 구성되고,
gene = List[codon] # 유전자는 다수의 코돈으로 구성된다.

gene_str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTTATATATACCCCTAGGACTCCCTTT"

def string_to_gene(s):
    gene = []
    for i in range(0, len(s), 3):
        if (i+2) >= len(s): # 다음에 문자 2개가 있을 경우에 실행함.
            return gene
        codon = (nucleotide[s[i]], nucleotide[s[i+1]], nucleotide[s[i+2]]) # 코돈 초기화
        gene.append(codon) # 3개씩 잘린 코돈이 gene에 추가된다.
    return gene

my_gene = string_to_gene(gene_str)

for k in my_gene:
    print(k)



