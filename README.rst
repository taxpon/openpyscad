OpenPySCAD
==========

.. image:: https://travis-ci.org/taxpon/openpyscad.svg
    :target: https://travis-ci.org/taxpon/openpyscad

.. image:: https://coveralls.io/repos/github/taxpon/openpyscad/badge.svg?branch=master
    :target: https://coveralls.io/github/taxpon/openpyscad?branch=master

Python library to generate OpenSCAD source code. This library provides intuitive interface when you handle 3D data.


Usage
-------

1. Install openpyscad via pip

.. code-block:: bash

    $ pip install openpyscad

2. Write python code as follows:

.. code-block:: python

    import opnepyscad as ops
    c1 = ops.Cube([10, 20, 10])
    c2 = ops.Cube([20, 10, 10])
    (c1 + c2).write("sample.scad")

3. Generated code will be written in the "sample.scad". OpenSCAD can detect the change of your code and reload automatically (that's so cool).


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

LICENSE
-------
MIT
