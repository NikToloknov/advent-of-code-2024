from dataclasses import dataclass
from typing import Iterator, Optional


@dataclass
class Node:
    value: int
    level: int
    left: Optional["Node"] = None
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


def validate_calibration(values: Values) -> bool:
    stack: list[Node] = [
        Node(
            value=values.numbers[0],
            level=0,
        ),
    ]

    while len(stack) > 0:
        node = stack.pop()

        if node.value == values.value:
            return True

        if node.level + 1 == len(values.numbers):
            continue

        if (value := node.value * values.numbers[node.level + 1]) <= values.value:
            node.right = Node(value=value, level=node.level + 1)
            stack.append(node.right)

        if (value := node.value + values.numbers[node.level + 1]) <= values.value:
            node.left = Node(value=value, level=node.level + 1)
            stack.append(node.left)

    return False


def main(path: str):
    total = sum(
        values.value for values in read_file(path) if validate_calibration(values)
    )
    print("Total valid probes:", total)


if __name__ == "__main__":
    main("input.txt")
