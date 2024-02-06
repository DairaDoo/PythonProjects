import colorgram

# My Code
colors = colorgram.extract('image.jpg', 25)
rbg_color_list = []


def getRgb(color_p):
    """"Get an RGB tuple for each element in object colors"""
    colorList = []
    for color in range(len(color_p.rgb)):
        getCurrentColor = color_p.rgb[color]
        colorList.append(getCurrentColor)
    return tuple(colorList)


for i in range(len(colors)):
    rbg_color_list.append(getRgb(colors[i]))
print(rbg_color_list)

# Angela version
# rbg_color_list2 = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rbg_color_list2.append(new_color)
# print(rbg_color_list2)