import random
from random import randint
import drawBot

imageName = "test"
imagesToGenerate = 3


drawBot.size(1000, 1000)


global randomCol

randomCol = random.randint(1, 4)
print(type(randomCol))
print(randomCol)


def colorr(num):
    randomColumn = num

    if randomColumn == 1:
        return (random.random(), 0, 0, 1, 1)
    elif randomColumn == 2:
        return (0, random.random(), 0, 1, 2)
    elif randomColumn == 3:
        return (0, 0, random.random(), 1, 3)
    else:
        return (random.random(), random.random(), random.random(), 1, 4)


colorr(randomCol)

colorToUse = colorr(randomCol)

print(colorToUse)


def generate_image():
    drawBot.newDrawing()
    im = drawBot.ImageObject()

    with im:

        range_to_use = randint(1000, 2200)
        print(range_to_use)

        randomCol = random.randint(1, 4)
        colorToUse = colorr(randomCol)
        for i in range(100, range_to_use):
            drawBot.blendMode("difference")

            drawBot.linearGradient(
                (-100, 1000),  # startPoint
                (-800, 8000),  # endPoint
                [
                    (
                        random.randint(-100, 100),
                        random.randint(-100, 100),
                        random.randint(-100, 100),
                    ),
                    (
                        random.randint(-100, 100),
                        random.randint(-100, 1000),
                        random.randint(1, 1000),
                    ),
                    (
                        random.randint(1, 10000),
                        random.randint(1, 1000),
                        random.randint(1, 1000),
                    ),
                ],  # colors
                [0, 0.2, 1],  # locations
            )

            # will add circle of darkness
            if random.random() > 0.5:
                drawBot.oval(
                    random.randint(0, 1000),
                    random.randint(0, 1000),
                    random.randint(0, 1000),
                    random.randint(0, 1000),
                )

            drawBot.polygon(
                (random.randint(-100, 10000), random.randint(-100, 1000)),
                (random.randint(-100, 1000), random.randint(-100, 1000)),
                (random.randint(-100, 1000), random.randint(-100, 1000)),
                (random.randint(-100, 1000), random.randint(-100, 10000)),
                close=True,
            )

            # stroke(random.randint(100,1000))
            # draw a line between two given points
            # #line((random.randint(1, 10000), random.randint(1, 10000)), (random.randint(1, 10000), random.randint(1, 1000)))
            drawBot.rect(
                random.randint(-111, 1000),
                random.randint(-111, 10000),
                random.randint(-111, 10),
                random.randint(-111, 10000),
            )
            drawBot.cmykFill(colorToUse[0], colorToUse[1], colorToUse[2], colorToUse[3])

            randStroke = random.randint(0, 1)

            strokeWidth = random.randint(0, 5)
            print(f"stroke is {strokeWidth}")

            drawBot.stroke(strokeWidth)

    im.colorInvert()

    intensityUse = random.randint(0, 199)
    print(f"intensity is {intensityUse}")
    im.edges(intensity=intensityUse)

    posterizeValue = random.randint(0, 199)
    print(f"posterize level is {posterizeValue}")
    im.colorPosterize(levels=posterizeValue)

    drawBot.image(im, (0, 0))

    random.randint(0, 100000000)

    drawBot.saveImage(
        f"~/Downloads/pointImage/100batch/{colorToUse[4]}-{posterizeValue}-{intensityUse}-{range_to_use}-{imageName}.png"
    )


for i in range(imagesToGenerate):
    generate_image()



