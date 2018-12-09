def order_weight(strng):
    string_sorted_weights = sorted(strng.split())
    int_sorted_weights = list(map(int, string_sorted_weights))

    new_sorted_weights = sorted(int_sorted_weights, key=calculate_weight)

    return ' '.join(list(map(str, new_sorted_weights)))


def calculate_weight(number):
    divisors = sorted([1*10**i for i in range(0, 20)], reverse=True)

    result = 0
    for divisor in divisors:
        quotient = divmod(number, divisor)[0]
        result += quotient
        number -= divisor * quotient

    return result
