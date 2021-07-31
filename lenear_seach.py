def linear_search(L, x):  # l is a list, x in en what we ar looking for
    n = len(L)  # n is number of element in the list
    for i in range(n):  # i is 0
        if L[i] == x:  # if x found in L
            return i # return the index

    return None  # return NOne in not found


if __name__ == '__main__':
    L = [1, 5, 52, 66, 9, 99]
    x = 66
    expected_result = 3
    result = linear_search(L, x)

    if expected_result == result:
        print('Test Passed !!')
    else:
        print('Test Failed !!')


'''n = len(L)
    i = 0

    while i < n:
        if L[i] == x:
            return i
        i = i + 1
    i = i - 1
    return i
'''