import math
from dataclasses import dataclass
from typing import Iterator, Optional


@dataclass
class Node:
    value: int
    level: int
    left: Optional["Node"] = None
    middle: Optional["Node"] = None
    right: Optional["Node"] = None


@dataclass
class Tree:
    root: Node


@dataclass
class Values:
    value: int
    numbers: tuple[int, ...]

    @classmethod
    def create(cls, data: str) -> "Values":
        value, *numbers = data.split(" ")
        return cls(
            value=int(value.replace(":", "")),
            numbers=tuple(int(number) for number in numbers),
        )

    def __repr__(self):
        return f"{self.value}: {' '.join(map(lambda x: str(x), self.numbers))}"


def read_file(path: str) -> Iterator[Values]:
    with open(path) as file:
        yield from [Values.create(line) for line in file.readlines()]


def concat(a: int, b: int) -> int:
    return int(10 ** (int(math.log(b, 10)) + 1) * a + b)


def validate_calibration(values: Values) -> bool:
    stack: list[Node] = [Node(value=values.numbers[0], level=0)]

    while len(stack) > 0:
        if (node := stack.pop()).value == values.value:
            return True

        if (level := node.level + 1) == len(values.numbers):
            continue

        number = values.numbers[level]

        if (value := node.value * number) <= values.value:
            node.right = Node(value=value, level=level)
            stack.append(node.right)

        if (value := node.value + number) <= values.value:
            node.left = Node(value=value, level=level)
            stack.append(node.left)

        if (value := concat(node.value, number)) <= values.value:
            node.middle = Node(value=value, level=level)
            stack.append(node.middle)

    return False


def main(path: str):
    total = sum(
        values.value for values in read_file(path) if validate_calibration(values)
    )
    print("Total valid probes:", total)


if __name__ == "__main__":
    main("input.txt")
