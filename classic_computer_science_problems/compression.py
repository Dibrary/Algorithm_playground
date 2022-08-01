
class CompressedGene:
    def __init__(self, gene):
        self._compress(gene)

    def _compress(self, gene):
        self.bit_string = 1
        for nucleotide in gene.upper():
            self.bit_string <<= 2 # 왼쪽으로 2바이트 시프트

            if nucleotide == "A":
                self.bit_string |= 0b00 # 왼쪽으로 밀고 비트를 추가한다.
            elif nucleotide == "C":
                self.bit_string += 0b01
            elif nucleotide == "G":
                self.bit_string |= 0b10
            elif nucleotide == "T":
                self.bit_string |= 0b11
            else:
                raise ValueError("유효하지 않은 뉴클레오티드 입니다:{}".format(nucleotide))
            # 단순히 0b꼴의 int로만 바꿔도 sys.getsizeof값이 작아진다. (압축이 된다)


    def decompress(self):
        gene = ""
        for i in range(0, self.bit_string.bit_length() -1, 2):
            bits = self.bit_string >> i & 0b11
            if bits == 0b00:
                gene += "A"
            elif bits == 0b01:
                gene += "C"
            elif bits == 0b10:
                gene += "G"
            elif bits == 0b11:
                gene += "T"
            else:
                raise ValueError("Invalid bits:{}".format(bits))
        return gene[::-1]

    def __str__(self):
        return self.decompress()

if __name__=="__main__":
    from sys import getsizeof
    original = "TAGGGATTAACCGTTATATATATATATATGCCATGGATCGTTATATAGGGATTAA"
    print("원본 {} 바이트".format(getsizeof(original)))
    compressed = CompressedGene(original)
    print("압축 {} 바이트".format(getsizeof(compressed.bit_string)))
    print(compressed)
    print("원본 문자열과 압축 해제한 문자열은 같나요? {}".format(original == compressed.decompress()))