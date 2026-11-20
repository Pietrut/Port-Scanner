def console_output(result: dict[int, str], verbose: bool) -> None:
    print("[PORT]     [STATE]")

    for port, status in result.items():
        if not verbose and status != "Open":
            return

        print(f"{port:<11}{status.upper()}")

def file_output(file_name: str, result: dict[int, str], verbose: bool) -> None:
    with open(file_name, "a") as file:
        file.write("[PORT]     [STATE]\n")

        for port, status in result.items():
            if not verbose and status != "Open":
                return

            file.write(f"{port:<11}{status.upper()}\n")

def output(output_type: str, result: dict[int, str], verbose: bool) -> None:
    if output_type.lower() == "console":
        console_output(result, verbose)
    else:
        file_output(output_type, result, verbose)