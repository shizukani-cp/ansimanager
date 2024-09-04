COLORS = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]

def _escaped_print(arg: str):
    print(f"\x1b[{arg}", end="")

def clear_display():
    _escaped_print("2J")

def up(n: int):
    _escaped_print(f"{n}A")

def down(n: int):
    _escaped_print(f"{n}B")

def right(n: int):
    _escaped_print(f"{n}C")

def left(n: int):
    _escaped_print(f"{n}D")

def goto(x: int, y: int):
    _escaped_print(f"{y};{x}H")

def scroll(n: int):
    _escaped_print(f"{n}S")

def scroll_back(n: int):
    _escaped_print(f"{n}T")

def clear_font():
    _escaped_print("0m")

def change_font_color(color: str):
    try:
        color_code = 30 + COLORS.index(color)
        _escaped_print(f"{color_code}m")
    except ValueError:
        raise ValueError("An undefined color was specified.")

def change_background_color(color: str):
    try:
        color_code = 40 + COLORS.index(color)
        _escaped_print(f"{color_code}m")
    except ValueError:
        raise ValueError("An undefined color was specified.")
