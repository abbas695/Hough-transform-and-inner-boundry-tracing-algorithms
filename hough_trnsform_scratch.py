from PIL import Image, ImageDraw
from math import sqrt, pi, cos, sin
from collections import defaultdict
import cv2
import numpy as np

# Load image:
input_image = cv2.imread("D:\circles.jpg")
gray=cv2.cvtColor(input_image,cv2.COLOR_RGB2GRAY)

# Output image:

# Find circles
rmin = 40
rmax = 60
steps = 10
threshold = 0.6

points = []
for r in range(rmin, rmax + 1):
    for t in range(steps):
        points.append((r, int(r * cos(2 * pi * t / steps)), int(r * sin(2 * pi * t / steps))))
acc = defaultdict(int)
edges= cv2.Canny(gray,100,200,apertureSize=3, L2gradient=True)
cordinates=np.nonzero(edges)
keep = set()
for x in range(len(cordinates[0])):
        keep.add((cordinates[1][x], cordinates[0][x]))

for x, y in keep :
    for r, dx, dy in points:
        a = x - dx
        b = y - dy
        acc[(a, b, r)] += 1

circles = []
for k, v in sorted(acc.items(), key=lambda i: -i[1]):
    x, y, r = k
    if v / steps >= threshold and all((x - xc) ** 2 + (y - yc) ** 2 > rc ** 2 for xc, yc, rc in circles):
        print(v / steps, x, y, r)
        circles.append((x, y, r))

for x, y, r in circles:
    cv2.circle(input_image,(x,y),r,(0,255,0),3)

# Save output image
cv2.imshow('circles', input_image)
cv2.waitKey(0)