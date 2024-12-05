from heapq import heappop, heappush

from typing import Iterator
from collections import defaultdict


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


def get_similarity_score(pairs: dict[int, list[int]]) -> int:
    return sum(left * right for _, (left, right) in pairs.items())


def main(path: str):
    lheap: list[int] = []
    rheap: list[int] = []
    score: dict[int, list[int]] = defaultdict(lambda: [0, 0])

    for left, right in read_file(path):
        score[left][0] += 1
        score[right][1] += right

        heappush(lheap, left)
        heappush(rheap, right)

    distance = find_distance(lheap, rheap)
    similarity = get_similarity_score(score)
    print(f"Distance: {distance}, Similarity score: {similarity}")


if __name__ == "__main__":
    main("input.txt")
