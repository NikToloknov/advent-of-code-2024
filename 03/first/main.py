import re


def read_file(path: str = "input.txt") -> str:
    with open(path) as file:
        return file.read()


def mul(dump: str) -> int:
    return sum(int(x) * int(y) for x, y in re.findall(r"mul\((\d+),(\d+)\)", dump))


def main(path: str):
    dump = read_file(path)
    print(mul(dump))


if __name__ == "__main__":
    main("input.txt")
