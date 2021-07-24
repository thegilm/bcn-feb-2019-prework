import math
points = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5),
          (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2),
          (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2),
          (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]

print("double hit(s)?")
for arrow1 in range(len(points)):
    for arrow2 in range(len(points)):
        if arrow1 == arrow2:
            continue
        if points[arrow1][0] == points[arrow2][0] and points[arrow1][1] == points[arrow2][1]:
            print("yep: "+str(points[arrow1][0])+", "+str(points[arrow1][1]))
            continue

print("Quadrants:")
q1 = 0
q2 = 0
q3 = 0
q4 = 0
for point in points:
    if point[0] > 0 and point[1] > 0:
        q1 += 1
    if point[0] < 0 and point[1] > 0:
        q2 += 1
    if point[0] < 0 and point[1] < 0:
        q3 += 1
    if point[0] > 0 and point[1] < 0:
        q4 += 1

print("Q1: "+str(q1)+", Q2: "+str(q2)+", Q3: "+str(q3)+", Q4: "+str(q4))

print("distance to center:")
# https://www.delftstack.com/de/howto/numpy/calculate-euclidean-distance/
origin = (0,0)
bestMatchIndex = 0
distanceToCenter = 10
temp = 0

radius = 9
failedShots = 0

for index in range(len(points)):
    temp = math.dist(origin,points[index])
    #print(temp)
    if temp > 9:
        failedShots += 1
    if temp < distanceToCenter:
        distanceToCenter = temp
        bestMatchIndex = index

print("Point "+str(points[bestMatchIndex][0])+", "+str(points[bestMatchIndex][1])+" is closest to the center, distance is "+str(distanceToCenter))
print(str(failedShots)+" arrows missed the target and have to be picked up in the woods.")