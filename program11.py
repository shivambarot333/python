def are_points_collinear(x1, y1, x2, y2, x3, y3):
    # Using the area of triangle formula, if area == 0, points are collinear
    area = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    return area == 0
x1, y1 = map(float, input("Enter coordinates of point 1 (x1 y1): ").split())
x2, y2 = map(float, input("Enter coordinates of point 2 (x2 y2): ").split())
x3, y3 = map(float, input("Enter coordinates of point 3 (x3 y3): ").split())

if are_points_collinear(x1, y1, x2, y2, x3, y3):
    print("The points lie on the same straight line.")
else:
    print("The points do not lie on the same straight line.")
