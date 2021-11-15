# Lauren Roe
# CST-305
# This is my own work

# The purpose of this is to use dynamical systems to model the deterministically chaotic behavior
import numpy as np                      # imported to use linspace
import matplotlib.pyplot as plt         # imported in order to plot the results
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import


def lorenz(x, y, z, r, s=10, b=2.667):          # s and b are defined as set values
    '''
    Given:
       x, y, z: a point of interest in three dimensional space
       s, r, b: parameters defining the lorenz attractor
    Returns:
       x_dot, y_dot, z_dot: values of the lorenz attractor's partial
           derivatives at the point x, y, z
    '''
    x_dot = s*(y - x)                   # equation given for xdot in the Lorenz System
    y_dot = r*x - y - x*z               # equation given for ydot in the Lorenz System
    z_dot = x*y - b*z                   # equation given for zdot in the Lorenz System
    return x_dot, y_dot, z_dot          # returns the equations


def plot(r):                            # plots the graphs

    for i in range(num_steps):
        x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i], r)    # sets the variable equal to the lorenz equations
        xs[i + 1] = xs[i] + (x_dot * dt)            # uses the formula for the next step in the array with x
        ys[i + 1] = ys[i] + (y_dot * dt)            # uses the formula for the next step in the array with y
        zs[i + 1] = zs[i] + (z_dot * dt)            # uses the formula for the next step in the array with z

    fig = plt.figure()                  # plots the 3D figure
    ax = fig.gca(projection='3d')       # defines the projection type

    ax.plot(xs, ys, zs, lw=0.5)         # plots the x y and z values
    ax.set_xlabel("X Axis")             # labels the x axis
    ax.set_ylabel("Y Axis")             # labels the y axis
    ax.set_zlabel("Z Axis")             # labels the z axis
    ax.set_title("Lorenz Attractor")    # titles the graphs

    plt.show()                          # shows the final plot

    str = 'r = '                        # creates the string for the title of the graph
    plt.plot(t, xs)                     # plots t on the x axis and xs on the y
    plt.xlabel("t")                     # labels the x axis
    plt.ylabel("xs")                    # labels the y axis
    plt.title('%s%s' %(str, r))         # titles the graph
    plt.show()                          # shows the plot

    plt.plot(t, ys)                     # plots t on the x axis and xs on the y
    plt.xlabel("t")                     # labels the x axis
    plt.ylabel("ys")                    # labels the y axis
    plt.title('%s%s' % (str, r))        # titles the graph
    plt.show()                          # shows the plot

    plt.plot(t, zs)                     # plots t on the x axis and xs on the y
    plt.xlabel("t")                     # labels the x axis
    plt.ylabel("zs")                    # labels the y axis
    plt.title('%s%s' % (str, r))        # titles the graph
    plt.show()                          # shows the plot


dt = 0.01                               # change in t in the equation
num_steps = 10000                       # the number of values in the array

# Need one more for the initial values
xs = np.empty(num_steps + 1)                # creates an array of the x values
ys = np.empty(num_steps + 1)                # creates an array of the y values
zs = np.empty(num_steps + 1)                # creates an array of the z values

# Set initial values
xs[0], ys[0], zs[0] = (0., 1., 1.05)        # sets the first values of the x y and z arrays

t = np.linspace(0, 100, 10001)              # gets the t values

# Step through "time", calculating the partial derivatives at the current point
# and using them to estimate the next point

plot(1)             # changes the r value to 1
plot(10)            # changes the r value to 10
plot(28)            # changes the r value to 28
