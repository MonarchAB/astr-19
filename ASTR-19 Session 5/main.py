import numpy as np
import math


def createTable():
    xValues = np.linspace(0, 2 * math.pi, 1000)

    sinValues = [math.sin(x) for x in xValues]

    for x, sinx in zip(xValues, sinValues):
        print(f"{x:<7.3f} {sinx:<7.3f}")


def main():
    createTable()


if __name__ == "__main__":
    main()