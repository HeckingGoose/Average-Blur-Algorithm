import pygame, time

def Blur(image, radius):
    currentTime = time.time()
    width = image.get_width()
    height = image.get_height()
    newSurf = pygame.surface.Surface((width, height))
    for x in range(width):
        for y in range(height):
            pixels = FetchPixelsAsCircle(image, x, y, radius)
            fR, fG, fB = 0, 0, 0
            area = 0
            for column in pixels:
                for row in column:
                    if row[2] == 'y':
                        fR += image.get_at((row[0], row[1])).r
                        fG += image.get_at((row[0], row[1])).g
                        fB += image.get_at((row[0], row[1])).b
                        area += 1
            fR = fR / area
            fG = fG / area
            fB = fB / area
            newSurf.set_at((x,y), (fR, fG, fB))
    print("Done in " + str(time.time() - currentTime) + " seconds.")
    return newSurf

def FetchPixelsAsCircle(image, x, y, radius):
    radiusSquared = radius * radius
    imageWidth = image.get_width()
    imageHeight = image.get_height()
    pixels = []
    for h in range(2 * radius + 1):
        tempPixels = []
        for w in range(2 * radius + 1):
            absoluteX = x + (w - radius)
            absoluteY = y + (h - radius)
            if radiusSquared >= ((absoluteX - x)**2 + (absoluteY - y)**2) and absoluteX > -1 and absoluteY >-1 and absoluteX < imageWidth and absoluteY < imageHeight:
                tempPixels.append([absoluteX, absoluteY, "y"])
            else:
                tempPixels.append([absoluteX, absoluteY, "n"])
        pixels.append(tempPixels)
    return pixels
