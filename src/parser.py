import argparse

def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str,  default="localhost", help="Enter the host as string")
    parser.add_argument("--ports", type=str,  default="", help="Enter the ports separated by coma or space")
    parser.add_argument("--range", type=str,  default="", help="Enter a port range separated by '-'")
    parser.add_argument("--timeout", type=float,  default=1.0, help="Seconds to wait before timeout")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose mode")
    parser.add_argument("--output", type=str,  default="Console", help="Console or file path")

    return parser.parse_args()

def get_ports(ports: str) -> list[int]:
    result = []

    for port in ports.replace(",", " ").split():
        if not port.isdigit():
            raise ValueError(f"Invalid port: {port}")

        port_number = int(port)

        if port_number < 1 or port_number > 65535:
            raise ValueError("Port must be between 1 and 65535")

        result.append(port_number)

    return result

def get_range(ports_range: str) -> tuple:
    range_start = None
    range_end = None
    splits: list[str] = ports_range.split("-", 1)

    if splits[0].isnumeric():
        range_start = int(splits[0])
    else:
        raise TypeError("Range start needs int, got string")

    if splits[1].isnumeric():
        range_end = int(splits[1])
    else:
        raise TypeError("Range end needs int, got string")

    if range_start > range_end:
        raise ValueError("Range start cannot be greater than range end")

    return (range_start, range_end)