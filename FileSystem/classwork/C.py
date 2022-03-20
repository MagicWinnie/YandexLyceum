import sys

sys.stdout = open("res.txt", "w")

pts = []
for line in sys.stdin:
    x, y = map(float, line.split())
    pts.append([x, y])
pts.sort()

area = 0
for i in range(1, len(pts)):
    area += (pts[i - 1][1] + pts[i][1]) / 2 * (pts[i][0] - pts[i - 1][0])

print(area)
