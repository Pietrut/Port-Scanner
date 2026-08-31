def show(port: int, status: str, verbose: bool) -> None:
    if not verbose and status != "Open":
        return

    spaces = "     "
    port_string = str(port)

    for _ in range(6 - len(port_string)):
        spaces += " "

    print(port_string + spaces + status.upper())