from enum import Enum

class Color:
    r: int
    g: int
    b: int
    i: int

    def __init__(r: int, g: int, b: int):
        c = Color()
        c.r = r
        c.g = g
        c.b = b
        c.i = 255
        return c

# White is not a valid color
class ColorName(Enum):
    RED = 1
    GREEN = 2
    BLACK = 3
    GRAY = 4
    BLACK = 5

def match_color(color: Color, min: Color, max: Color) -> bool:
    return color.r >= min.r and color.r <= max.r and color.g >= min.g and color.g <= max.g and color.b >= min.b and color.b <= max.b

def name_color(color: Color) -> None | ColorName:
    if match_color(color, Color(200, 0, 0), Color(255, 50, 50)):
        return ColorName.RED
    elif match_color(color, Color(0, 200, 0), Color(50, 255, 50)):
        return ColorNome.GREEN
    elif match_color(color, Color(0, 0, 0), Color(30, 30, 30)):
        return ColorName.BLACK
    elif match_color(color, Color(30,30,30), Color(100,100,100)):
        return ColorName.GRAY

    return None

