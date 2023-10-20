import math

def sphere_volume(radius):
    if radius < 0:
        return "Radius cannot be negative"
    else:
        volume = (4/3) * math.pi * radius**3
        return volume

radius = 5.0
volume = sphere_volume(radius)
print(f"The volume of a sphere with radius {radius} is {volume:.2f}")

       

