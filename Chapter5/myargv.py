import sys


def add(*args):
    result = 0
    lists = args[0]
    for i in lists:
        result += int(i)
    return result


if __name__ == '__main__':
    data = sys.argv[1:]
    print(data)
    print(add(data))
