def read_messy_input(string) -> list[float]:
    return [float(s) for s in string.replace(",", ".").split(" ")]
