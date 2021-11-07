
import drawBot
from random import randint 
drawBot.size(1000,1000)
im = drawBot.ImageObject()

global range_to_use


import random 

def generate_image():

    with im: 
        
        range_to_use= randint(1400,2999)
        print(range_to_use)

        for i in range(100,range_to_use):
            drawBot.blendMode("difference")
            
            drawBot.linearGradient(
        (-100, 1000),                         # startPoint
        (-800, 8000),                         # endPoint
        [    (random.randint(-100, 100), random.randint(-100, 100),random.randint(-100, 100)),(random.randint(-100, 100), random.randint(-100, 1000),random.randint(1, 1000)),(random.randint(1, 10000), random.randint(1, 1000),random.randint(1, 1000))],  # colors
        [0, .2, 1]                          # locations
        )


            drawBot.polygon((random.randint(-100, 10000), random.randint(-100, 1000)), (random.randint(-100, 1000), random.randint(-100, 1000)), (random.randint(-100, 1000), random.randint(-100, 1000)), (random.randint(-100, 1000), random.randint(-100, 10000)), close=True)

        # stroke(random.randint(100,1000))
    # draw a line between two given points
        # #line((random.randint(1, 10000), random.randint(1, 10000)), (random.randint(1, 10000), random.randint(1, 1000)))
            drawBot.rect(random.randint(-111, 1000), random.randint(-111, 10000),random.randint(-111, 10), random.randint(-111, 10000))
            drawBot.cmykFill(11, 11, 10, 1)
            
        
            randStroke=random.randint(0, 1)
        
            drawBot.stroke(random.randint(0, 1), random.randint(0, 1),random.randint(0, 1),random.randint(0, 1))
            drawBot.oval(random.randint(0, 1000), random.randint(0, 1000),random.randint(100, 1000), random.randint(100, 1000))
        
        
            (random.randint(1, 10000), random.randint(1, 1000),random.randint(1, 1000)),(random.randint(1, 10000), random.randint(1, 1000),random.randint(1, 1000))
            
    im.colorInvert()

    intensityUse=random.randint(10,199)
    print(f"intensity is {intensityUse}")
    im.edges(intensity=intensityUse )


    posterizeValue=random.randint(10,199)
    print(f"posterize level is {posterizeValue}")
    im.colorPosterize(levels=posterizeValue)


    drawBot.image(im, (0,0))

    num=random.randint(0, 100000000)

    drawBot.saveImage(
            f"~/Downloads/moss/{range_to_use}-{posterizeValue}-{intensityUse}-{num}.png"
        )





for i in range(100):
    generate_image()
