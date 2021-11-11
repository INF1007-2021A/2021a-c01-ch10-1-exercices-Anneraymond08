#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np


# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    x = np.linspace(-1.3, 2.5, num=64)
    return np.array(x)


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
    z = cartesian_coordinates
    x = []
    y = []
    for value in z:
        print(value)
        x.append(value[0])
        y.append(value[1])
    r = np.sqrt(x**2+y**2)
    t = np.arctan2(y, x)
    return np.array([r, t])


def find_closest_index(values: np.ndarray, number: float) -> int:
    return 0


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(linear_values())
    print(coordinate_conversion(linear_values()))

