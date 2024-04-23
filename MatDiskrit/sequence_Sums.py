def calculate_value(fij, i, j):
    if i == j:
        return fij[i][j] ** 2
    else:
        if i + j in fij[j]:
            return 9 * fij[j][i + j]
        else:
            return 0

def calculate_sum(fij):
    n = len(fij)
    total = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            total += calculate_value(fij, i, j)
    return total

def main():
    # Example usage:
    fij = {
        i: {j: (i + j) for j in range(1, 10)} for i in range(1, 10)
    }
    print(calculate_sum(fij))

if __name__ == "__main__":
    main()