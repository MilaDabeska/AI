def convert(matr, n):
    result = [[count(matr, i, j, n) for j in range(n)] for i in range(0, n)]
    printp = "\n".join(["   ".join(map(str, x)) for x in result])
    return printp


def count(matrix, i, j, n):
    counter = 0
    if matrix[i][j] == "#": return "#"
    if i > 0 and matrix[i - 1][j] == "#": counter += 1
    if i > 0 and j > 0 and matrix[i - 1][j - 1] == "#": counter += 1
    if i < n - 1 and matrix[i + 1][j] == "#": counter += 1
    if i < n - 1 and j < n - 1 and matrix[i + 1][j + 1] == "#": counter += 1
    if j > 0 and matrix[i][j - 1] == "#": counter += 1
    if j < n - 1 and matrix[i][j + 1] == "#": counter += 1
    if i > 0 and j < n - 1 and matrix[i - 1][j + 1] == "#": counter += 1
    if i < n - 1 and j > 0 and matrix[i + 1][j - 1] == "#": counter += 1
    return counter


if __name__ == '__main__':
    number = int(input())

    m = []
    for i in range(0, number):
        matrix2 = [elem for elem in input().split("   ")]
        m.append(matrix2)

    print(convert(m, number))
