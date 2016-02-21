import sys
import os
sys.path.append("")
sys.path.insert(
    0,
    "/".join(os.path.dirname(os.path.abspath(__file__)).split("/")[:-1])
)

from openpyscad import *
Circle(10).offset(10).write("example.scad", with_print=True)
