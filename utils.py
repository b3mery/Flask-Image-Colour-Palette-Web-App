from colorthief import ColorThief

def rgb_to_hex(rgb:tuple):
    """Converts RGB Tuple to Hexadecimal 

    Args:
        rgb (tuple): RGB Tuple

    Returns:
        str: Hexadecimal Colour Code
    """
    return '#'+'%02x%02x%02x'.upper() % rgb

def get_colour_palette(file):
    color_thief = ColorThief(file)
    color_palette = color_thief.get_palette(color_count=11, quality=11)
    return color_palette

def extract_top_hex_colours_from_image(file):
    top_10_rgb = get_colour_palette(file)
    return [rgb_to_hex(rgb) for rgb in top_10_rgb]

