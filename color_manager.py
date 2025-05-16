from time import sleep
import color_sensor
from hub import port

class Color:
    r: float
    g: float
    b: float
    i: float

    def __init__(self, r: float, g: float, b: float):
        self.r = r
        self.g = g
        self.b = b
        self.i = (r + g + b) / 3

class ColorName:
    RED = 1
    GREEN = 2
    BLACK = 3
    GRAY = 4
    BLACK = 5

def calculate_percentages(r: float, g: float, b: float) -> Color:
    total = r + g + b
    if total == 0:
        return Color(0, 0, 0)
    
    return Color(
        (r / total) * 100,
        (g / total) * 100,
        (b / total) * 100
    )

def match_color(color: Color, min_percent: float, dominant_color: str) -> bool:
    if dominant_color == 'r':
        return color.r >= min_percent and color.r > color.g and color.r > color.b
    elif dominant_color == 'g':
        return color.g >= min_percent and color.g > color.r and color.g > color.b
    elif dominant_color == 'b':
        return color.b >= min_percent and color.b > color.r and color.b > color.g
    return False

def name_color(color: Color) -> None | ColorName:
    intensity = color.i

    if intensity < 10:
        return ColorName.BLACK
    
    rgb_diff = max(abs(color.r - color.g), abs(color.g - color.b), abs(color.r - color.b))
    if rgb_diff < 15 and 10 <= intensity <= 40:
        return ColorName.GRAY

    if match_color(color, 45, 'r'):
        return ColorName.RED
    elif match_color(color, 45, 'g'):
        return ColorName.GREEN

    return None

while True:
    rgbi = color_sensor.rgbi(port.A)
    color = calculate_percentages(rgbi[0], rgbi[1], rgbi[2])
    
    color_name = name_color(color)

    print(color.r)
    print(color.g)
    print(color.b)
    print(color.i)
    print(color_name)

    sleep(0.5)
