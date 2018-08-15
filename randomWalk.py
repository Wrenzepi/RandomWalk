#!/usr/bin/env python3
'''
Author: David Kohler
randomWalk.py
'''

import matplotlib.pyplot as plt
import numpy as np
import plotly
import plotly.graph_objs as go
import seaborn as sns


def user_customization_1D():
    '''
    Prompts user for customization options for 1D
    '''
    sns.set_palette('husl')

    n_string = input('Enter length of walk (< 500,001): ')
    while((not n_string.isdigit()) or (int(n_string) < 1)
            or ((int(n_string) > 500000))):
        n_string = input('Enter valid length of walk (< 500,001): ')

    n = int(n_string)

    walkers_string = input('Enter number of walkers (< 21): ')
    while((not walkers_string.isdigit()) or (int(walkers_string) < 1)
            or ((int(walkers_string) > 20))):
        walkers_string = input('Enter valid number of walkers (< 21): ')

    walkers = int(walkers_string)

    return n, walkers

def user_customization_2D():
    '''
    Prompts user for customization options for 2D
    '''
    sns.set_palette('husl')

    n_string = input('Enter length of walk (< 250,001): ')
    while((not n_string.isdigit()) or (int(n_string) < 1)
            or ((int(n_string) > 250000))):
        n_string = input('Enter valid length of walk (< 250,001): ')

    n = int(n_string)

    walkers_string = input('Enter number of walkers (< 21): ')
    while((not walkers_string.isdigit()) or (int(walkers_string) < 1)
            or ((int(walkers_string) > 20))):
        walkers_string = input('Enter valid number of walkers (< 21): ')

    walkers = int(walkers_string)

    return n, walkers

def user_customization_3D():
    '''
    Prompts user for customization options for 3D
    '''
    sns.set_palette('husl')

    n_string = input('Enter length of walk (< 100,001): ')
    while((not n_string.isdigit()) or (int(n_string) < 1)
            or ((int(n_string) > 100000))):
        n_string = input('Enter valid length of walk (< 100,001): ')

    n = int(n_string)

    walkers_string = input('Enter number of walkers (< 11): ')
    while((not walkers_string.isdigit()) or (int(walkers_string) < 1)
            or ((int(walkers_string) > 10))):
        walkers_string = input('Enter valid number of walkers (< 11): ')

    walkers = int(walkers_string)

    return n, walkers

def make_arrays_1D(n, num_arrays):
    '''
    Generate num_arrays number of random walks each of length n (1D)
    '''
    data = []

    for i in range(num_arrays):
        y = np.zeros(n)

        for i in range(1, n):
            num = np.random.randint(1, 3)
            if num == 1:
                y[i] = y[i-1] + 1
            elif num == 2:
                y[i] = y[i-1] - 1

        trace = go.Scatter(
            x = np.arange(n),
            y = y,
            line=dict(
                width=0.3
            )
        )
        data.append(trace)

    return data

def make_arrays_2D(n, num_arrays):
    '''
    Generate num_arrays number of random walks each of length n (2D)
    '''
    data = []
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

        trace = go.Scatter(
            x = x,
            y = y,
            line=dict(
                width=0.3
            )
        )
        data.append(trace)

    return data

def make_arrays_3D(n, num_arrays):
    '''
    Generate num_arrays number of random walks each of length n (3D)
    '''
    data = []
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

        trace = go.Scatter3d(
            x = x,
            y = y,
            z = z,
            marker=dict(
                size=2,
                opacity=0.6
            )
        )
        data.append(trace)

    return data

def plot(data):
    '''
    Plot each array in data on same plot (any dimension)
    '''
    layout = go.Layout(
        title='Random Walk',
        margin=dict(
            l=0,
            r=0,
            b=25,
            t=50
        )
    )
    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig)


if __name__ == '__main__':
    print("Enter 1 for 1D visualization, 2 for 2D, 3 for 3D")
    D = input('+>')
    while((D != '1') and (D != '2') and (D != '3')):
        print('Please choose a valid option')
        D = input('+>')
    if D == '1':
        n, walkers = user_customization_1D()
        data = make_arrays_1D(n, walkers)
        plot(data)
    elif D == '2':
        n, walkers = user_customization_2D()
        data = make_arrays_2D(n, walkers)
        plot(data)
    else:
        n, walkers = user_customization_3D()
        data = make_arrays_3D(n, walkers)
        plot(data)
