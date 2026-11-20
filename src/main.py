import socket
import parser
from output import output
from concurrent.futures import ThreadPoolExecutor

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
    except OSError as e:
        return f"Error: {e}"
    finally:
        sock.close()

def main() -> None:
    ports: list[int] = []

    result: dict[int, str] = {}

    args = parser.parse_input()

    if args.ports != "":
        ports = parser.get_ports(args.ports)
    elif args.range != "":
        range_start, range_end = parser.get_range(args.range)

        if range_start and range_end:
            ports = list(range(range_start, range_end + 1))
        else:
            print("Invalid range!")
            return
    else:
        print("Invalid ports!")
        return

    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(
            lambda port: check_port(args.host, port, args.timeout),
            ports
        )

        result = dict(zip(ports, results))

    output(args.output, result, args.verbose)

if __name__ == "__main__":
    main()