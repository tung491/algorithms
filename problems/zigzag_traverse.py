def zigzag_traverse(matrix):
    height = len(matrix) - 1
    width = len(matrix[0]) - 1
    result = []
    row, col = 0, 0
    going_down = True
    while not is_out_of_bounds(row, col, height, width):
        result.append(matrix[row][col])
        if going_down:
            if col == 0 or row == height:
                going_down = False
                if row == height:
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1
        else:
            if row == 0 or col == width:
                going_down = True
                if col == width:
                    row += 1
                else:
                    col += 1
            else:
                row -= 1
                col += 1
    return result


def is_out_of_bounds(row, col, height, width):
    return row < 0 or row > height or col < 0 or col > width


def test():
    matrix = [[1, 3, 4, 10],
              [2, 5, 9, 11],
              [6, 8, 12, 15],
              [7, 13, 14, 16]]
    print(zigzag_traverse(matrix))


if __name__ == '__main__':
    test()