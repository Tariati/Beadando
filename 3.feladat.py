import matplotlib.pyplot as plt
import matplotlib.image as image
import numpy as np
import random

primls = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
211, 223, 227, 229, 233, 239, 241, 251]
img=image.imread("virag.jpg")
averageint = img.mean()
def atalakito(kep):

    width = kep.shape[0]
    height = kep.shape[1]
    result = np.zeros((width,height,3),dtype=int)
    redCurrent = 1
    for row in range(len(result)):
        for pixel in range(len(result[row])):
            if redCurrent > 255:
                 redCurrent = 1

            result[row][pixel][0] = redCurrent
            result[row][pixel][1] = random.choice(primls)
            if img[row][pixel] - averageint < 0:
                result[row][pixel][2] = img[row][pixel]
            else:
                result[row][pixel][2] = img[row][pixel] - averageint
            redCurrent += 1

    return result

result = atalakito(img)
plt.imshow(result)
plt.show()



