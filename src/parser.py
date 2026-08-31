import argparse

def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str,  default="localhost", help="Enter the host as string")
    parser.add_argument("--ports", type=str,  default="0", help="Enter the ports separated by coma or space")
    parser.add_argument("--range", type=str,  default="0-0", help="Enter a port range separated by '-'")
    parser.add_argument("--timeout", type=float,  default=1.0, help="Seconds to wait before timeout")
    parser.add_argument("--verbose", type=bool, default=False, help="Enable verbose mode")

    return parser.parse_args()

def get_ports(ports: str) -> list[int]:
    result: list[int] = []

    current = 0
    for letter in ports:
        if letter == "," or letter == " ":
            if current != 0:
                result.append(current)

            current = 0
            continue

        if letter.isnumeric():
            current = current * 10 + int(letter)

    if current != 0:
        result.append(current)

    return result

def get_range(ports_range: str) -> tuple:
    range_start = 0
    range_end = 0
    splits: list[str] = ports_range.split("-", 1)

    if splits[0].isnumeric():
        range_start = int(splits[0])
    else:
        raise TypeError("Range start needs int, got string")

    if splits[1].isnumeric():
        range_end = int(splits[1])
    else:
        raise TypeError("Range end needs int, got string")

    return (range_start, range_end)