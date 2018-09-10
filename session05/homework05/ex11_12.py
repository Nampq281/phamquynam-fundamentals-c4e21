#11
def is_inside(point, area):
    [x, y] = point
    [a, b, width, height] = area
    if abs(a) <= abs(x) <= abs(a) + width:
        if abs(b) <= abs(y) <= abs(b) + height:
            return True
        else:
            return False
    else:
        return False

#12
test1 = is_inside([200, 120], [140, 60, 100, 200]) 
test2 =  is_inside([100, 120], [140, 60, 100, 200])
if test1 and not test2:
    print("Your function is correct")
else:
    print("Bug detected")