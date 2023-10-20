import numpy as np
import matplotlib.pyplot as plt
import random

Pmax = 10
r = 1
A = 0.3
L = 15
T = 3
delta_p = 5
p1 = 35
delta_e = 2
delta_r = 3
N = 128

def print_plot(arr):
    fig, ax = plt.subplots()
    ax.pcolormesh(arr, vmin=-1, vmax=1)
    ax.imshow(arr, cmap='winter')
    plt.show()

def initial_data_individual_half(N):
    individual_position = np.zeros((N, N))
    energy_individual = np.zeros((N, N))
    time_life = np.zeros((N, N))
    k = 0

    while k < N*N*A:
        x = random.randint(0, N - 1)
        y = random.randint(0, N - 1)
        #if y > int(N/2):
        if individual_position[x][y] != 1:
            individual_position[x][y] = 1
            energy_individual[x][y] = 1
            time_life[x][y] = 1
            k += 1

    return [individual_position, energy_individual, time_life]

    individual_position = np.zeros((N, N))
    energy_individual = np.zeros((N, N))
    time_life = np.zeros((N, N))
    k = 0

    while k < N*N*A:
        x = random.randint(0, N-1)
        y = random.randint(0, N - 1)
        if individual_position[x][y] != 1:
            individual_position[x][y] = 1
            energy_individual[x][y] = 1
            time_life[x][y] = 1
            k += 1

    return [individual_position, energy_individual, time_life]

def time(time_life):

    for i in range(len(time_life)):
        for j in range(len(time_life)):
            if time_life[i][j] > 0:
                time_life[i][j] += 1

    return time_life

def plot_energy_update(plot):

    for i in range(len(plot)):
        for j in range(len(plot)):
            if plot[i][j] < Pmax:
                plot[i][j] += r

    return plot

def fooding(plot, energy_individual):

    for i in range(len(plot)):
        for j in range(len(plot)):
            if energy_individual[i][j] > 0:
                if plot[i][j] >= delta_p:
                    if energy_individual[i][j] + delta_p <= p1:
                        energy_individual[i][j] += delta_p
                        plot[i][j] -= delta_p
                    else:
                        energy_individual[i][j] += p1
                        plot[i][j] -= p1 - energy_individual[i][j]
                else:
                    energy_individual[i][j] += plot[i][j]
                    plot[i][j] = 0

    return [plot, energy_individual]

def activity(energy_individual):

    energy_individual -= delta_e

    return energy_individual

def move(individual_position, energy_individual, time_life):

    check_move = np.zeros((len(individual_position),len(individual_position)))

    for i in range(len(individual_position)):
        for j in range(len(individual_position)):
            if individual_position[i][j] == 1 and check_move[i][j] == 0:
                x1 = i - 1
                x2 = i + 2
                y1 = j - 1
                y2 = j + 2
                if i == 0:
                    x1 = i
                if i == N - 1:
                    x2 = i + 1
                if j == 0:
                    y1 = j
                if j == N - 1:
                    y2 = j + 1

                if  np.sum(individual_position[x1:x2, y1: y2]) < ((x2-x1) * (y2 - y1))-1:

                    k = i
                    l = j

                    while not (individual_position[k][l] == 0):
                        k = random.randint(x1, x2-1)
                        l = random.randint(y1, y2-1)

                    individual_position[k][l] = 1
                    energy_individual[k][l] = energy_individual[i][j]
                    time_life[k][l] = time_life[i][j]
                    check_move[k][l] = 1

                    individual_position[i][j] = 0
                    energy_individual[i][j] = 0
                    time_life[i][j] = 0
    return [individual_position, energy_individual, time_life]

def death(individual_position, energy_individual, time_life):
    N = len(individual_position)

    for i in range(N):
        for j in range(N):
            if (time_life[i][j] > L or energy_individual[i][j] <= 0):

                time_life[i][j] = 0
                individual_position[i][j] = 0
                energy_individual[i][j] = 0

    return [individual_position, energy_individual, time_life]

def reproduction(individual_position, energy_individual, time_life):

    N = len(time_life)

    check_reproduction = np.zeros((N,N))

    for i in range(N):
        for j in range(N):
            if individual_position[i][j] == 1 and time_life[i][j] >= T and energy_individual[i][j] > delta_r and check_reproduction[i][j] == 0:

                x1 = i - 1
                x2 = i + 2
                y1 = j - 1
                y2 = j + 2
                if i == 0:
                    x1 = i
                if i == N - 1:
                    x2 = i + 1
                if j == 0:
                    y1 = j
                if j == N - 1:
                    y2 = j + 1


                if  np.sum(individual_position[x1:x2, y1: y2]) < ((x2-x1) * (y2 - y1))-1:

                    k = i
                    l = j

                    while not (individual_position[k][l] == 0):
                        k = random.randint(x1, x2-1)
                        l = random.randint(y1, y2-1)

                    individual_position[k][l] = 1
                    energy_individual[k][l] = energy_individual[i][j] - delta_r
                    time_life[k][l] = time_life[i][j]
                    check_reproduction[k][l] = 1
                    time_life[k][l] = 1

                    energy_individual[i][j] = delta_r
                    time_life[i][j] = 1



    return [individual_position, energy_individual, time_life]

def BaseKA(iter, N):

    plot = np.zeros((N, N)) + Pmax

    initial_all = initial_data_individual_half(N)
    individual_position = initial_all[0]
    energy_individual = initial_all[1]
    time_life = initial_all[2]


    print('Stupid, iter = {}'.format(0))
    print_plot(individual_position)

    for k in range(iter):

        fooding(plot,energy_individual)
        activity(energy_individual)
        death(individual_position, energy_individual, time_life)
        move(individual_position, energy_individual, time_life, plot)
        reproduction(individual_position, energy_individual, time_life)
        time(time_life)
        death(individual_position, energy_individual, time_life)
        plot_energy_update(plot)

        print('Iter = {}'.format(k + 1))
        if k == 14:
            print_plot(individual_position)

    return [plot, time_life, energy_individual]

def max_array(arr):

    N = max(len(arr[0]),len(arr))
    M = min(len(arr[0]),len(arr))
    arr1 = np.copy(arr)
    max_arr = np.zeros((len(arr)*len(arr[0])))
    xy = np.zeros(((len(arr)*len(arr[0])),2))
    for i in range(len(arr)*len(arr[0])):
        max_arr[i] = np.max(arr1)
        x = np.argmax(arr1)
        if N == len(arr[0]):
            xy[i] = [(int(x // N)), int(x % N)]
        else:
            xy[i] = [(int(x // M)), int(x % M)]
        arr1[int(xy[i][0])][int(xy[i][1])] = 0

    xy = np.array(xy, dtype=int)
    max_arr = np.array(max_arr, dtype=int)

    return [max_arr, xy]

def move(individual_position, energy_individual, time_life, plot):

    check_move = np.zeros((len(individual_position),len(individual_position)))

    for i in range(len(individual_position)):
        for j in range(len(individual_position)):
            if individual_position[i][j] == 1 and check_move[i][j] == 0:
                x1 = i - 1
                x2 = i + 2
                y1 = j - 1
                y2 = j + 2
                if i == 0:
                    x1 = i
                if i == N - 1:
                    x2 = i + 1
                if j == 0:
                    y1 = j
                if j == N - 1:
                    y2 = j + 1

                if  np.sum(individual_position[x1:x2, y1: y2]) < ((x2-x1) * (y2 - y1))-1 and np.max(plot[x1:x2, y1: y2]) != plot[i][j]:

                    max_neighborhood, xy_neighborhood = max_array(plot[x1:x2, y1: y2])

                    for it in range((x2-x1) * (y2 - y1)-1):

                        k = xy_neighborhood[it][0]+x1
                        l = xy_neighborhood[it][1]+y1

                        if individual_position[k][l] == 0:

                            individual_position[k][l] = 1
                            energy_individual[k][l] = energy_individual[i][j]
                            time_life[k][l] = time_life[i][j]
                            check_move[k][l] = 1

                            individual_position[i][j] = 0
                            energy_individual[i][j] = 0
                            time_life[i][j] = 0

                            break
    return [individual_position, energy_individual, time_life]

def Modific(iter, N):

    plot = np.zeros((N, N)) + Pmax

    initial_all = initial_data_individual_half(N)
    individual_position = initial_all[0]
    energy_individual = initial_all[1]
    time_life = initial_all[2]

    print('Iter = {}'.format(0))
    print_plot(individual_position)
    

    for k in range(iter):

        fooding(plot, energy_individual)
        activity(energy_individual)
        death(individual_position, energy_individual, time_life)
        move(individual_position, energy_individual, time_life, plot)
        reproduction(individual_position, energy_individual, time_life)
        time(time_life)
        death(individual_position, energy_individual, time_life)
        plot_energy_update(plot)
        

        print('Iter = {}'.format(k + 1))
        if k > 14:
            print_plot(individual_position)

    plt.figure()
    return [plot, time_life, energy_individual]

BaseKA(100, N)
#Modific(250, N)
