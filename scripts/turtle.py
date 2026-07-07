#!/usr/bin/env python3
import re
import sys
import math
import matplotlib.pyplot as plt
 
 
def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "./turtle"
 
    with open(path, "r") as f:
        lines = f.readlines()
 
    x, y = 0, 0
    angle = 0
    path_x, path_y = [x], [y]
 
    for line in lines:
        line = line.strip()
        if not line:
            continue
 
        if "Tourne gauche" in line:
            deg = int(re.search(r"de (\d+) degrees", line).group(1))
            angle = (angle + deg) % 360
        elif "Tourne droite" in line:
            deg = int(re.search(r"de (\d+) degrees", line).group(1))
            angle = (angle - deg) % 360
        elif "Avance" in line:
            dist = int(re.search(r"Avance (\d+) spaces", line).group(1))
            x += dist * math.cos(math.radians(angle))
            y += dist * math.sin(math.radians(angle))
            path_x.append(x)
            path_y.append(y)
        elif "Recule" in line:
            dist = int(re.search(r"Recule (\d+) spaces", line).group(1))
            x -= dist * math.cos(math.radians(angle))
            y -= dist * math.sin(math.radians(angle))
            path_x.append(x)
            path_y.append(y)
 
    plt.plot(path_x, path_y)
    plt.axis("equal")
    plt.title("Turtle Path")
    plt.show()

if __name__ == "__main__":
    main()