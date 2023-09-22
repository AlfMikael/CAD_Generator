"""
To test whether cadquery and the import of step files work.
Or any other tests.
"""


# Create and import a basic cantilever part
import cadquery as cq
import numpy as np
import math

import os.path, sys
BASE_PARAMETERS = {}
BASE_PARAMETERS["thickness"] = 4
BASE_PARAMETERS["length"] = 12
BASE_PARAMETERS["strain"] = 0.04
BASE_PARAMETERS["nose_angle"] = 85
BASE_PARAMETERS["extrusion_distance"] = 4


def create_cantilever(modified_parameters=dict(), name="test_cantilever"):
    p = BASE_PARAMETERS.copy()
    p.update(modified_parameters)
    # Create part
    th = p["thickness"]
    l = p["length"]
    strain = p["strain"]
    nose_angle = math.radians(p["nose_angle"])
    fatness = p["extrusion_distance"]

    arm_length = l

    nose_height = 1.09 * strain * arm_length ** 2 / th
    nose_x = nose_height / math.tan(nose_angle)

    # Point coordinates no radius business
    p_c = [(0, 0),  # Start
           (l * 1.20 + nose_x, 1 / 2 * th * 1.25),
           (l * 1.20 + nose_x, 3 / 4 * th),
           (l * 1.07 + nose_x, th + nose_height),
           (l + nose_x, th + nose_height),
           (l, th),
           (0, th)]

    sketch = (
        cq.Workplane("XY")
    )

    data = np.array(p_c)

    x = data[:, 0]
    y = data[:, 1]

    sketch = sketch.moveTo(x[0], y[0])
    for i in range(1, len(x)):
        x1, y1 = x[i], y[i]
        sketch = sketch.lineTo(x1, y1)

    sketch = sketch.close()
    sketch = sketch.extrude(fatness)

    assy = cq.Assembly()
    assy.add(sketch, name="sketch", color=cq.Color("gray"))
    cq.exporters.export(sketch, name + ".step")
