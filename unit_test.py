def average(L):
    if not L:
        return None
    return sum(L) / len(L)


if __name__ == '__main__':
    L = [1, 2, 3, 4, 5]
    expected_result = 3.0
    result = average(L)

    if expected_result == result:
        print('Test Passed!')
    else:
        print('Test Failed!', 'Received :', result, 'Expected :', expected_result)
