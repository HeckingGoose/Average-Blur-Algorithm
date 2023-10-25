# Import modules
import pygame, effects, sys

# Define constant values
maxWidth = 1500
maxHeight = 900

# Initialise window so pygame will let me load an image
pygame.display.init()
pygame.display.set_mode((1,1), 0, 32)

# Read input for image filename
print("Input the target image's filename")
valid = False
while not valid:
    fileName = input(">")
    fileType = fileName.split('.')[len(fileName.split('.'))-1]
    try:
        if fileType.lower() == "png":
            image = pygame.image.load(fileName).convert_alpha()
        else:
            image = pygame.image.load(fileName)
        valid = True
    except:
        print("File '" + fileName + "' not found!")

# Calculate values to scale image to (Stolen from my pixel sorter)
scaleFactor = 1
if image.get_width() > maxWidth:
    if (maxWidth / image.get_width()) * image.get_height() > maxHeight:
        scaleFactor = maxHeight / image.get_height()
    else:
        scaleFactor = maxWidth / image.get_width()

# Configure pygame
clock = pygame.time.Clock()
screen = pygame.surface.Surface((image.get_width() * scaleFactor, image.get_height() * scaleFactor))
display = pygame.display.set_mode((image.get_width() * scaleFactor, image.get_height() * scaleFactor), 0, 32)
pygame.display.set_caption("Blurring: " + fileName)
pygame.display.set_icon(image)

# Read input for blur radius
radius = -1
print("Input a blur radius")
while radius <= 0:
    radius = input(">")
    try:
        radius = int(radius)
        if radius <= 0:
            raise Exception
    except:
        print("Positive, real integers only!")

# Process image
image = effects.Blur(image, radius)
displayImage = pygame.transform.scale(image, (image.get_width() * scaleFactor, image.get_height() * scaleFactor))

# Update window title and image
pygame.display.set_caption("Blurred: " + fileName)
pygame.display.set_icon(image)

# Debug function to test fetching circle works
def DrawDebugCircle(x, y):
    pixels = effects.FetchPixelsAsCircle(image, x, y, radius)
    countx, county = 0, 0
    for column in pixels:
        county += 1
        countx = 0
        for row in column:
            countx += 1
            if row[2] == "y":
                display.set_at((countx, county), (0, 255, 0))  
# Main loop
while True:
    clock.tick(12)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fileName = fileName.split('.')
            pygame.image.save(image, "Blurred/" + fileName[0] + " - Blurred, radius " + str(radius) + "." + fileType)
            pygame.quit()
            sys.exit()
    display.blit(image, (0, 0))
    #DrawDebugCircle(15, 15)
    screen.blit(display, (0, 0))
    pygame.display.update()
