import sys

sys.path.append('C:\\Users\\marth\\PycharmProjects\\Battelship')

from field.read_file import read_file

def ship_size(position):
    '''(list, tuple) -> (tuple)
    Returns a length of ship
    '''
    board = read_file('field.txt')
    abc = 'ABCDEFGHIJ'
    ck = abc.index(position[0])
    count1 = 1
    count2 = 1
    count3 = 1
    count4 = 1
    check = has_ship(position)
    if check == 'False':
        print('There is no ship!')
    elif check == 'True':
        for i in board:
            if ck == 9:
                if (position[0], position[-1] + 1) in i:
                    if 1 in i:
                        count1 += 1
                    elif 2 in i:
                        count1 += 1
                    elif 0 in i:
                        continue
                elif (position[0], position[-1] - 1) in i:
                    if 1 in i:
                        count2 += 1
                    elif 2 in i:
                        count2 += 1
                    elif 0 in i:
                        continue
                elif (abc[ck - 1], position[-1]) in i:
                    if 1 in i:
                        count4 += 1
                    elif 2 in i:
                        count4 += 1
                    elif 0 in i:
                        continue
            elif ck == 0:
                if (position[0], position[-1] + 1) in i:
                    if 1 in i:
                        count1 += 1
                    elif 2 in i:
                        count1 += 1
                    elif 0 in i:
                        continue
                elif (position[0], position[-1] - 1) in i:
                    if 1 in i:
                        count2 += 1
                    elif 2 in i:
                        count2 += 1
                    elif 0 in i:
                        continue
                elif (abc[ck + 1], position[-1]) in i:
                    if 1 in i:
                        count3 += 1
                    elif 2 in i:
                        count3 += 1
                    elif 0 in i:
                        continue
            elif position[-1] == 10:
                if (position[0], position[-1] - 1) in i:
                    if 1 in i:
                        count2 += 1
                    elif 2 in i:
                        count2 += 1
                    elif 0 in i:
                        continue
                elif (abc[ck + 1], position[-1]) in i:
                    if 1 in i:
                        count3 += 1
                    elif 2 in i:
                        count3 += 1
                    elif 0 in i:
                        continue
                elif (abc[ck - 1], position[-1]) in i:
                    if 1 in i:
                        count4 += 1
                    elif 2 in i:
                        count4 += 1
                    elif 0 in i:
                        continue
            elif position[-1] == 0:
                if (position[0], position[-1] + 1) in i:
                    if 1 in i:
                        count1 += 1
                    elif 2 in i:
                        count1 += 1
                    elif 0 in i:
                        continue
                elif (abc[ck + 1], position[-1]) in i:
                    if 1 in i:
                        count3 += 1
                    elif 2 in i:
                        count3 += 1
                    elif 0 in i:
                        continue
                elif (abc[ck - 1], position[-1]) in i:
                    if 1 in i:
                        count4 += 1
                    elif 2 in i:
                        count4 += 1
                    elif 0 in i:
                        continue
            else:
                if (position[0], position[-1] + 1) in i:
                    if 1 in i:
                        count1 += 1
                    elif 2 in i:
                        count1 += 1
                    elif 0 in i:
                        continue
                elif (position[0], position[-1] - 1) in i:
                    if 1 in i:
                        count2 += 1
                    elif 2 in i:
                        count2 += 1
                    elif 0 in i:
                        continue
                elif (abc[ck + 1], position[-1]) in i:
                    if 1 in i:
                        count3 += 1
                    elif 2 in i:
                        count3 += 1
                    elif 0 in i:
                        continue
                elif (abc[ck - 1], position[-1]) in i:
                    if 1 in i:
                        count4 += 1
                    elif 2 in i:
                        count4 += 1
                    elif 0 in i:
                        continue
        if count1 == max(count1, count2, count3, count4):
            for i in board:
                if position[-1] == 10 or position[-1] == 9:
                    continue
                elif position[-1] == 8:
                    if (position[0], position[-1] + 2) in i:
                        if 1 in i:
                            count1 += 1
                        elif 2 in i:
                            count1 += 1
                        elif 0 in i:
                            break
                else:
                    if (position[0], position[-1] + 2) in i:
                        if 1 in i:
                            count1 += 1
                        elif 2 in i:
                            count1 += 1
                        elif 0 in i:
                            break
                    if (position[0], position[-1] + 3) in i:
                        if 1 in i:
                            count1 += 1
                        elif 2 in i:
                            count1 += 1
                        elif 0 in i:
                            break
        if count2 == max(count1, count2, count3, count4):
            for i in board:
                if position[-1] == 0 or position[-1] == 1:
                    continue
                elif position[-1] == 2:
                    if (position[0], position[-1] - 2) in i:
                        if 1 in i:
                            count2 += 1
                        elif 2 in i:
                            count2 += 1
                        elif 0 in i:
                            break
                else:
                    if (position[0], position[-1] - 2) in i:
                        if 1 in i:
                            count2 += 1
                        elif 2 in i:
                            count2 += 1
                        elif 0 in i:
                            break
                    if (position[0], position[-1] - 3) in i:
                        if 1 in i:
                            count2 += 1
                        elif 2 in i:
                            count2 += 1
                        elif 0 in i:
                            break
        if count3 == max(count1, count2, count3, count4):
            for i in board:
                if ck == 9 or ck == 8:
                    continue
                elif ck == 7:
                    if (abc[ck + 2], position[-1]) in i:
                        if 1 in i:
                            count3 += 1
                        elif 2 in i:
                            count3 += 1
                        elif 0 in i:
                            break
                else:
                    if (abc[ck + 2], position[-1]) in i:
                        if 1 in i:
                            count3 += 1
                        elif 2 in i:
                            count3 += 1
                        elif 0 in i:
                            break
                    if (abc[ck + 3], position[-1]) in i:
                        if 1 in i:
                            count3 += 1
                        elif 2 in i:
                            count3 += 1
                        elif 0 in i:
                            break
        if count4 == max(count1, count2, count3, count4):
            for i in board:
                if ck == 0 or ck == 1:
                    continue
                else:
                    if (abc[ck - 2], position[-1]) in i:
                        if 1 in i:
                            count4 += 1
                        elif 2 in i:
                            count4 += 1
                        elif 0 in i:
                            break
                    if (abc[ck - 3], position[-1]) in i:
                        if 1 in i:
                            count4 += 1
                        elif 2 in i:
                            count4 += 1
                        elif 0 in i:
                            break
    return max(count1, count2, count3, count4)
print(ship_size(('H', 8)))
