import openpyscad as ops


class Custom3dShapes(object):

    @staticmethod
    def dice(edge=15, fn=32):
        """ dice
        """
        edge = float(edge)
        # dice
        c = ops.Cube(edge, center=True)
        s = ops.Sphere(edge * 3 / 4, center=True)
        dice = c & s
        # points
        c = ops.Circle(edge / 12, _fn=fn)
        h = 0.7
        point = c.linear_extrude(height=h)
        point1 = point.translate([0, 0, edge / 2 - h / 2])
        point2_1 = point1.rotate(a=90, v=[1, 0, 0]).translate([edge / 6, 0, edge / 6])
        point2_2 = point2_1.mirror([-edge / 6, 0, -edge / 6])
        point2 = point2_1 + point2_2
        point3 = point2.rotate(a=90, v=[0, 0, 1]) + point1.rotate(a=90, v=[0, 1, 0])
        point4_12 = point2.rotate(a=-90, v=[0, 0, 1])
        point4 = point4_12 + point4_12.mirror([0, 1, 0])
        point5_123 = point3.rotate(a=90, v=[0, 0, 1])
        point5 = point5_123 + point5_123.mirror([1, 0, 0])
        point6_1 = point.translate([0, 0, -(edge / 2 + h / 2)]).translate([0, edge / 6, 0])
        point6_2 = point6_1.translate([edge / 4, 0, 0])
        point6_3 = point6_1.translate([-edge / 4, 0, 0])
        point6_123 = point6_1 + point6_2 + point6_3
        point6_456 = point6_123.mirror([0, 1, 0])
        point6 = point6_123 + point6_456
        dice_with_holes = dice - point1 - point2 - point3 - point4 - point5 - point6
        dice_with_holes = dice_with_holes.mirror([0, 0, 1])
        return(dice_with_holes)
