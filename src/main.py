import socket
import parser as parser
import output as output

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
    range_start = 0
    range_end = 0

    args = parser.parse_input()
    host = args.host
    timeout = args.timeout

    if args.ports != "0":
        ports = parser.get_ports(args.ports)
    elif args.range != "0-0":
        range_start, range_end = parser.get_range(args.range)
    else:
        print("Invalid ports!")

    print("[PORT]     [STATE]")
    if len(ports) != 0:
        for port in ports:
            output.show(port, check_port(host, port, timeout), args.verbose)
    elif range_start != 0 and range_end != 0:
        for port in range(range_start, range_end + 1):
            output.show(port, check_port(host, port, timeout), args.verbose)

if __name__ == "__main__":
    main()