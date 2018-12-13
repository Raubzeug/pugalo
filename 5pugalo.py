#!/usr/bin/env python3

def get_data(filename):
    numbers = []
    try:
        with open(filename) as fh:
            for i in fh:
                line=i.split(' ')
                numbers.append(line)
            return numbers
    except EnvironmentError as err:
        print(err)

class MyException(Exception):
    pass

def pugalo(list_to_sort, razmah):

    count = 0
    M = {}

    for i in range(len(list_to_sort)):
        if M.get(list_to_sort[i]):
            M[list_to_sort[i]].append(i)
        else:
            M.setdefault(list_to_sort[i], [i])

    for i in sorted(M):
        for j in M[i]:
            for m in range(len(M[i])): #check the option like 1 3 1 1 4 5. If we swap values 0 and 3, we'll get sorted list.
                if (j - count - m) == 0 or (j - count - m) % razmah == 0:
                    count += 1
                    break
            else:
                raise MyException

    return 'YES'

def main():
    numbers = get_data('input.txt')
    matreshki = list(map(int, numbers[1]))
    data2 = list(map(int, numbers[0]))
    razmah = data2[1]
    assert data2[0] == len(matreshki), 'Invalid data: massive length does not match data in input'

    if razmah == 1:
        finish = 'YES'
    else:
        try:
            finish = pugalo(matreshki, razmah)
        except MyException:
            finish = 'NO'

    fh = None
    try:
        with open('output.txt', 'w') as fh:
            fh.write(finish)
    except EnvironmentError as err:
        print(err)

main()
