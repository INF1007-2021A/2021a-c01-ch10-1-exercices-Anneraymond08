#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate


# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    return np.linspace(-1.3, 2.5, num=64)


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
    return np.array([(np.sqrt(c[0]**2 + c[1]**2), np.arctan2(c[1], c[0])) for c in cartesian_coordinates])


def find_closest_index(values: np.ndarray, number: float) -> int:
    return np.abs(values - number).argmin()


def create_plot():
    x = np.linspace(-1, 1, num=250)
    y = x ** 2 * np.sin(1/x**2) + x
    plt.scatter(x, y)
    plt.show()


def monte_carlo(iteration = 5000):
    x_inside_dots = []
    x_outside_dots = []
    y_inside_dots = []
    y_outside_dots = []
    for i in range(iteration):
        x = np.random.random()
        y = np.random.random()
        if np.sqrt(x**2 + y**2) <= 1:
            x_inside_dots.append(x)
            y_inside_dots.append(y)
        else:
            x_outside_dots.append(x)
            y_outside_dots.append(y)
    plt.scatter(x_inside_dots, y_inside_dots)
    plt.scatter(x_outside_dots, y_outside_dots)
    plt.show()
    return len(x_inside_dots) / iteration * 4


def integrate_and_plot():
    result_int = integrate.quad(lambda x: np.exp(-x**2), -np.inf, np.inf)
    x = np.arange(-4,4,0.1)
    y = [integrate.quad(lambda x: np.exp(-x**2), 0, value) for value in x]
    plt.plot(x,y)
    plt.show()
    return result_int[0]


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(linear_values())
    print(coordinate_conversion(np.array([(1, 2), (3, 5), (6, 9)])))
    print(find_closest_index(np.array([1,2,3,8,10]), 9.5))
    create_plot()
    print(monte_carlo(1000))
    integrate_and_plot()
