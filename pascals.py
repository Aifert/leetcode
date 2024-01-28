# pascals triangle (easy)


def generate(numRows):
    result = [[1]]

    for i in range(numRows - 1):
        # building a temporary array so we don't modify the actual result
        temp = [0] + result[-1] + [0]
        row = []
        for j in range(len(result[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        result.append(row)

    return result
