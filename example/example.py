import sys
import os
sys.path.append("")
sys.path.insert(
    0,
    "/".join(os.path.dirname(os.path.abspath(__file__)).split("/")[:-1])
)
# sys.path.append(
#     "/".join(os.path.dirname(os.path.abspath(__file__)).split("/")[:-1])
# )


from openpyscad import *
import openpyscad


def sample_module():
    return Cube([20, 20, 10]).color("Yellow")

e = Empty()
for i in range(10):
    e += sample_module().translate([i, i, i])

m = Minkowski().append([Cube([10, 10, 1]), Cylinder(r=2, h=1, _fn=50)])
h = Hull().append([
    Circle(10).translate([15, 10, 0]),
    Circle(10)
])
h.write("example.scad", with_print=True)
