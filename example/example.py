import sys
import os
sys.path.append("")
sys.path.append(
    "/".join(os.path.dirname(os.path.abspath(__file__)).split("/")[:-1])
)

import openpyscad as ops  # noqa

c1 = ops.Cube([20, 20, 20])
c2 = ops.Cube([10, 10, 40]).translate([5, 5, -10])
(c1 - c2).rotate([0, 0, 45]).write("example.scad")
