import matplotlib.pyplot as plt
import numpy as np


def plot_trajectory(*filenames: str):
    fig = plt.figure(figsize=(18, 7), tight_layout=True)

    earth = [plt.Circle((0, 0), 6.378e6, color='lightblue') for i in range(3)]
    axes = []

    for i in range(3):
        axes.append(fig.add_subplot(131 + i))
        axes[i].add_patch(earth[i])
        axes[i].set_aspect("equal")
        axes[i].grid()

    for filename in filenames:
        arr = np.loadtxt(filename, delimiter=",")
        x = arr[:, 1]
        y = arr[:, 2]
        z = arr[:, 3]
        axes[0].plot(x, y, label=filename)
        axes[0].set_ylabel("y position (m)")
        axes[0].set_xlabel("x position (m)")
        axes[1].plot(y, z, label=filename)
        axes[1].set_ylabel("z position (m)")
        axes[1].set_xlabel("y position (m)")
        axes[2].plot(x, z, label=filename)
        axes[2].set_ylabel("z position (m)")
        axes[2].set_xlabel("x position (m)")
        axes[0].set_title("xy")
        axes[1].set_title("yz")
        axes[2].set_title("xz")

    plt.legend()
    plt.show()


def plot_from_array(t, arr):
    fig = plt.figure(figsize=(12, 5), tight_layout=True)

    earth = [plt.Circle((0, 0), 6.378e6, color='lightblue') for i in range(3)]
    axes = []

    for i in range(3):
        axes.append(fig.add_subplot(231 + i))
        axes[i].add_patch(earth[i])
        axes[i].set_aspect("equal")
        axes[i].grid()

    x = arr[:, 0]
    y = arr[:, 1]
    z = arr[:, 2]
    axes[0].plot(x, y)
    axes[0].set_ylabel("y position (m)")
    axes[0].set_xlabel("x position (m)")
    axes[1].plot(y, z)
    axes[1].set_ylabel("z position (m)")
    axes[1].set_xlabel("y position (m)")
    axes[2].plot(x, z)
    axes[2].set_ylabel("z position (m)")
    axes[2].set_xlabel("x position (m)")
    axes[0].set_title("xy")
    axes[1].set_title("yz")
    axes[2].set_title("xz")

    axes.append(fig.add_subplot(212))
    # Plot altitude above each
    altitude = np.sqrt(x**2 + y**2 + z**2) - 6.378e6
    axes[3].plot(t/86400, altitude)
    axes[3].set_ylabel("Altitude (m)")
    axes[3].set_xlabel("Mission Time (d)")

    plt.show()


def plot_error(diff: np.ndarray):
    fig = plt.figure(figsize=(18, 7), tight_layout=True)

    axes = []

    for i in range(3):
        axes.append(fig.add_subplot(131 + i))
        axes[i].set_ylabel("Solver Error (m)")
        axes[i].set_xlabel("Integrator Step Number")
        axes[i].grid()

    for i in range(3):
        axes[i].plot(diff[:, i])

    axes[0].set_title("x error")
    axes[1].set_title("y error")
    axes[2].set_title("z error")

    plt.show()


if __name__ == "__main__":
    plot_trajectory("c_code/simplified.csv", "c_code/advanced.csv")
