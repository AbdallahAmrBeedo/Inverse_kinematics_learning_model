import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from math import cos, sin, pi, radians

A1 = 1
A2 = 1

def forward_kinematic_model(q1:float, q2:float) -> tuple:
    """
    This function solves the 2 manipulator link forward kinematics to determine the position of the end effector and the joints.

    Args:
        q1: angle of the first link in degrees. (float)
        q2: angle of the second link in degrees. (float)
    
    Returns:
        (x_1,y1): position of the second joint. (tuple)
        (x_e,ye): position of the end effector. (tuple)

    """
    theta = q1 + q2
    q1 = radians(q1)
    q2 = radians(q2)
    x_1 = A1 * cos(q1)
    y_1 = A1 * sin(q1)
    x_e = A1 * cos(q1) + A2 * cos(q1+q2)
    y_e = A1 * sin(q1) + A2 * sin(q1+q2)
    print(f"end effector position: ({x_e}, {y_e})")
    print(f"end effector orientation: {theta}")
    return x_1, y_1, x_e, y_e

def plot_manipulator(q1:float, q2:float):
    """
    This function plotes 2 manipulator link given the angles of the links.

    Args:
        q1: angle of the first link in degrees. (float)
        q2: angle of the second link in degrees. (float)
    """
    x_1, y_1, x_e, y_e = forward_kinematic_model(q1, q2)
    plt.scatter([0], [0])
    plt.plot([0, x_1], [0, y_1], linewidth='3')
    plt.scatter([x_1], [y_1])
    plt.plot([x_1, x_e], [y_1, y_e], linewidth='3')
    plt.xlim([-2,2])
    plt.ylim([-2,2])
    plt.title('2 link manipulator')
    plt.show()

def inv_kine_learning_model(x:float, y:float, theta:float):
    """
    A learning based model to solve the inverse kineamtics of a 2 link manipulator.

    Args:
        x: position of the end effector on x axis. (float)
        y: position of the end effector on y axis. (float)
        theta: orientation of the end effector in degrees. (float)

    Returns:
        (q1, q2): angles of the 2 link manipulator to give the desired position in degree
    """
    angles = np.array(inv_kine_model(tf.constant([[x,y,radians(theta)]])))[0] * 180 / pi

    return angles

if __name__ == "__main__":
    model_size = "small" # chose the model size: "large", "medium", "small"
    inv_kine_model = tf.keras.models.load_model(f'models/invkine_model.h5')
    print("Model Loaded")
    while True:
        try:
            print("Press Ctrl+C and hit Enter to exit.")
            x = float(input("Enter the x position: "))
            y = float(input("Enter the y position: "))
            theta = float(input("Enter the theta: "))
            q1, q2 = inv_kine_learning_model(x, y, theta)
            print("Close the figure window to continue...")
            plot_manipulator(q1, q2)
        except KeyboardInterrupt:
            print("Ending Program...")
            break