def find_uniq(arr):

    for number in arr:
        if is_not_unique(number, arr):
            continue
        else:
            return number


def is_not_unique(number, array):
    count = 0
    for n in array:
        if number == n:
            count += 1
            if count > 1:
                return True
    return False
