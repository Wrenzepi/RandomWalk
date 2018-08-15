#!/usr/bin/env python3
'''
Author: David Kohler
random_walk.py
'''

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import seaborn as sns


def user_customization_1D():
    '''
    Prompts user for customization options for 1D
    '''
    sns.set_palette('husl')

    n_string = input('Enter length of walk (< 100,001): ')
    while((not n_string.isdigit()) or (int(n_string) < 1)
            or ((int(n_string) > 100000))):
        n_string = input('Enter valid length of walk (< 100,001): ')

    n = int(n_string)

    walkers_string = input('Enter number of walkers (< 41): ')
    while((not walkers_string.isdigit()) or (int(walkers_string) < 1)
            or ((int(walkers_string) > 40))):
        walkers_string = input('Enter valid number of walkers (< 41): ')

    walkers = int(walkers_string)

    return n, walkers

def user_customization_2D():
    '''
    Prompts user for customization options for 2D
    '''
    sns.set_palette('husl')

    n_string = input('Enter length of walk (< 500,001): ')
    while((not n_string.isdigit()) or (int(n_string) < 1)
            or ((int(n_string) > 500000))):
        n_string = input('Enter valid length of walk (< 500,001): ')

    n = int(n_string)

    walkers_string = input('Enter number of walkers (< 31): ')
    while((not walkers_string.isdigit()) or (int(walkers_string) < 1)
            or ((int(walkers_string) > 30))):
        walkers_string = input('Enter valid number of walkers (< 31): ')

    walkers = int(walkers_string)

    return n, walkers

def user_customization_3D():
    '''
    Prompts user for customization options for 3D
    '''
    sns.set_palette('husl')

    n_string = input('Enter length of walk (< 50,001): ')
    while((not n_string.isdigit()) or (int(n_string) < 1)
            or ((int(n_string) > 50000))):
        n_string = input('Enter valid length of walk (< 50,001): ')

    n = int(n_string)

    walkers_string = input('Enter number of walkers (< 16): ')
    while((not walkers_string.isdigit()) or (int(walkers_string) < 1)
            or ((int(walkers_string) > 15))):
        walkers_string = input('Enter valid number of walkers (< 16): ')

    walkers = int(walkers_string)

    return n, walkers

def make_arrays_1D(n, num_arrays):
    '''
    Generate num_arrays number of random walks each of length n (1D)
    '''
    y_arrays = []

    for i in range(num_arrays):
        y = np.zeros(n)

        for i in range(1, n):
            num = np.random.randint(1, 3)
            if num == 1:
                y[i] = y[i-1] + 1
            elif num == 2:
                y[i] = y[i-1] - 1


        y_arrays.append(y)

    return y_arrays

def make_arrays_2D(n, num_arrays):
    '''
    Generate num_arrays number of random walks each of length n (2D)
    '''
    x_arrays = []
    y_arrays = []

    for i in range(num_arrays):
        x = np.zeros(n)
        y = np.zeros(n)

        for i in range(1, n):
            num = np.random.randint(1, 5)
            if num == 1:
                x[i] = x[i-1] + 1
                y[i] = y[i-1]
            elif num == 2:
                x[i] = x[i-1] - 1
                y[i] = y[i-1]
            elif num == 3:
                x[i] = x[i-1]
                y[i] = y[i-1] + 1
            elif num == 4:
                x[i] = x[i-1]
                y[i] = y[i-1] - 1

        x_arrays.append(x)
        y_arrays.append(y)

    return x_arrays, y_arrays

def make_arrays_3D(n, num_arrays):
    '''
    Generate num_arrays number of random walks each of length n (3D)
    '''
    x_arrays = []
    y_arrays = []
    z_arrays = []

    for i in range(num_arrays):
        x = np.zeros(n)
        y = np.zeros(n)
        z = np.zeros(n)

        for i in range(1, n):
            num = np.random.randint(1, 7)
            if num == 1:
                x[i] = x[i-1] + 1
                y[i] = y[i-1]
                z[i] = z[i-1]
            elif num == 2:
                x[i] = x[i-1] - 1
                y[i] = y[i-1]
                z[i] = z[i-1]
            elif num == 3:
                x[i] = x[i-1]
                y[i] = y[i-1] + 1
                z[i] = z[i-1]
            elif num == 4:
                x[i] = x[i-1]
                y[i] = y[i-1] - 1
                z[i] = z[i-1]
            elif num == 5:
                x[i] = x[i-1]
                y[i] = y[i-1]
                z[i] = z[i-1] + 1
            elif num == 6:
                x[i] = x[i-1]
                y[i] = y[i-1]
                z[i] = z[i-1] - 1

        x_arrays.append(x)
        y_arrays.append(y)
        z_arrays.append(z)

    return x_arrays, y_arrays, z_arrays

def plot_1D(y_arrays, num_walkers):
    '''
    Plot each array in y_arrays on same plot (1D)
    '''
    colors = get_color_array()
    x = range(len(y_arrays[0]))
    for i in range(num_walkers):
        plt.plot(x, y_arrays[i], alpha=0.5, color=colors[i])
    plt.axis('off')
    plt.show()

def plot_2D(x_arrays, y_arrays):
    '''
    Plot each array in x_arrays and y_arrays on same plot (2D)
    '''
    colors = get_color_array()
    for i in range(len(x_arrays)):
        plt.plot(x_arrays[i], y_arrays[i], alpha=0.7, color=colors[i])
    plt.axis('off')
    plt.show()

def plot_3D(x_arrays, y_arrays, z_arrays):
    '''
    Plot each array in x_arrays and y_arrays on same plot (2D)
    '''
    colors = get_color_array()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(len(x_arrays)):
        ax.plot(x_arrays[i], y_arrays[i], z_arrays[i], alpha=0.7, color=colors[i])
    plt.axis('off')
    plt.show()

def get_color_array():
    '''
    Returns array of colors in random order
    '''
    color_array = ['aquamarine', 'black', 'blue', 'blueviolet', 'brown',
            'chocolate', 'coral', 'crimson', 'cyan',
            'deeppink', 'deepskyblue', 'dodgerblue', 'firebrick',
            'forestgreen', 'fuchsia', 'gainsboro', 'gold', 'goldenrod',
            'gray', 'green', 'greenyellow', 'indianred',
            'indigo', 'lawngreen', 'lime',
            'magenta', 'maroon', 'midnightblue', 'mistyrose',
            'olive', 'orange', 'peru', 'pink', 'plum', 'purple',
            'red', 'rosybrown', 'royalblue', 'saddlebrown',
            'seagreen', 'sienna', 'slateblue',
            'springgreen', 'steelblue', 'tan', 'teal',
            'tomato', 'turquoise', 'violet', 'yellow']

    np.random.shuffle(color_array)
    return color_array


if __name__ == '__main__':
    print("Enter 1 for 1D visualization, 2 for 2D, 3 for 3D")
    D = input('+>')
    while((D != '1') and (D != '2') and (D != '3')):
        print('Please choose a valid option')
        D = input('+>')
    if D == '1':
        n, walkers = user_customization_1D()
        y_arrays = make_arrays_1D(n, walkers)
        plot_1D(y_arrays, walkers)
    elif D == '2':
        n, walkers = user_customization_2D()
        x_arrays, y_arrays = make_arrays_2D(n, walkers)
        plot_2D(x_arrays, y_arrays)
    else:
        n, walkers = user_customization_3D()
        x_arrays, y_arrays, z_arrays = make_arrays_3D(n, walkers)
        plot_3D(x_arrays, y_arrays, z_arrays)
