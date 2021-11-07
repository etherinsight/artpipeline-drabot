```python

import drawBot
import random 

from random import randint 
drawBot.size(1000,1000)
im = drawBot.ImageObject()






with im: 

    for i in range(100,randint(200,1999)):
        
        drawBot.linearGradient(
    (100, 100),                         # startPoint
    (800, 800),                         # endPoint
    [    (random.randint(1, 100), random.randint(1, 100),random.randint(1, 100)),(random.randint(1, 100), random.randint(1, 1000),random.randint(1, 1000)),(random.randint(1, 10000), random.randint(1, 1000),random.randint(1, 1000))],  # colors
    [0, .2, 1]                          # locations
    )


        drawBot.polygon((random.randint(1, 10000), random.randint(1, 1000)), (random.randint(1, 1000), random.randint(1, 1000)), (random.randint(1, 1000), random.randint(1, 1000)), (random.randint(1, 1000), random.randint(1, 10000)), close=True)

    # stroke(random.randint(100,1000))
# draw a line between two given points
    # #line((random.randint(1, 10000), random.randint(1, 10000)), (random.randint(1, 10000), random.randint(1, 1000)))
        drawBot.rect(random.randint(1, 1000), random.randint(1, 10000),random.randint(1, 10), random.randint(1, 10000))
        drawBot.cmykFill(11, 11, 10, 1)
        drawBot.blendMode("difference")
    
        drawBot.randStroke=random.randint(0, 1)
    
        drawBot.stroke(random.randint(0, 1), random.randint(0, 1),random.randint(0, 1),random.randint(0, 1))
        drawBot.oval(random.randint(0, 1000), random.randint(0, 1000),random.randint(1000, 1000), random.randint(100, 1000))
    
    
        
im.colorInvert()
im.edges(intensity=21)

im.colorPosterize(levels=9)


drawBot.image(im, (-90, -90))
drawBot.saveImage("~/Downloads/aRect.png")
```


