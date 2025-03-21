from colorsys import rgb_to_hsv


def hex_to_oklch(hex):

    def hex_to_oklch(hex_color):
        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        r, g, b = r / 255.0, g / 255.0, b / 255.0

        r = r**2.2
        g = g**2.2
        b = b**2.2

        l = (0.2126*r + 0.7152*g+0.0722*b) ** (1/2.2)
        a = r-g
        b = b-g

        chroma = (a**2 + b**2) ** 0.5
        hue = (a / chroma if chroma != 0 else 0)

        return (l, chroma, hue)

    hex_to_oklch(hex)
