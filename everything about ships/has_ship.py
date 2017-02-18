import sys

sys.path.append('C:\\Users\\marth\\PycharmProjects\\Battelship')

from field.read_file import read_file


def has_ship(position):
    '''(list, tuple) -> (bool)
    Returns True, if ship is in that position.
    If there is no ship, returns False.
    0 is for ' ' 1 is for  '*' 2 s for 'X'
    '''
    board = read_file('field.txt')
    for i in board:
        if position in i:
            if i[-1] == 0:
                return('False')
            elif i[-1] == 1:
                return('True')
            elif i[-1] == 2:
                return('True')
        else:
            continue
print(has_ship(('H', 8)))