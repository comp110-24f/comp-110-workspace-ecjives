"""9/27/24 - Variables, Scope, and Importing Functions Challenge Question"""

__author__ = "730745467"

def get_coords (xs:str, ys:str) -> None:
    x_index:int = 0
    while (x_index < len(xs)):
        y_index:int = 0
        while (y_index < len(ys)):
            print(f"({xs[x_index]}, {ys[y_index]})")
            y_index += 1
        x_index += 1