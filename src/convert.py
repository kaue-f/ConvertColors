import math


def hex_to_oklch(hex_color):
    hex_color = hex_color.lstrip('#')

    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    r, g, b = r / 255.0, g / 255.0, b / 255.0

    gama = 2.16

    r = r ** gama
    g = g ** gama
    b = b ** gama

    l = (0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b) ** (1/3)
    m = (0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b) ** (1/3)
    s = (0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b) ** (1/3)

    L = 0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s
    a = 1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s
    b = 0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s

    chroma = math.sqrt(a ** 2 + b ** 2)

    hue = math.degrees(math.atan2(b, a))
    if hue < 0:
        hue += 360

    L = L * 100

    return (f"oklch({L:.1f}% {chroma:.3f} {hue:.3f})")
