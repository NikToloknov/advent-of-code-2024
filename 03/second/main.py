import re


def read_file(path: str = "input.txt") -> str:
    with open(path) as file:
        return file.read()


def mul(dump: str) -> int:
    enabled = True
    sum: int = 0

    for x, y, action in re.findall(r"mul\((\d+),(\d+)\)|(do\(\)|don't\(\))", dump):
        if x and y and enabled:
            sum += int(x) * int(y)
        elif action:
            enabled = action == "do()"

    return sum


def main(path: str):
    dump = read_file(path)
    print(mul(dump))


if __name__ == "__main__":
    main("input.txt")
