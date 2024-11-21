def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        num = True
        for i in range(2, result // 2 + 1):
            if result % i == 0:
                num = False
        if num:
            print('Простое')
        else:
            print('Составное')
        return result

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)

