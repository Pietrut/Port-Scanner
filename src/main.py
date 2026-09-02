import socket
import parser
from output import output

def check_port(host: str, port: int, timeout: float) -> str:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    try:
        sock.connect((host, port))
        return "Open"
    except ConnectionRefusedError:
        return "Closed"
    except TimeoutError:
        return "Timeout"
    finally:
        sock.close()

def main() -> None:
    ports: list[int] = []
    range_start = None
    range_end = None

    result: dict[int, str] = {}

    args = parser.parse_input()

    if args.ports != "":
        ports = parser.get_ports(args.ports)
    elif args.range != "":
        range_start, range_end = parser.get_range(args.range)
    else:
        print("Invalid ports!")

    if len(ports) != 0:
        for port in ports:
            result[port] = check_port(args.host, port, args.timeout)

        output(args.output, result, args.verbose)
    elif range_start is not None and range_end is not None:
        for port in range(range_start, range_end + 1):
            result[port] = check_port(args.host, port, args.timeout)

        output(args.output, result, args.verbose)

if __name__ == "__main__":
    main()