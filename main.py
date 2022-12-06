import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def compareNeighborhood(neighborhood, threshold, numNeighbours):
    meanX = 0
    meanY = 0
    for d in range(numNeighbours):
        meanX += abs(neighborhood[0][0] - neighborhood[0][d+1])   
        meanY += abs(neighborhood[0][0] - neighborhood[d+1][0])
    if(meanX/numNeighbours > threshold or meanY/numNeighbours > threshold):
        return True
    else:
        return False    


def edgeDetector(img, threshold, numNeighbours):
    l,c = img.shape
    imgEdge = np.zeros(shape=(l, c), dtype=np.uint8)
    x = 0
    for i in range(l-numNeighbours-2):
        for j in range(c-numNeighbours-2):
            if(compareNeighborhood(img[i:i+numNeighbours+2,j:j+numNeighbours+2], threshold, numNeighbours)):
                imgEdge[i,j] = 255
                x += 1
            else:
                imgEdge[i,j] = 0
    print(x)
    return imgEdge


def grayScale(l,c,image):
    shapes_Gray = np.zeros(shape=(l, c), dtype=np.uint8)
    for i in range(l):
        for j in range(c):
            r = float(image[i, j, 0])
            g = float(image[i, j, 1])
            b = float(image[i, j, 2])
            
            shapes_Gray[i, j] = (r + g + b) / 3
    return shapes_Gray


imagemComplexa = np.array(Image.open("museum.jpg"))[:, :, :3]
imagemSimples = np.array(Image.open("shapes.png"))[:, :, :3]

lSimples, cSimples, pSimples = imagemSimples.shape
lComplexa, cComplexa, pComplexa = imagemComplexa.shape

imagemSimplesCinza = grayScale(lSimples,cSimples,imagemSimples)
imagemComplexaCinza = grayScale(lComplexa,cComplexa,imagemComplexa)


result1 = edgeDetector(imagemSimplesCinza,200,5)
result2 = edgeDetector(imagemSimplesCinza,230,25)
result3 = edgeDetector(imagemComplexaCinza,200,5)
result4 = edgeDetector(imagemComplexaCinza,230,10)

plt.figure(figsize=(16, 16))
plt.subplot(1, 4, 1)
plt.imshow(result1, cmap="gray")
plt.subplot(1, 4, 2)
plt.imshow(result2, cmap="gray")
plt.subplot(2, 4, 3)
plt.imshow(result3, cmap="gray")
plt.subplot(2, 4, 4)
plt.imshow(result4, cmap="gray")

plt.show()


