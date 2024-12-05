from typing import Iterator, TypeAlias

Report: TypeAlias = list[int]


def read_file(path: str = "input.txt") -> Iterator[Report]:
    with open(path) as file:
        yield from [[int(x) for x in line.split(" ")] for line in file.readlines()]


def detect_safety(report: Report) -> bool:
    trend = (report[0] - report[1]) > 0
    for i in range(len(report) - 1):
        if not (0 < abs(diff := report[i] - report[i + 1]) < 4) or (diff > 0) != trend:
            return False
    return True


def main(path: str):
    safety_reports = sum([detect_safety(report) for report in read_file(path)])
    print(f"Safety reports count: {safety_reports}")


if __name__ == "__main__":
    main("input.txt")
