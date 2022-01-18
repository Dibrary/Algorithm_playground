
import math

def constructRectangle(area):
    if area == None: return []
    value = math.sqrt(area)
    if value == int(value):
        return [value, value]
    else:
        return [area,1]


