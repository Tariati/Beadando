import matplotlib.pyplot as plt
import matplotlib.image as image
import random

primls = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
211, 223, 227, 229, 233, 239, 241, 251,]
img=image.imread("flowers.jpg")
plt.imshow()
plt.show()
def atalakito(kep):
    red = img[:, :, 2]
    green = img[:, :, 1]
    blue = img[:, :, 0]
    for i in range(red):
        red += 1
    for j in range(green):
        green[j] = random.choice(primls)
    for k in range(blue):



