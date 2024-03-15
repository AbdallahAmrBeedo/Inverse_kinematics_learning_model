from math import cos, sin, pi, radians
import numpy as np
import pandas as pd

A1 = 1
A2 = 1

def forward_kinematic_model(q1:float, q2:float) -> tuple:
    """
    This function solves the 2 manipulator link forward kinematics to determine the position of the end effector.

    Args:
        q1: angle of the first link in degrees. (float)
        q2: angle of the second link in degrees. (float)
    
    Returns:
        (x,y): position of the end effector. (tuple)

    """
    q1 = radians(q1)
    q2 = radians(q2)
    x = A1 * cos(q1) + A2 * cos(q1+q2)
    y = A1 * sin(q1) + A2 * sin(q1+q2)
    return x,y

q1_array = np.linspace(0,180,50)
q2_array = np.linspace(0,180,50)

data_set = {"x":[], "y":[], "q1":[], "q2": []}

for q1 in q1_array:
    for q2 in q2_array:
        x , y = forward_kinematic_model(q1, q2)
        data_set["x"].append(x)
        data_set["y"].append(y)
        data_set["q1"].append(q1)
        data_set["q2"].append(q2)

df = pd.DataFrame(data_set)

df.to_csv("manipulator_dataset_small.csv", index=False)