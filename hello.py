# A program to find the radious of a circle

import math

def circle_radius(area):
  if area < 0:
    return None
  radius = math.floor(math.sqrt(area / math.pi)) 
  return 

area = 25
radius = circle_radius(area)
if radius is not None:
  print(f"The radius of a circle with an area of {area} is: {radius}")