from PIL import Image

milk = Image.open("milk2.jpg")
print milk.getdata()[200]

def getRed(pixel):
    return pixel[0]

def getGreen(pixel):
    return pixel[1]

def getBlue(pixel):
    return pixel[2]

def getAveragePixel(pixel):
    avg = ((getRed(pixel) + getGreen(pixel) + getBlue(pixel)) / 3)
    return (avg, avg, avg)

def getrandompixel(pixel):
    avg2 = ((getRed(pixel) + getGreen(pixel) + getBlue(pixel)) / 4)
    return (avg2, avg2, avg2)

# def getMedian(pixel):
#     red = getRed(pixel)
#     green = getGreen(pixel)
#     blue = getBlue(pixel)
#     return (red, green, blue)


new_pixel = []
size = milk.height * milk.width
old_pixels = milk.getdata()
for i in range(size):
    old_pixel_variable = old_pixels[i]
    if (i < size / 3):
        new_pixel_variable = getAveragePixel(old_pixel_variable)
    elif (i < size / 2):
        new_pixel_variable = getrandompixel(old_pixel_variable)
    else:
        new_pixel_variable = old_pixel_variable
    new_pixel.append(new_pixel_variable)

    #top bottom middle
    #left right
    #put bottom half of pic on top & top half on bottom
    #make it look like its snowing
    #make it so it shows random filters

# for pixel in milk.getdata():
#     # red_pixel = (255, 0, 0)
#     # new_pixel.append(red_pixel)
#     # red_value = getRed(pixel)
#     # green_value = getGreen(pixel)
#     # blue_value = getBlue(pixel)
#     # new_pixel_variable = (red_value, green_value, blue_value)
#     new_pixel_variable = getMedian(pixel)
#     new_pixel.append(new_pixel_variable)


print new_pixel[200]

new_image = Image.new("RGB", milk.size)
#new_image.show()
new_image.putdata(new_pixel)
new_image.show()
