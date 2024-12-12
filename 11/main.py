import math
from functools import cache


def read_file(path: str) -> tuple[int, ...]:
    with open(path) as file:
        return tuple(int(num) for num in file.read().split(" "))


@cache
def operation(stone: int) -> tuple[int, ...]:
    if stone == 0:
        return (1,)
    if (digits := int(math.log10(stone)) + 1) % 2 == 0:
        return divmod(stone, 10 ** (digits // 2))
    return (stone * 2024,)


@cache
def calc_stones_count(stone: int, blinks: int) -> int:
    if blinks == 0:
        return 1

    return sum(
        calc_stones_count(new_stone, blinks - 1) for new_stone in operation(stone)
    )


def main(path: str, blinks: int):
    stones = sum(calc_stones_count(stone, blinks) for stone in read_file(path))
    print(f"Count of stones: {stones}")


if __name__ == "__main__":
    main("input.txt", 75)
