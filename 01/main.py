from heapq import heappop, heappush

from typing import Iterator
from collections import Counter


def read_file(path: str = "input.txt") -> Iterator[tuple[int, int]]:
    with open(path) as file:
        for line in file.readlines():
            left, right = line.split("   ")
            yield int(left), int(right)


def find_distance(left: list[int], right: list[int]) -> int:
    distance: int = 0

    while left and right:
        distance += abs(heappop(left) - heappop(right))

    return distance


def main(path: str):
    lheap: list[int] = []
    rheap: list[int] = []

    for left, right in read_file(path):
        heappush(lheap, left)
        heappush(rheap, right)

    distance = find_distance(lheap, rheap)
    print(f"Distance: {distance}")


if __name__ == "__main__":
    main("input.txt")
