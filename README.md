[![Build Status](https://travis-ci.org/taxpon/openpyscad.svg?branch=develop)](https://travis-ci.org/taxpon/openpyscad) [![Coverage Status](https://coveralls.io/repos/github/taxpon/openpyscad/badge.svg?branch=develop)](https://coveralls.io/github/taxpon/openpyscad?branch=develop) [![Python3](https://img.shields.io/badge/python-3-blue.svg)](#)
# OpenPySCAD
Python library to generate [OpenSCAD](http://www.openscad.org/) source code. This library provides intuitive interface when you handle 3D data.
OpenPySCAD supports python3(3.5+).

## Install
```bash
pip install openpyscad
```

## How to use
- Write python code as follows:
```python
import openpyscad as ops
c1 = ops.Cube([10, 20, 10])
c2 = ops.Cube([20, 10, 10])
(c1 + c2).write("sample.scad")
```

- Generated code will be written in the "sample.scad".
- For automatic reload and preview, you need to turn on "Design > Automatic Reload and Preview" in OpenSCAD
```openscad
union(){
    cube([10, 20, 10]);
    cube([20, 10, 10]);
};
```

## Generated code examples

### 3D Shapes

Python:
```python
Sphere(r=10, _fn=100)
Cube([10, 10, 10])
Cylinder(h=10, r=10)
p = Polyhedron(
    points=[
        [10, 10, 0], [10, -10, 0], [-10, -10, 0], [-10, 10, 0],  [0, 0, 10]
    ],
    faces=[
        [0, 1, 4], [1, 2, 4], [2, 3, 4], [3, 0, 4],  [1, 0, 3], [2, 1, 3]
    ]
)
```

Generated OpenSCAD code:
```openscad
sphere(r=10, $fn=100);
cube(size=[10, 10, 10]);
cylinder(h=10, r=10);
polyhedron(points=[[10, 10, 0], [10, -10, 0], [-10, -10, 0], [-10, 10, 0], [0, 0, 10]], faces=[[0, 1, 4], [1, 2, 4], [2, 3, 4], [3, 0, 4], [1, 0, 3], [2, 1, 3]]);
```

### Boolean Operations

Python:
```python
# Union
Cube([20, 10, 10]) + Cube([10, 20, 10])

# You can also write like this
u = Union()
u.append(Cube[20, 10, 10])
u.append(Cube[10, 20, 10])

# Difference
Cube([20, 10, 10]) - Cube([10, 20, 10])

# You can also write like this
i = Difference()
i.append(Cube[20, 10, 10])
i.append(Cube[10, 20, 10])

# Intersection
Cube([20, 10, 10]) & Cube([10, 20, 10])

# You can also write like this
i = Intersection()
i.append(Cube[20, 10, 10])
i.append(Cube[10, 20, 10])
```

Generated OpenSCAD code:
```openscad
// Union
union(){
    cube([20, 10, 10])
    cube([10, 20, 10])
};

// Difference
difference(){
    cube([20, 10, 10]);
    cube([10, 20, 10]);
};

// Intersection
intersection(){
    cube([20, 10, 10]);
    cube([10, 20, 10]);
};
```

### Transformations

Python:
```python
# Translate
Cube([20, 10, 10]).translate([10, 10, 10])

# Rotate
Cube([20, 10, 10]).rotate([0, 0, 45])

# Scale
Cube([20, 10, 10]).scale([2, 1, 1])

# Resize
Cube([20, 10, 10]).resize([2, 1, 1])

# Mirror
Cube([20, 10, 10]).mirror([1, 1, 1])

# Color
Cube([20, 10, 10]).color("Red")

# Offset
Circle(10).offset(10)
```

Generated OpenSCAD code:
```openscad
// Translate
translate(v=[10, 10, 10]){
    cube([20, 10, 10]);
};

// Rotate
rotate(v=[0, 0, 45]){
    cube([20, 10, 10]);
};

// Scale
scale(v=[2, 1, 1]){
    cube([20, 10, 10]);
};

// Resize
resize(newsize=[2, 1, 1]){
    cube(size=[20, 10, 10]);
};

// Mirror
mirror([1, 1, 1]){
    cube(size=[20, 10, 10]);
};

// Color
color("Red"){
    cube(size=[20, 10, 10]);
};

// Offset
offset(r=10){
    circle(r=10);
};
```

### Modifiers
OpenPySCAD provides [modifiers](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Modifier_Characters) interfaces ("*", "!", "#" and "%").

Python:
```python
c1 = Cube(10)
c1.disable()         # add "*" character
c1.show_only()       # add "!" character
c1.is_debug()        # add "#" character
c1.is_transparent()  # add "&" character
```

## Interested in contribution?
Please read [CONTRIBUTING.md](./CONTRIBUTING.md). 

