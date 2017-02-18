def read_file(filename):
    '''(str) -> (list)
    Return list from file.
    Reads a board from file.
    0 is for ' ' 1 is for  '*' 2 s for 'X'
    '''
    board = []
    count = []
    with open(filename, 'r') as file:
        for line in file:
            for i in line:
                if i == '*':
                    count.append(1)
                elif i == '\n':
                    continue
                elif i == 'X':
                    count.append(2)
                else:
                    count.append(0)
        for i in range(1, 11):
            for j in 'ABCDEFGHIJ':
                board.append([(j, i)])
        for i in range(0, len(count)):
            board[i].append(count[i])
    return(board)
print(read_file('field.txt'))
