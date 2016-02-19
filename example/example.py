import sys
import os
sys.path.append("")
sys.path.append(
    "/".join(os.path.dirname(os.path.abspath(__file__)).split("/")[:-1])
)

import openpyscad as ops  # noqa

c1 = ops.Cube([20, 10, 10])
c2 = ops.Cube([10, 20, 10])
c3 = ops.Cube([10, 10, 20])

d1 = c1 + c2 + c3
d2 = c1 & c2 & c3

d1.write("example.scad")
# d2.write("example.scad")
