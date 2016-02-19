OpenPySCAD
==========

Python library to generate OpenSCAD source code. This library provides intuitive interface when you handle 3D data.


Install
-------
You can install OpenPySCAD from PyPI.

.. code-block:: bash

    $ pip install openpyscad


3D Shape
--------

Cube
^^^^

Source:

.. code-block:: python

    Cube([10, 10, 10])


Generated code: openscad

.. code-block::

    cube([10, 10, 10]);

Boolean Operation
-----------------

Union
^^^^^

Source:

.. code-block:: python

    Cube([20, 10, 10]) + Cube([10, 20, 10])

    # You can also write like this
    u = Union()
    u.append(Cube[20, 10, 10])
    u.append(Cube[10, 20, 10])

Generated code:

.. code-block:: openscad

    union(){
        cube([20, 10, 10])
        cube([10, 20, 10])
    };

Difference
^^^^^^^^^^

Source:

.. code-block:: python

    Cube([20, 10, 10]) - Cube([10, 20, 10])

    # You can also write like this
    i = Difference()
    i.append(Cube[20, 10, 10])
    i.append(Cube[10, 20, 10])

Generated code:

.. code-block:: openscad

    difference(){
        cube([20, 10, 10]);
        cube([10, 20, 10]);
    };


Intersection
^^^^^^^^^^^^

Source:

.. code-block:: python

    Cube([20, 10, 10]) & Cube([10, 20, 10])

    # You can also write like this
    i = Intersection()
    i.append(Cube[20, 10, 10])
    i.append(Cube[10, 20, 10])

Generated code:

.. code-block:: openscad

    intersection(){
        cube([20, 10, 10]);
        cube([10, 20, 10]);
    };


Transform
---------

Translate
^^^^^^

Source:

.. code-block:: python

    Cube([20, 10, 10]).translate([10, 10, 10])

    # You can also write like this
    r = Translate([10, 10, 10])
    r.append(Cube[20, 10, 10])

Generated code:

.. code-block:: openscad

    translate([10, 10, 10]){
        cube([20, 10, 10]);
    };



Rotate
^^^^^^

Source:

.. code-block:: python

    Cube([20, 10, 10]).rotate([0, 0, 45])

    # You can also write like this
    r = Rotate([0, 0, 45])
    r.append(Cube[20, 10, 10])

Generated code:

.. code-block:: openscad

    rotate([0, 0, 45]){
        cube([20, 10, 10]);
    };

