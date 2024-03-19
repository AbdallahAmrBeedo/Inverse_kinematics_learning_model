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
        (x, y, theta): position and orientation of the end effector. (tuple)
    """
    x = A1 * cos(q1) + A2 * cos(q1+q2)
    y = A1 * sin(q1) + A2 * sin(q1+q2)
    theta = q1 + q2
    return round(x,4),round(y,4), theta

n_angles = 200 # number of divisions 

q1_array = np.linspace(0,1.8*pi,n_angles)
q2_array = np.linspace(0,1.8*pi,n_angles)

data_set = {"x":[], "y":[], "theta":[], "q1":[], "q2": []}

for q1 in q1_array:
    for q2 in q2_array:
        x , y, theta = forward_kinematic_model(q1, q2)
        data_set["x"].append(x)
        data_set["y"].append(y)
        data_set["theta"].append(theta)
        data_set["q1"].append(q1)
        data_set["q2"].append(q2)

df = pd.DataFrame(data_set)

df.to_csv(f"data/manipulator_dataset.csv", index=False)
