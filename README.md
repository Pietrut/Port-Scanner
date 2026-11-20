# Port Scanner

A lightweight, multithreaded TCP port scanner written in Python. It allows users to scan individual ports, custom port lists, or entire port ranges on a specified host.

## Features

- **TCP port scanning** – Detects open and closed TCP ports.
- **Multithreading** – Uses `ThreadPoolExecutor` to scan multiple ports concurrently.
- **Custom port selection** – Scan individual ports, comma-separated lists, or port ranges.
- **Configurable timeout** – Specify how long to wait for a connection attempt.
- **Multiple output options** – Display results in the console or save them to a file.
- **Verbose mode** – Enable additional scanning information.

## Requirements

- Python 3.10 or newer
- No external dependencies

## Installation

Clone and install the repository:

```bash
git clone https://github.com/Pietrut/Port-Scanner.git
cd Port-Scanner
python -m pip install -e .
```

## Usage

Run the scanner using:

```bash
port-scanner [OPTIONS]
```

### Arguments

| Argument | Default | Description |
|---|---|---|
| `--host` | `localhost` | Target hostname or IPv4 address |
| `--ports` | `None` | Comma- or space-separated list of ports |
| `--range` | `None` | Port range in `START-END` format |
| `--timeout` | `1.0` | Connection timeout in seconds |
| `--verbose` | `False` | Enable verbose output |
| `--output` | `Console` | Console output or file path |

### Examples

**Scan a single port:**

```bash
port-scanner --host 127.0.0.1 --ports 80
```

**Scan multiple ports:**

```bash
port-scanner --host example.com --ports "22,80,443,8080"
```

**Scan a port range:**

```bash
port-scanner --host 192.168.1.1 --range 1-1024
```

**Customize the timeout:**

```bash
port-scanner --host example.com --range 1-1000 --timeout 2.5
```

**Save results to a file:**

```bash
port-scanner --host example.com --ports "80,443" --output results.txt
```

**Enable verbose mode:**

```bash
port-scanner --host localhost --range 1-1000 --verbose
```

## Port State

Each port is classified as:

- `Open` – The TCP connection was successful.
- `Closed` – The connection was refused.
- `Timeout` – The connection attempt timed out.


## Disclaimer

This project is intended for educational purposes and authorized network testing only. Only scan systems and networks you own or have explicit permission to test.

## License

This project is licensed under the MIT License.