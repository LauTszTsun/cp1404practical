COLOR_NAMES ={"AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff",
    "BlueViolet": "#8a2be2"}
color_name = input("Enter a color name: ").lower()
while color_name != "":
    try:
        print(f"{color_name} is {COLOR_NAMES[color_name]}")
    except KeyError:
        print("Invalid color name")
    color_name = input("Enter a color name: ").lower()
