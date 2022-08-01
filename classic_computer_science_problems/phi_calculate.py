
def calculate_pi(n_terms):
    numerator = 4.0
    denominator = 1.0
    operation = 1.0
    pi = 0.0

    for _ in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0

    return pi

if __name__=="__main__":
    print(calculate_pi(1000000)) # 숫자가 더 커질수록 계속 정확해진다.


