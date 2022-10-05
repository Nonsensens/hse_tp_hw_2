def read_file(name_file):
    with open(name_file) as f:
        all_numbers_f = list(map(int, f.readline().split()))
    return all_numbers_f


def _min(numbers):
    min_n = numbers[0]
    for i in numbers:
        if i < min_n:
            min_n = i
    return min_n


def _max(numbers):
    max_n = numbers[0]
    for i in numbers:
        if i > max_n:
            max_n = i
    return max_n


def _sum(numbers):
    s = 0
    for i in numbers:
        s += i
    return s


def _mult(numbers):
    m = 1
    for i in numbers:
        m *= i
    return m


def file_is_empty(name_file):
    return len(read_file(name_file))


if __name__ == '__main__':
    name_f = input()
    f = read_file(name_f)
    print(_min(f), _max(f), _sum(f), _mult(f))

