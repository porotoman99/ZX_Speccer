from PIL import Image
import os , sys , math

ZXvals = (0 , 215 , 255)
ditherPercent = (0 , 0.03125 , 0.0625 , 0.125 , 0.25 , 0.375 , 0.46875 , 0.50 , 0.625)
class ClosestPixel:
    diff = 1000
    r1 = 0
    g1 = 0
    b1 = 0
    r2 = 0
    g2 = 0
    b2 = 0
    dither = 0

for infile in sys.argv[1:]:
    f , e = os.path.splitext(infile)
    outfile = f + e
    try:
        img = Image.open(infile)
        img = img.convert("RGBA")
        xDim = img.size[0]
        yDim = img.size[1]
        imgout = img.resize((xDim * 4 , yDim * 4))
        print("Imported and copied image.")
        for yPos in range(yDim):
            print("Working...")
            for xPos in range(xDim):
                chR = img.getpixel((xPos , yPos))[0]
                chG = img.getpixel((xPos , yPos))[1]
                chB = img.getpixel((xPos , yPos))[2]
                chA = img.getpixel((xPos , yPos))[3]
                testPixel = ClosestPixel()
                for R1 in ZXvals:
                    for G1 in ZXvals:
                        for B1 in ZXvals:
                            for R2 in ZXvals:
                                for G2 in ZXvals:
                                    for B2 in ZXvals:
                                        for dither in ditherPercent:
                                            testRed = (R1 * dither) + (R2 * (1 - dither))
                                            testGreen = (G1 * dither) + (G2 * (1 - dither))
                                            testBlue = (B1 * dither) + (B2 * (1 - dither))
                                            pixelDiff = math.sqrt((testRed - chR)**2 + (testGreen - chG)**2 + (testBlue - chB)**2)
                                            if(pixelDiff < testPixel.diff):
                                                testPixel.diff = pixelDiff
                                                testPixel.r1 = round(R1)
                                                testPixel.g1 = round(G1)
                                                testPixel.b1 = round(B1)
                                                testPixel.r2 = round(R2)
                                                testPixel.g2 = round(G2)
                                                testPixel.b2 = round(B2)
                                                testPixel.dither = dither
                for yOut in range((yPos * 4) , ((yPos + 1)* 4)):
                    for xOut in range((xPos * 4) , ((xPos + 1)* 4)):
                        imgout.putpixel((xOut , yOut) , (testPixel.r2 , testPixel.g2 , testPixel.b2 , chA))
                if(testPixel.dither == 0.03125):
                    if((xPos + yPos) % 2 == 0):
                        imgout.putpixel(((xPos * 4)+0 , (yPos * 4)+0) , (testPixel.r1 , testPixel.g1 , testPixel.b1 , chA))
                elif(testPixel.dither == 0.0625):
                    if(xPos % 2 == 0):
                        imgout.putpixel(((xPos * 4)+0 , (yPos * 4)+0) , (testPixel.r1 , testPixel.g1 , testPixel.b1 , chA))
                    else:
                        imgout.putpixel(((xPos * 4)+0 , (yPos * 4)+2) , (testPixel.r1 , testPixel.g1 , testPixel.b1 , chA))
                elif(testPixel.dither == 0.125):
                    imgout.putpixel(((xPos * 4)+0 , (yPos * 4)+0) , (testPixel.r1 , testPixel.g1 , testPixel.b1 , chA))
                    imgout.putpixel(((xPos * 4)+2 , (yPos * 4)+2) , (testPixel.r1 , testPixel.g1 , testPixel.b1 , chA))
                elif(testPixel.dither == 0.25):
                    imgout.putpixel(((xPos * 4)+0 , (yPos * 4)+0) , (testPixel.r1 , testPixel.g1 , testPixel.b1 , chA))
                    imgout.putpixel(((xPos * 4)+0 , (yPos * 4)+2) , (testPixel.r1 , testPixel.g1 , testPixel.b1 , chA))
                    imgout.putpixel(((xPos * 4)+1 , (yPos * 4)+1) , (testPixel.r1 , testPixel.g1 , testPixel.b1 , chA))
                    imgout.putpixel(((xPos * 4)+1 , (yPos * 4)+3) , (testPixel.r1 , testPixel.g1 , testPixel.b1 , chA))
                elif(testPixel.dither == 0.375):
                    imgout.putpixel(((xPos * 4)+0 , (yPos * 4)+0) , (testPixel.r1 , testPixel.g1 , testPixel.b1 , chA))
                    imgout.putpixel(((xPos * 4)+2 , (yPos * 4)+0) , (testPixel.r1 , testPixel.g1 , testPixel.b1 , chA))
                    imgout.putpixel(((xPos * 4)+1 , (yPos * 4)+1) , (testPixel.r1 , testPixel.g1 , testPixel.b1 , chA))
                    imgout.putpixel(((xPos * 4)+0 , (yPos * 4)+2) , (testPixel.r1 , testPixel.g1 , testPixel.b1 , chA))
                    imgout.putpixel(((xPos * 4)+2 , (yPos * 4)+2) , (testPixel.r1 , testPixel.g1 , testPixel.b1 , chA))
                    imgout.putpixel(((xPos * 4)+3 , (yPos * 4)+3) , (testPixel.r1 , testPixel.g1 , testPixel.b1 , chA))
                elif(testPixel.dither == 0.46875):
                    imgout.putpixel(((xPos * 4)+0 , (yPos * 4)+0) , (testPixel.r1 , testPixel.g1 , testPixel.b1 , chA))
                    imgout.putpixel(((xPos * 4)+2 , (yPos * 4)+0) , (testPixel.r1 , testPixel.g1 , testPixel.b1 , chA))
                    imgout.putpixel(((xPos * 4)+1 , (yPos * 4)+1) , (testPixel.r1 , testPixel.g1 , testPixel.b1 , chA))
                    imgout.putpixel(((xPos * 4)+3 , (yPos * 4)+1) , (testPixel.r1 , testPixel.g1 , testPixel.b1 , chA))
                    imgout.putpixel(((xPos * 4)+0 , (yPos * 4)+2) , (testPixel.r1 , testPixel.g1 , testPixel.b1 , chA))
                    imgout.putpixel(((xPos * 4)+2 , (yPos * 4)+2) , (testPixel.r1 , testPixel.g1 , testPixel.b1 , chA))
                    imgout.putpixel(((xPos * 4)+3 , (yPos * 4)+3) , (testPixel.r1 , testPixel.g1 , testPixel.b1 , chA))
                    if((xPos + yPos) % 2 == 0):
                        imgout.putpixel(((xPos * 4)+1 , (yPos * 4)+3) , (testPixel.r1 , testPixel.g1 , testPixel.b1 , chA))
                elif(testPixel.dither == 0.5):
                    imgout.putpixel(((xPos * 4)+0 , (yPos * 4)+0) , (testPixel.r1 , testPixel.g1 , testPixel.b1 , chA))
                    imgout.putpixel(((xPos * 4)+2 , (yPos * 4)+0) , (testPixel.r1 , testPixel.g1 , testPixel.b1 , chA))
                    imgout.putpixel(((xPos * 4)+1 , (yPos * 4)+1) , (testPixel.r1 , testPixel.g1 , testPixel.b1 , chA))
                    imgout.putpixel(((xPos * 4)+3 , (yPos * 4)+1) , (testPixel.r1 , testPixel.g1 , testPixel.b1 , chA))
                    imgout.putpixel(((xPos * 4)+0 , (yPos * 4)+2) , (testPixel.r1 , testPixel.g1 , testPixel.b1 , chA))
                    imgout.putpixel(((xPos * 4)+2 , (yPos * 4)+2) , (testPixel.r1 , testPixel.g1 , testPixel.b1 , chA))
                    imgout.putpixel(((xPos * 4)+3 , (yPos * 4)+3) , (testPixel.r1 , testPixel.g1 , testPixel.b1 , chA))
        imgout.save(outfile)
    except IOError:
        print("IOError for " , infile)
print("Done!")
